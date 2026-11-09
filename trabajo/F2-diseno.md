# F2: Diseño (insumo para D2 y D6)

Resultado interno. Coherente con F1, sección C (mandato). Diagrama en `trabajo/F2-diagrama.mmd`.

Idea central: el flujo es determinista de punta a punta y funciona sin modelo. El modelo es una pieza opcional que solo traduce el texto libre del miembro a una opción de una lista cerrada. Si el modelo se apaga, el flujo sigue con menús (eso es la versión B, D6).

---

## A. Arquitectura (para D2)

### A1. Componentes y recorrido del miembro

Recorrido en WhatsApp (M5). El mismo backend sirve a la app (M1 dice "en la app"): un solo motor, dos canales.

1. **Canal WhatsApp (tercero: Meta).** WhatsApp Business Platform. Meta recibe el mensaje y lo entrega a Salud360 por webhook (aviso HTTP que Meta envía a nuestro servidor cada vez que llega un mensaje). Respuestas con botones y listas nativas de WhatsApp siempre que se pueda, para reducir texto libre.
2. **Orquestador de conversación (determinista).** Máquina de estados: el código sabe en qué paso está cada conversación (consentimiento, necesidad, ubicación, proveedor, cita) y qué respuestas son válidas en ese paso. Todos los mensajes que lee el miembro son plantillas fijas aprobadas, rellenadas con datos de la base. Ningún texto generado por el modelo llega al miembro.
3. **Identidad y consentimiento (determinista).** Cruza el número de WhatsApp con la base de miembros existente. Si no es miembro: enlace al directorio público y nada más (no se procesa dato de salud). Si es miembro: pide consentimiento (ver A6) antes de aceptar cualquier texto libre. Permite elegir dependiente (la arquitectura lo soporta; queda fuera del piloto de 8 semanas, ver F3).
4. **Reglas de señales de alarma (determinista).** Lista de frases y palabras clave validada por el consejo médico (§05), más una pregunta de chequeo con botones. Se evalúa sobre el texto crudo antes del modelo. Si dispara: mensaje fijo (ver A3) y fin del flujo de búsqueda.
5. **Intérprete de texto (modelo de IA, tercero).** Recibe solo el texto del miembro. Antes de enviarlo, un filtro determinista elimina los identificadores conocidos (nombre del titular y de sus dependientes registrados, teléfono, número de afiliado, correos y números de documento). El texto libre puede contener otros datos personales que el filtro no detecta (nombres de terceros, lugares); por eso el contrato de subprocesador es condición para encender el modelo (A6). Devuelve un objeto con campos cerrados: punto de entrada (de la lista), ubicación mencionada, preferencia de horario, bandera "posible alarma", o "no sé". El miembro confirma con un botón antes de seguir.
6. **Validador de salida (determinista).** Rechaza cualquier valor fuera de la lista cerrada o mal formado. Rechazo, demora o caída del modelo equivalen a "no sé": el orquestador muestra el menú.
7. **Catálogo clínico (datos, no código).** Lista cerrada de puntos de entrada, tabla "necesidad a punto de entrada", reglas de alarma y textos de seguridad. Versionado, con registro de quién aprobó cada versión. Solo cambia por aprobación del consejo médico.
8. **Búsqueda y ranking de sedes (determinista).** Consulta SQL sobre el catálogo de proveedores limpio: especialidades del punto de entrada, cercanía, precio y disponibilidad. Orden fijo y explicable (A4). Devuelve pocas opciones con precio tomado de la base.
9. **Agendamiento en tres niveles (determinista).** Ver A4.
10. **Traspaso a humano.** Soporte (WhatsApp, §01) recibe la conversación con el contexto ya resuelto (punto de entrada, cantón, sedes vistas), para no empezar de cero los 6 min 40 s (§03).
11. **Telemedicina (clínicos por consulta, §05).** Destino de derivación solo bajo reglas (A3).
12. **Back office de datos (fuera de línea).** Limpieza del catálogo de proveedores (A5), con revisión humana. Opcionalmente un modelo propone, nunca publica.
13. **Plataforma.** Funciones serverless (código que corre por evento sin administrar servidores), base de datos relacional administrada, cola y programador de tareas administrados (para plazos de respuesta de proveedores), y un interruptor de configuración que apaga el modelo sin desplegar código.

### A2. Fronteras del modelo de IA

| Dónde participa el modelo | De qué puede ser autoridad | Qué nunca puede responder solo |
|---|---|---|
| Interpretar el texto libre del miembro en el flujo | Proponer un punto de entrada de la lista cerrada; el miembro lo confirma con un botón | Qué especialista ver fuera de la lista, diagnóstico, gravedad, cualquier recomendación clínica |
| Extraer datos logísticos del mismo texto | Ubicación, horario preferido, para quién es la cita; validados contra listas (cantones, dependientes) y confirmados | Qué proveedor elegir, precios, disponibilidad, horarios reales |
| Señal de posible alarma | Solo puede escalar: activa el mismo mensaje fijo de seguridad que las reglas | Nunca puede bajar una urgencia ni anular una alarma de las reglas; nunca dice "no es grave" |
| Limpieza de datos, fuera de línea | Proponer mapeos de especialidades y posibles duplicados; la analista aprueba cada uno | Escribir en el catálogo publicado; completar o estimar precios |
| No participa | Nada | Precios, disponibilidad, ranking, agendamiento, consentimiento, identidad, textos que lee el miembro, mensajes a proveedores |

Consecuencias que conviene decir en voz alta en la sesión:
- Precios y disponibilidad salen de la base (M2, objetivo mantenido). El modelo no los ve: no recibe la base de proveedores en el prompt.
- Lo que viaja al modelo no es anónimo. Un filtro determinista elimina los identificadores conocidos (nombre del titular y de sus dependientes registrados, teléfono, número de afiliado, correos y números de documento), pero el texto libre puede traer otros datos personales que el filtro no detecta ("a mi hija María Rodríguez le duele la muela desde que fuimos a Heredia": nombre de tercero y lugar). Por eso el contrato de subprocesador con el proveedor del modelo (sin retención de datos y sin uso para entrenamiento) es condición obligatoria para encender el modelo, y el texto de consentimiento nombra al proveedor del modelo como tercero que recibe el mensaje.
- La inyección de instrucciones (un usuario que intenta que el modelo diga otra cosa) tiene impacto acotado: lo peor que puede salir es un punto de entrada equivocado de la lista, que el miembro ve y debe confirmar.
- Tipo de modelo necesario: modelo de lenguaje pequeño y rápido, bueno en español coloquial de Costa Rica, con salida estructurada (respuesta forzada a un esquema con valores permitidos), versión fijable, sin retención de datos y sin entrenamiento con ellos. No hace falta "el mejor modelo" (M2): la tarea es clasificar en una lista cerrada. Proveedor y modelo concretos: F3.
- Por qué un modelo general y no un clasificador entrenado: no hay ingenieros de ML ni datos etiquetados (§05); un modelo general con ejemplos en el prompt funciona sin entrenar.

### A3. Parte clínica de M1 sin triaje por modelo

Qué se le dice al CEO: el sistema no dice "qué especialista ver" a partir de síntomas. Dice "por dónde empezar" dentro de una lista que firmó el consejo médico, y para lo grave dice "a emergencias" o "habla con un clínico".

- **Lista cerrada de puntos de entrada.** Basada en los servicios de §01: medicina general, especialistas, laboratorios, imágenes, odontología, nutrición, psicología. El consejo médico define qué especialidades admiten acceso directo y cuáles pasan por medicina general. La lista concreta no la decide ingeniería.
- **Tabla "necesidad a punto de entrada".** Necesidades descritas en lenguaje de miembro (zona del cuerpo, tipo de servicio, "necesito un examen", "quiero hablar con alguien") a un punto de entrada. Es la que usa el menú (B) y la que el modelo debe respetar (A). Para lo ambiguo sin alarma, el valor por defecto es medicina general.
- **Reglas de alarma deterministas, en dos niveles.**
  - Emergencia: mensaje fijo que indica acudir a emergencias o llamar al 911 (número de emergencias de Costa Rica; dato confirmado por Enrique, fuera del brief). El texto final del mensaje lo aprueba el consejo médico. No se ofrece proveedor ni telemedicina (telemedicina es orientación, §01).
  - Atención pronta sin emergencia (según defina el consejo): oferta de telemedicina.
- **Telemedicina como destino caro, no como comodín.** Cuesta ~$9,40 por consulta contra ~$1,85 de un contacto de soporte (§03): $9,40 / $1,85 = ~5 veces. Capacidad libre estimada: 3.200 - 2.400 = ~800 consultas al mes (§03, estimado de operaciones). Se deriva solo si (a) lo marca una regla del consejo, (b) el miembro pide explícitamente orientación clínica, o (c) hay contenido clínico que ni el modelo ni el menú pudieron ubicar. La ambigüedad logística va a soporte humano, no a telemedicina.
- **Asimetría:** reglas y modelo solo pueden subir el nivel de atención, nunca bajarlo. Un falso positivo cuesta una consulta de telemedicina o un mensaje de emergencia innecesario; un falso negativo puede costar una vida.
- **Ritmo del consejo.** Se reúne una vez al mes (§05). En 8 semanas (M3) caben como máximo 2 reuniones (8 semanas / ~4,3 semanas por mes = ~1,9). La lista y las reglas del piloto deben estar listas para la primera. Es ruta crítica para F3.

### A4. "Agendar en el mismo flujo" con 41% de disponibilidad estructurada

Solo el 41% de proveedores tiene disponibilidad estructurada (§03) y no se les puede obligar (§05). El 59% restante (100 - 41) no admite reserva inmediata. Tres niveles, en el mismo chat:

| Nivel | Cuándo | Qué ve el miembro |
|---|---|---|
| 1. Reserva directa | Sede con disponibilidad estructurada | Horarios reales de la base; reserva con un botón, usando el motor de reservas de la app actual (la app ya tiene reservas, §01; falta confirmar que use la disponibilidad del 41%) |
| 2. Solicitud de cita | Sede sin disponibilidad, con WhatsApp o teléfono verificado | "Pedimos la cita por ti". Salud360 envía al proveedor un mensaje de plantilla de WhatsApp con botones (confirmar horario, proponer otro, no puedo). El miembro recibe la confirmación en el mismo chat. Si no hay respuesta en el plazo, se ofrece la siguiente sede |
| 3. Contacto asistido | Sin respuesta o sin canal del proveedor | Teléfono y precio de la sede, más botón para pasar a soporte humano con el contexto ya armado |

- El nivel 2 no es gratis: cada solicitud al proveedor es un mensaje iniciado por Salud360 con una plantilla de WhatsApp, y Meta cobra esos mensajes. Desde el 1 de octubre de 2026 Meta cobra todo mensaje que envía Salud360, dentro o fuera de la ventana de atención de 24 horas (periodo después del último mensaje del usuario en que la empresa puede responder sin plantilla), así que se cobran tanto la solicitud al proveedor como la confirmación al miembro (contexto/04). La ventana solo determina si hace falta usar una plantilla aprobada. Su costo se cuantifica en la Fase 3 (D4).

- El proveedor no adopta software: responde un WhatsApp, que ya usa. Facilitar, no obligar (§05).
- Incentivo: en el ranking, las sedes que confirman rápido o publican disponibilidad suben. El orden es: disponibilidad estructurada o tasa de confirmación alta, luego precio completo, luego cercanía. Es el incentivo más barato disponible: más miembros.
- Opcional: enlace web simple para que el proveedor publique sus horarios sin instalar nada.
- Honestidad para el CEO: "en el mismo flujo" es literal solo en el nivel 1. En el nivel 2 la solicitud es inmediata y la confirmación llega después.

### A5. Limpieza de datos de proveedores (fuera del flujo del miembro)

Es la prioridad 1 de F1 (sección B). Lo hace la analista con apoyo de ingeniería, en lotes.

- **214 nombres de especialidades (§03).** Taxonomía canónica corta. Primero reglas simples (minúsculas, tildes, abreviaturas, similitud de texto). Lo que quede, un modelo puede proponer el mapeo fuera de línea y la analista aprueba cada fila. 214 filas es un volumen que una persona revisa completo; el modelo solo acelera. Tabla de mapeo persistente: toda escritura nueva no reconocida va a una cola de revisión.
- **Sedes duplicadas.** El 18% comparte teléfono con otra sede (§03). Regla: mismo teléfono y nombre o dirección parecidos genera candidato a duplicado; decide un humano. No se fusiona automático: una central telefónica compartida es legítima.
- **Precios faltantes.** El 63% tiene lista completa (§03); el 37% (100 - 63) no. Nunca se estima ni se infiere un precio. La sede sin precio para el servicio buscado se muestra con "precio por confirmar" y baja en el ranking. Campaña de completitud: mensaje al proveedor con su lista actual para confirmar o completar.
- **Proveedores activos (500 vs 748, §03).** Bandera de activo verificada; solo sedes activas entran al copiloto.
- **Bandera "publicable en copiloto".** Una sede entra al flujo solo si tiene especialidad canónica, está activa, tiene teléfono verificado y precio para el punto de entrada del piloto. El piloto (M3) se limita a lo que ya esté limpio.
- La limpieza también mejora el directorio público y la app, con o sin IA.

### A6. Datos de salud y Ley 8968

Forma de la restricción (§05): consentimiento expreso e informado, y Salud360 responde por cada subprocesador. La letra la valida el abogado.

- **Dónde se pide el consentimiento.** En el primer contacto por WhatsApp (y en la app), antes de aceptar texto libre. Mensaje corto con: qué se procesa, para qué, qué terceros lo ven (Meta, proveedor del modelo), cuánto se guarda y cómo revocarlo. Botones "Acepto" / "No acepto". Se guarda versión del texto, fecha y número. Comando para revocar en cualquier momento.
- **Si no acepta.** Enlace al directorio público y teléfono de soporte. No se procesa dato de salud en el chat.
- **Qué se guarda.**
  - Sí: consentimiento, punto de entrada confirmado, sede elegida, estado de la cita (como el historial de consultas que la app ya guarda, §01).
  - Temporal: el texto libre del miembro, solo mientras dura la conversación; se borra al cerrarla.
  - Para medir calidad (D5): salida del modelo, si el miembro confirmó o corrigió y si disparó alarma. Sin texto crudo, salvo una muestra con consentimiento adicional (pendiente con el abogado).
  - Nunca: texto de mensajes en los registros técnicos (logs). Se filtra en el código.
- **Qué viaja a cada subprocesador.**
  - Meta: todo lo que el miembro escribe por WhatsApp; es inevitable si se acepta M5. Mitigación: botones en vez de texto, no pedir más detalle clínico del necesario y ofrecer el mismo flujo en la app a quien no quiera usar WhatsApp.
  - Proveedor del modelo: solo el texto del mensaje. Antes de enviarlo, un filtro determinista elimina los identificadores conocidos (nombre del titular y de sus dependientes registrados, teléfono, número de afiliado, correos y números de documento). El texto libre puede contener otros datos personales que el filtro no detecta (nombres de terceros, lugares). Por eso el contrato de subprocesador (sin retención de datos y sin uso para entrenamiento) es condición obligatoria para encender el modelo, y el texto de consentimiento nombra al proveedor del modelo como tercero que recibe el mensaje. La base de proveedores no viaja (contra M2).
  - Proveedor de la cita (nivel 2): nombre del miembro, servicio y horario. Nunca los síntomas.
  - Telemedicina: el contexto solo si el miembro lo autoriza en el traspaso.

### A7. Decisiones

| Decisión | Alternativa descartada | Razón |
|---|---|---|
| Flujo determinista (máquina de estados) con el modelo como pieza opcional | Agente de IA que conduce la conversación | Un agente libre no se puede acotar ni probar con datos de salud y sin equipo de ML (§05) |
| El modelo solo clasifica en una lista cerrada | El modelo recomienda especialista según síntomas (M1 literal) | Es triaje, un acto clínico, sin médico en planta (§05) |
| Todo texto al miembro es plantilla aprobada | Respuestas redactadas por el modelo | Elimina alucinaciones en lo que el miembro lee y simplifica la revisión legal |
| Precios y disponibilidad por consulta SQL | Base entera en el prompt (M2) | La base está mal en origen; el prompt no la arregla, cuesta en cada mensaje y la envía a un tercero |
| Modelo pequeño con salida estructurada | "El mejor modelo disponible" (M2) | Clasificar en una lista no requiere el modelo más caro (costo en F3) |
| Modelo general con ejemplos | Clasificador entrenado propio | No hay ingenieros de ML ni datos etiquetados (§05) |
| Reglas de alarma antes del modelo, y el modelo solo escala | Que el modelo evalúe urgencia | La seguridad no puede depender de una pieza probabilística que cambia de versión |
| Valor por defecto: medicina general; telemedicina solo por regla | Telemedicina ante cualquier duda | Telemedicina cuesta ~5 veces un contacto de soporte y hay ~800 consultas libres (§03) |
| Agendamiento en tres niveles con solicitud por WhatsApp al proveedor | Integrar agendas de proveedores u obligarlos a un sistema | No se les puede obligar (§05); un WhatsApp con botones no exige adopción, con costo por mensaje que se calcula en D4 |
| Ranking que premia disponibilidad y confirmación | Orden alfabético o por cercanía | Es el incentivo que Salud360 sí controla (§05) |
| Limpieza fuera de línea con aprobación humana | Normalizar con el modelo en tiempo real | Los errores del modelo quedarían frente al miembro sin revisión |
| Solo sedes "publicables" en el copiloto | Mostrar todo el catálogo | Mejor pocas sedes correctas que muchas con precios faltantes (63% completas, §03) |
| Consentimiento antes de cualquier texto libre | Consentimiento en términos generales de la app | Ley 8968 exige consentimiento expreso e informado para datos de salud (§05) |
| Texto libre se borra al cerrar la conversación | Guardar conversaciones completas | Menos dato sensible guardado, menos riesgo frente a PRODHAB |
| Servicios administrados (serverless, base administrada, cola) | Servidores o clúster propios | Sin SRE de guardia y los mismos 4 ingenieros mantienen la app (§05) |
| Interruptor que apaga el modelo y deja el menú | Flujo que depende del modelo | Si el modelo cambia de versión o falla, el servicio sigue (D5) |
| Un backend para WhatsApp y app | Dos productos separados | M1 pide app, M5 pide WhatsApp; menos de 4 ingenieros no mantienen dos |
| Lanzar B para todo el tráfico y A para el 20% del texto libre, con criterio de decisión previo | Lanzar solo con IA o solo sin IA | Se decide con datos de producción y no con opinión; el modelo es apagable |

### A8. Operable por menos de 4 ingenieros

- Piezas propias: orquestador, búsqueda, agendamiento, back office. Todo es código web convencional y SQL; nada requiere ML.
- Contenido clínico y plantillas como datos editables con aprobación, no como código: el consejo y la analista cambian contenido sin desplegar.
- Sin infraestructura de modelos: el modelo es una llamada a un servicio administrado, con versión fijada.
- Alertas mínimas: tasa de "no sé" del modelo, tasa de alarmas, solicitudes sin respuesta de proveedores, errores del webhook. Detalle en F4 (D5).

---

## B. Versión sin IA (para D6)

### B1. Qué es

El mismo sistema de A con el interruptor del modelo apagado. Nada más se pierde.

- **WhatsApp con menús.** "¿Qué necesitas?" con lista nativa: dolor o molestia (zona del cuerpo), dientes, ojos, salud mental, nutrición, exámenes con orden médica, chequeo general, "no sé". Dos o tres toques llevan al punto de entrada de la misma tabla del consejo.
- **Alarmas con botones.** Pregunta de chequeo fija ("¿Tienes alguno de estos?") con las señales del consejo. Las palabras clave también se aplican a cualquier texto que escriba el miembro.
- **Texto libre sin modelo.** Diccionario de sinónimos mantenido por la analista ("hombro", "espalda", "muela", "ansiedad") que mapea palabras a la tabla. Se alimenta de lo que los miembros escriben y no se reconoce.
- **Mismo motor:** limpieza de datos, búsqueda y ranking, agendamiento en tres niveles, traspaso a humano con contexto.
- **Directorio y app mejorados:** búsqueda por necesidad, orden por disponibilidad y precio, sello "precio confirmado". Esto llega también al público (§01).

### B2. Comparación honesta con A

Qué gana A:
- Entiende mensajes escritos como la gente escribe: errores, regionalismos, varias cosas en un mensaje, descripciones largas. En WhatsApp mucha gente escribe en vez de tocar botones (supuesto a medir).
- Menos pasos para quien escribe bien su necesidad; menos abandono en menús profundos.
- Puede detectar formas de pedir ayuda urgente que no están en la lista de palabras (solo para escalar).

Qué no gana A:
- No arregla los datos, que son la causa principal (F1, sección B). Ambas versiones dependen de la misma limpieza.
- No aumenta el 41% de disponibilidad ni hace que los proveedores contesten.
- Su ventaja está acotada por diseño: el modelo solo elige dentro de la misma lista que el menú ya ofrece. A mejora la entrada al embudo, no el resto.
- El costo del modelo es despreciable frente al del canal (F3); las desventajas reales son un subprocesador más con datos de salud, más texto en el consentimiento y la carga de evaluar y vigilar las versiones del modelo (D5).

Cuándo convendría quedarse con B:
- Si el piloto muestra que la mayoría usa botones o que la tasa de reconocimiento del diccionario es alta.
- Si el abogado no acepta enviar texto libre de salud al proveedor del modelo.
- Si el equipo no puede sostener el conjunto de evaluación y la vigilancia de versiones.
- Si en el experimento A no mejora la conversión a cita frente a B.

Lectura: en las 8 semanas se lanza B como base para todo el tráfico. Desde el primer día en producción, A atiende al 20% de las conversaciones con texto libre, como experimento controlado: ambas versiones se miden una contra otra en producción. El modelo solo se enciende si antes pasa una prueba con un conjunto de casos (detalle en la Fase 4, D5). Criterio fijado de antemano: si en 4 semanas A mejora la conversión a cita sin aumentar las alarmas mal resueltas, sube al 100%; si no, se apaga. Los umbrales concretos se definen en la Fase 4.

---

## C. Pendientes para validar con Enrique

Supuestos nuevos (también en `contexto/03-plan-y-estado.md`):
1. La base de miembros tiene el número de WhatsApp de cada miembro y de sus dependientes, o al menos del titular.
2. La consulta presencial la paga el miembro al proveedor y no cuesta a Salud360. Por eso medicina general es el valor por defecto y no telemedicina.
3. Las sedes tienen dirección suficiente para filtrar por cantón. No se asume georreferencia exacta.

Respaldado por el brief:
4. La app ya tiene reservas (§01). Falta confirmar si usa la disponibilidad estructurada del 41%: ver duda sobre qué significa disponibilidad estructurada.
5. Soporte ya atiende por WhatsApp (§01). Falta confirmar que su herramienta permita recibir conversaciones traspasadas con contexto.

Dudas:
6. ¿Qué significa "disponibilidad estructurada" en el 41%? ¿Agenda real reservable o solo horario de atención? Cambia el alcance del nivel 1.
7. ¿Los proveedores tienen WhatsApp y aceptarían recibir solicitudes? ¿Qué plazo de respuesta es razonable? Define el nivel 2.
8. ¿El consejo médico puede aprobar la lista y las reglas en su próxima reunión? Con ~1,9 reuniones en 8 semanas es ruta crítica.
9. ¿Telemedicina atiende casos de "atención pronta" o solo orientación? ¿Cómo se agenda hoy?
10. Para el abogado: ¿la elección de un punto de entrada ya es dato de salud? ¿El consentimiento por botón de WhatsApp es "expreso"? ¿Se puede guardar una muestra de texto para evaluación? ¿El filtro de identificadores conocidos más el contrato de subprocesador es suficiente bajo la Ley 8968?
11. ¿Conviene el mismo número de WhatsApp de soporte o uno nuevo? Afecta traspaso y percepción.
