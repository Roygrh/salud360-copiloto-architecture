# F3: Plan de 8 semanas (insumo para D3) y economía unitaria (insumo para D4)

Resultado interno. Coherente con F1 (sección C, mandato) y F2 (lanzamiento: versión sin IA, B, para todo el tráfico; modelo, A, para el 20% de las conversaciones con texto libre, solo si pasa la prueba con conjunto de casos y tras 5 días hábiles en modo sombra; en el piloto se valida seguridad y calidad, y la decisión A frente a B se toma con volumen de régimen, F4 A5). Precios: únicamente `contexto/04-precios-referencia.md`. Moneda: USD. Redondeo: costos por conversación a 4 decimales, montos mensuales a 2 decimales, porcentajes a 1 o 2 decimales; cada operación usa el valor ya redondeado del paso anterior.

---

# PARTE A. LAS 8 SEMANAS (D3)

## A1. Capacidad real del equipo

- **SUPUESTO: 2 ingenieros equivalentes a tiempo completo** (4 ingenieros × 50%). Razón: los mismos 4 mantienen la app actual sin SRE de guardia ni equipo de plataforma (§05), así que la mitad de su tiempo se va en operar lo que ya existe.
- **SUPUESTO: analista a 0,5 tiempo completo.** El brief solo dice "tiempo parcial" (§05); 0,5 es el punto medio.
- Presupuesto en 8 semanas: 2 × 8 = **16 semanas-ingeniero** y 0,5 × 8 = **4 semanas-analista** (unas 160 horas si la semana es de 40 horas, supuesto).

Reparto de esfuerzo (SUPUESTO, estimación propia, a validar con el equipo):

| Pieza | Semanas-ingeniero |
|---|---|
| Canal WhatsApp (webhook, envío, plantillas), identidad y consentimiento | 2 |
| Orquestador (máquina de estados), menú, diccionario de sinónimos, reglas de alarma | 3 |
| Búsqueda y ranking SQL, bandera "publicable" | 1 |
| Agendamiento: nivel 1 (1), nivel 2 con cola de plazos (2), nivel 3 traspaso a soporte (1) | 4 |
| Pieza del modelo: filtro de identificadores, intérprete, validador, interruptor, asignación al 20%, conjunto de casos | 2 |
| Apoyo a la limpieza de datos (scripts de normalización y candidatos a duplicado) | 1 |
| Pruebas de punta a punta, métricas mínimas (F2 A8), lanzamiento | 1 |
| **Subtotal** | **14** |
| Reserva para imprevistos: 16 - 14 = 2 (2 / 16 = 12,5%). La consumen casi por completo las extensiones de la pieza del modelo definidas en F4 (corrida diaria, modo sombra, apagado automático, métricas por grupo) | 2 |

Lectura: el plan cabe, pero casi sin holgura: la reserva queda tomada por la pieza del modelo. Cualquier pieza nueva desplaza otra; por eso A5 es largo y, ante cualquier retraso, lo primero que se corta es A (A5).

## A2. Plan semana a semana

Frentes en paralelo. "Hito" marca una dependencia que bloquea a otros frentes.

| Sem. | Datos (analista + ing.) | Consejo médico (ruta crítica) | Meta / WhatsApp (riesgo de tercero) | Legal (abogado) | Ingeniería versión B | Agendamiento | Pieza del modelo |
|---|---|---|---|---|---|---|---|
| 1 | Definir zona del piloto (A4). Taxonomía canónica de especialidades; reglas simples sobre los 214 nombres (§03) | Ingeniería y analista redactan el borrador: lista cerrada, tabla "necesidad a punto de entrada", reglas de alarma, texto de emergencia. Pedir fecha de la reunión 1 | Alta de la cuenta de WhatsApp Business Platform y verificación del negocio. Política de Meta para proveedores de IA: resuelta, el copiloto la cumple (`04`, Parte C) | Encargo: texto de consentimiento, contrato de subprocesador con el proveedor del modelo, revisión de Meta como subprocesador | Webhook, identidad (cruce con base de miembros), estructura del orquestador | Confirmar si las reservas de la app usan la disponibilidad del 41% (§03, duda de F2) | Definir formato del conjunto de casos |
| 2 | Duplicados por teléfono compartido (18%, §03) y bandera de activo, solo en la zona | Enviar borrador al consejo para lectura previa | Enviar plantillas a aprobación de Meta (solicitud al proveedor, confirmación de cita fuera de ventana) | Borrador de consentimiento | Consentimiento por botón, menú, diccionario | Nivel 1 sobre el motor de reservas de la app | Conjunto de casos v1: frases redactadas por agentes de soporte a partir de su experiencia (sin texto real de miembros) |
| 3 | Precios del punto de entrada en la zona: llamar o escribir a las sedes con lista incompleta (37%, §03). En las semanas 3-5 se registra quién responde y en cuánto tiempo (prueba de vida para el nivel 2, F2 A5; F4 B2) | **Reunión 1: aprueba lista cerrada, tabla, reglas de alarma y textos** (hito) | Seguimiento de plantillas | | Cargar catálogo aprobado; reglas de alarma; búsqueda y ranking | Nivel 1 terminado | Filtro de identificadores, intérprete, validador |
| 4 | Primer corte de sedes publicables | | **Plantillas aprobadas** (hito; si se rechazan, reenviar) | **Consentimiento final y contrato de subprocesador firmado** (hito para producción y para encender el modelo) | Flujo B de punta a punta en ambiente de prueba | Nivel 2: plantilla al proveedor, plazo de respuesta, siguiente sede | Prueba v1 con el conjunto de casos |
| 5 | Completar precios faltantes en la zona. Semanas 5-7: soporte etiqueta el motivo de cada contacto y la cuenta corporativa, para tener la línea base de "¿a dónde voy?" antes del piloto (F4 A4) | Consejo revisa por escrito los casos dudosos de la prueba (SUPUESTO: acepta revisión asíncrona) | | | Integración con el catálogo publicable | Nivel 3: traspaso a soporte con contexto | Ajuste de instrucciones y ejemplos; prueba v2 |
| 6 | **Corte final de sedes publicables** (hito; se congela la lista) | | | | Pruebas internas con cuentas de prueba | Ensayo con 2-3 proveedores reales que acepten participar (SUPUESTO) | **Prueba final contra umbral (F4 A2)**: decide si A entra en la semana 8. Sombra interna sobre las pruebas internas (F4 A3) |
| 7 | Revisión de lo que los evaluadores escribieron y no se reconoció (alimenta diccionario) | **Reunión 2: ajustes** a alarmas y tabla según pruebas (hito) | | | Aplicar ajustes del consejo (son datos, no código: F2 A8) | Ensayo de la demo con el proveedor de la demo | Volver a correr la prueba con el catálogo ajustado. Sigue la sombra interna (F4 A3) |
| 8 | Monitoreo de "precio por confirmar" y sedes que no responden | | | | **Producción** para el alcance de A4. Demo del CEO (A6) | En producción | Si pasó la prueba: A al 20% del texto libre en modo sombra los primeros 5 días hábiles y visible después (F4 A3). Si no pasó o hay retraso: apagado |

Supuesto de calendario: la reunión 1 cae en la semana 3 y la reunión 2 en la semana 7 (separación de ~4 semanas, una por mes, §05). Si la próxima reunión del consejo cae antes de la semana 3, no hay tiempo para un borrador serio; si cae después de la semana 4, se activa A3.

Dependencias principales:
- Reunión 1 → catálogo clínico → reglas de alarma, contenido del menú, lista cerrada del modelo, etiquetas finales del conjunto de casos.
- Limpieza de datos → sedes publicables → búsqueda → todo lo que el miembro ve, incluida la demo.
- Cuenta de WhatsApp → todo el canal (M5). Plantillas aprobadas → nivel 2.
- Consentimiento final → cualquier conversación en producción. Contrato de subprocesador + prueba aprobada → encender el modelo.
- Confirmación del motor de reservas de la app → alcance real del nivel 1.

Regla de retraso: si cualquier frente se atrasa, lo primero que se corta es A (el modelo). B sale igual en la semana 8 porque no depende del modelo: el interruptor existe precisamente para esto.

Riesgo de Meta: la cuenta y las plantillas dependen de un tercero con plazos que no controlamos. Mitigación: empezar el día 1. Si las plantillas no están aprobadas en la semana 6, el nivel 2 no sale y esas sedes pasan al nivel 3 (contacto asistido). Si la cuenta no está lista, no hay respaldo barato en 8 semanas (el canal de la app se corta, A5): es el riesgo de plazo sin plan B, por eso se escala desde la semana 1.

## A3. Contingencia de la ruta crítica (el consejo no aprueba a tiempo)

Primera mitigación: pedir al consejo una sesión extraordinaria o revisión por escrito (SUPUESTO: el brief solo dice que se reúne una vez al mes, §05; no dice si acepta otra forma).

Si aun así no hay aprobación en la semana 4, se lanza un alcance reducido:
- **Puntos de entrada que no requieren juicio clínico**, porque el miembro ya sabe qué necesita o alguien ya decidió por él: odontología, laboratorio con orden médica, imágenes con orden médica, nutrición. Medicina general como servicio elegido directamente por el miembro (como en el directorio), no como resultado de interpretar síntomas.
- **Solo botones (B), sin texto libre y sin modelo.** Sin catálogo de alarmas aprobado no se puede interpretar lo que el miembro escribe.
- **Aviso fijo de emergencias en cada pantalla** ("si es una emergencia, llama al 911"), revisado por el abogado.

Evaluación de viabilidad con el brief:
- Viable técnicamente: usa las mismas piezas de B y no contradice §05 (no hay triaje: el miembro elige un servicio).
- Pierde el centro de M1: "describo lo que me pasa y me dicen por dónde empezar". El caso del hombro (§02) no sale en producción.
- No elimina del todo la dependencia clínica: el texto de emergencias debería aprobarlo el consejo (F2 A3). Con el aviso genérico revisado por el abogado se reduce, no se elimina. A decidir con Enrique.
- La demo cambia: se muestra un caso de odontología o laboratorio en producción, y el caso del hombro como "pendiente de aprobación del consejo en su reunión de [fecha]". No se muestra en vivo algo que no está aprobado.

## A4. Alcance del piloto (semana 8)

| Dimensión | Entra | Razón |
|---|---|---|
| Miembros | Empleados de las tres cuentas corporativas más grandes (M3). El resto de miembros sigue como hoy | Son la audiencia del día de la presentación (M3); el problema de negocio es la renovación corporativa (§02, 71% en cuentas pequeñas, §03). Controla volumen y riesgo. SUPUESTO: la base de miembros identifica la cuenta corporativa de cada miembro |
| Zona | Sedes de los cantones donde viven o trabajan esos empleados (dato a pedir al cliente) | La analista a 0,5 (A1) no limpia 1.140 sedes (§03) en 8 semanas: 160 horas / 1.140 sedes = ~8,4 minutos por sede, sin contar llamadas para confirmar precios. Limitar zona hace la limpieza posible |
| Sedes | Solo las "publicables" (F2 A5): especialidad canónica, activa, teléfono verificado y precio del punto de entrada | Mejor pocas sedes correctas que muchas con precios faltantes (63% completas, §03) |
| Puntos de entrada | Medicina general (valor por defecto), odontología, laboratorio con orden médica, imágenes con orden médica, nutrición. Especialidades de acceso directo solo si las aprueba la reunión 1 | Son los de §01 con menor riesgo clínico; la lista final la decide el consejo, no ingeniería (F2 A3) |
| Alarmas | Las dos categorías de F2 A3 (emergencia y atención pronta), para cualquier texto, incluida la crisis de salud mental | La alarma debe funcionar aunque el punto de entrada no esté en el piloto |
| Canal | Solo WhatsApp (M5) | Es lo que pide M5 y lo que se demuestra. La app comparte backend y entra después (A5) |
| Agendamiento | Niveles 1, 2 y 3 | Sin los tres no hay "agenda en el mismo flujo" defendible (F2 A4) |
| Modelo | A al 20% del texto libre, solo si pasó la prueba de la semana 6 | Decisión de F2 |

SUPUESTO: el número de empleados de las tres cuentas no está en el brief; define el volumen del piloto y debe pedirse. La economía de la parte B se calcula para el despliegue completo (38.000 miembros), no para el piloto.

## A5. Lo que se corta (no entra en las 8 semanas)

| Se corta | Razón |
|---|---|
| Copiloto conversacional dentro de la app | Exige interfaz nueva y publicación en tiendas; no cabe en 2 ingenieros equivalentes. Va primero en las semanas 9-12: mismo backend y sin costo de Meta (B3) |
| Psicología y salud mental como punto de entrada | Requiere un protocolo de crisis del consejo. La regla de alarma de crisis sí está activa |
| Especialidades de acceso directo no aprobadas | Decisión clínica del consejo (§05), no de ingeniería |
| Sedes fuera de la zona o no publicables | Limpieza imposible en 8 semanas a 0,5 analista (A4) |
| Miembros fuera de las tres cuentas | Volumen y riesgo; se abre en régimen (desde las semanas 9-12) tras validar seguridad y calidad en el piloto (F4 A5) |
| Agendar para dependientes | Consentimiento sobre datos de terceros, incluidos menores: requiere al abogado. F2 A1 lo prevé; se pospone |
| Modelo al 100% | Se decide con volumen de régimen (F2 B2, F4 A5); en el piloto A solo se valida en seguridad y calidad |
| Pieza del modelo (A), si hay retraso | Es lo primero que se corta: B sale igual en la semana 8 porque no depende del modelo. El interruptor existe precisamente para esto |
| Modelo para limpieza fuera de línea | 214 nombres (§03) se revisan a mano con reglas; evita otro flujo de datos hacia un subprocesador |
| Integración de agendas de proveedores y enlace web de horarios | No se les puede obligar (§05); adopción incierta |
| Recordatorios de cita, encuestas y mensajes proactivos | Cada mensaje cuesta USD 0,0113 o más (`04`) y no son necesarios para el valor central |
| Muestra de texto crudo para evaluar el modelo | Pendiente del abogado (F2 A6) |
| Agendamiento integrado de telemedicina | Se deriva por el canal actual; integrarlo no cambia el resultado del piloto |
| Panel de métricas completo | Solo las alertas mínimas de F2 A8 y las métricas de la validación del piloto (F4 A5) |
| Atender no miembros por el copiloto | Reciben el enlace al directorio público (F2 A1) |

## A6. Qué demuestra el CEO el día de la presentación (M3)

Guion (en producción, con una cuenta de prueba marcada como grupo A; nunca con datos de un miembro real). El día de la demo, para los miembros reales A está todavía en modo sombra (primeros 5 días hábiles, F4 A3); solo la cuenta de prueba lo ve activo:

1. **Primer contacto.** Desde el teléfono de la cuenta de prueba escribe al número de Salud360. Aparece el consentimiento con botones. Toca "Acepto". Mensaje para la audiencia: cumplimos la Ley 8968 antes de leer una palabra de salud (§05).
2. **Necesidad común (§02).** Escribe: "Me duele el hombro desde hace 3 semanas, ¿a dónde voy?". Las reglas de alarma no disparan. El sistema propone "Medicina general" (o la especialidad que haya habilitado el consejo) y pregunta con botones si es correcto. Toca "Sí".
3. **Ubicación y opciones.** Elige su cantón. Recibe una lista con 3 sedes publicables, cada una con precio fijo de la base y la marca "reserva inmediata" o "pedimos la cita por ti".
4. **Cita.** Elige una sede de nivel 1 y reserva un horario real (sede coordinada de antemano, SUPUESTO). Como respaldo, muestra una de nivel 2: la solicitud sale al proveedor de la demo, que confirma con un botón en su WhatsApp, y la confirmación llega al chat.
5. **Señal de alarma.** En una conversación nueva escribe: "Me duele el pecho y me cuesta respirar". Recibe el mensaje fijo de emergencias aprobado por el consejo, sin proveedor ni cita. Mensaje: el sistema no hace triaje ni opina; ante la señal, deriva.
6. **Interruptor.** Apaga el modelo en vivo desde la configuración (sin desplegar código). Repite el paso 2 con el mismo texto o con el menú: llega a la misma sede con el mismo precio. Mensaje: el producto no depende de la IA; la IA solo acorta el camino.
7. **Cierre con números:** costo por contacto de soporte evitado, unos USD 1,08 en el escenario base en régimen (B5), frente a USD 1,85 por contacto de soporte (§03). Una conversación del copiloto no equivale a un contacto evitado.

Datos reales que el CEO debe tener listos:
- Número de sedes publicables en la zona y cuántas tienen reserva inmediata (nivel 1).
- Puntos de entrada activos y fecha de aprobación del consejo.
- Resultado de la prueba del modelo (semana 6) y si A está en modo sombra o apagado para los miembros reales.
- Cuántos empleados de las tres cuentas tienen acceso al piloto.
- En régimen (38.000 miembros): costo total por conversación USD 0,1355 (B2), costo por contacto de soporte evitado USD 1,08 (B5) y costo por miembro USD 0,0415 al mes (B6), todo en escenario base.
- Del piloto: solo el costo variable por conversación, USD 0,0925 en base sin infraestructura (B2). Durante el piloto domina el costo fijo de infraestructura (Parte B, costo del piloto).
- Retorno (B8): el ahorro en soporte paga la operación del copiloto; el retorno real está en la renovación de cuentas corporativas.

Lo que NO debe prometer:
- Que el sistema dice qué especialista ver o diagnostica.
- Cobertura nacional o de todas las sedes.
- Reserva inmediata en todas las sedes (solo nivel 1).
- Ahorro en soporte: no está medido todavía.
- Que el copiloto mejora la renovación: es la hipótesis del proyecto y todavía no está medida (B8).
- Fechas de expansión no aprobadas por el consejo o el abogado.
- Que la IA "entiende todo": la IA es opcional y apagable.
- Que A está activo para todos los miembros desde el lanzamiento: arranca en modo sombra (F4 A3).
- Una fecha de decisión sobre la IA: se decide con volumen de régimen (F4 A5).

---

# PARTE B. ECONOMÍA UNITARIA (D4)

**Aviso: todos los cálculos de B1 a B7 corresponden al régimen**, es decir, con el copiloto abierto a los 38.000 miembros (desde las semanas 9-12). No son el costo del piloto de 8 semanas. El piloto tiene un volumen mucho menor, que no se puede calcular porque el brief no dice cuántos empleados tienen las tres cuentas corporativas (M3, A4).

**Costo del piloto.** El costo variable escala con el número de conversaciones: USD 0,0925 por conversación en el escenario base, sin infraestructura (B2). La infraestructura fija (USD 200 a 1.000 al mes, SUPUESTO de B2) no depende del volumen, así que durante el piloto es el componente dominante del costo. Costo mensual del piloto = conversaciones del piloto × 0,0925 + infraestructura fija. Falta el número de empleados de las tres cuentas (Parte C).

## B1. Línea base (lo que cuesta hoy)

- Soporte: 9.000 contactos al mes × USD 1,85 = **USD 16.650 al mes** (§03; 9.000 es el supuesto de F1).
- Por miembro: USD 16.650 / 38.000 = **USD 0,44 al mes**, es decir 0,44 / 3,10 = 14,2% del margen por miembro (§05).
- **Por qué no 11.300:** los contactos "¿a dónde voy para X?" (11.300, hoja de la analista) superan al total medido (9.000, dashboard), y un subconjunto no puede ser mayor que el total (F1 A2). Usar 11.300 inflaría el ahorro con una cifra que no se sostiene. Consecuencia: no sabemos qué parte de los 9.000 es "¿a dónde voy?"; se trata como supuesto en B5.
- Telemedicina como referencia: USD 9,40 por consulta (§03), unas 5 veces un contacto de soporte (9,40 / 1,85 = 5,1). Cada derivación a telemedicina pesa en el resultado (B7).

## B2. Costo de una conversación del copiloto

Supuestos de conversación (canal WhatsApp; la app no tiene costo de Meta, `04`):
- Según `04`, desde octubre de 2026 Meta cobra cada mensaje que Salud360 envía, dentro o fuera de la ventana de 24 horas, a USD 0,0113 (servicio y utilidad). Los mensajes del miembro no se cobran.
- SUPUESTO: todos los miembros que conversan están en WhatsApp (cota alta de costo).

**1. Mensajes salientes al miembro** (SUPUESTO de conteo):

| Escenario | Mensajes | Detalle | Costo |
|---|---|---|---|
| Mínimo | 5 | Necesidad, chequeo de alarma, ubicación, sedes con horarios, confirmación (consentimiento ya dado en una conversación anterior) | 5 × 0,0113 = 0,0565 |
| Base | 7 | Consentimiento, necesidad o confirmación del punto de entrada, chequeo de alarma, ubicación, sedes, horarios, confirmación | 7 × 0,0113 = 0,0791 |
| Máximo | 10 | Base + una aclaración + aviso "pedimos la cita por ti" + segunda ronda de sedes porque el proveedor no respondió | 10 × 0,0113 = 0,1130 |

**2. Nivel 2: mensajes al proveedor.** La solicitud es una plantilla de utilidad (SUPUESTO: Meta la clasifica como utilidad y no como marketing; ver B7); la respuesta del proveedor es gratis; si propone otro horario, la respuesta de Salud360 es otro mensaje cobrado.
- Fracción de conversaciones que llegan al nivel 2: SUPUESTO 59% = 100% - 41% de proveedores con disponibilidad estructurada (§03). Es conservador: el ranking pone primero a las sedes con disponibilidad (F2 A4), lo que debería bajar esa fracción.

| Escenario | Mensajes al proveedor por conversación de nivel 2 | Costo por conversación promedio |
|---|---|---|
| Mínimo | 1 solicitud × 1 mensaje = 1 | 0,59 × 1 × 0,0113 = 0,0067 |
| Base | 1 solicitud × 2 mensajes = 2 | 0,59 × 2 × 0,0113 = 0,0133 |
| Máximo | 2 solicitudes × 2 mensajes = 4 | 0,59 × 4 × 0,0113 = 0,0267 |

**3. Llamada al modelo** (Claude Haiku 5.5, `04`: USD 0,10 por millón de entrada, 0,50 por millón de salida). El prompt es muy menor a 100.000 tokens, así que aplica la tarifa baja. Token: unidad de texto que cobra el modelo, aproximadamente una sílaba o palabra corta.
- SUPUESTO de tamaño: entrada = instrucciones + lista cerrada + tabla de necesidades + ejemplos + texto del miembro; salida = objeto estructurado corto (punto de entrada, ubicación, horario, bandera de alarma).

| Escenario | Entrada | Salida | Llamadas | Costo por conversación con modelo |
|---|---|---|---|---|
| Mínimo | 2.000 | 50 | 1 | 2.000 × 0,10 / 10⁶ + 50 × 0,50 / 10⁶ = 0,000200 + 0,000025 = 0,000225 |
| Base | 4.000 | 100 | 1 | 0,000400 + 0,000050 = 0,000450 |
| Máximo | 8.000 | 200 | 3 (el miembro corrige y vuelve a escribir) | 3 × (0,000800 + 0,000100) = 0,002700 |

- El modelo aplica solo al 20% del texto libre (F2). SUPUESTO: todas las conversaciones tienen texto libre (cota alta). Promedio por conversación: mínimo 0,000225 × 0,20 = 0,000045; base 0,000450 × 0,20 = 0,000090; máximo 0,002700 × 0,20 = 0,000540.
- No se usa caché de prompt: su precio no está en `04`.

**4. Infraestructura** (serverless, base de datos, cola). SUPUESTO a validar con la factura real de nube: costo fijo incremental de USD 200 (mínimo), 500 (base) y 1.000 (máximo) al mes. No hay dato en el brief; el CFO revisa la factura línea por línea (§05) y esa es la fuente que debe reemplazar este rango. Por conversación, con el volumen base de B5 (11.632 conversaciones al mes): 200 / 11.632 = 0,0172; 500 / 11.632 = 0,0430; 1.000 / 11.632 = 0,0860.

**Resultado: costo por conversación**

| Componente | Mínimo | Base | Máximo |
|---|---|---|---|
| WhatsApp al miembro | 0,0565 | 0,0791 | 0,1130 |
| WhatsApp al proveedor (nivel 2) | 0,0067 | 0,0133 | 0,0267 |
| Modelo (20%) | 0,0000 (0,000045) | 0,0001 (0,000090) | 0,0005 (0,000540) |
| **Variable** | **0,0632** | **0,0925** | **0,1402** |
| Infraestructura (volumen base) | 0,0172 | 0,0430 | 0,0860 |
| **Total por conversación** | **0,0804** | **0,1355** | **0,2262** |

No incluido: horas de ingeniería (16 semanas-ingeniero, A1; el brief no da salarios), consultas de telemedicina derivadas (B7) y contactos de nivel 3 que siguen yendo a soporte (ya descontados en B5).

## B3. Hallazgo: el costo está en el canal, no en la IA

- Canal por conversación (base): 0,0791 + 0,0133 = 0,0924. Modelo por conversación (base, al 20%): 0,000090. El canal cuesta 0,0924 / 0,000090 = ~1.027 veces el modelo. Con el modelo al 100% (0,000450): 0,0924 / 0,000450 = ~205 veces.
- Un solo mensaje de WhatsApp ahorrado (0,0113) paga 0,0113 / 0,000450 = ~25 llamadas al modelo.
- La infraestructura fija (0,0430 por conversación en base) también pesa más que el modelo.

Consecuencias de diseño:
- **Cada mensaje saliente cuenta.** Agrupar contenido (chequeo de alarma junto con la pregunta de necesidad; sedes y horarios en una sola lista nativa), usar listas y botones en vez de varios mensajes, no enviar recordatorios ni encuestas en el piloto (A5).
- **La app es el canal barato:** mismo backend y sin costo de Meta. Es lo primero después de las 8 semanas (A5).
- **Argumento a favor de A que no estaba en F2:** si el modelo ahorra al menos un paso de menú por conversación, se paga solo (un mensaje evitado vale ~25 llamadas). Es hipótesis a medir en el experimento del 20%, no un hecho.
- El costo del canal no depende de la IA: Meta cobra igual el mensaje escrito por una plantilla, una persona o una IA (`04`). La versión B paga el mismo canal.

## B4. Comparación con M2 (toda la base en el prompt, mejor modelo)

SUPUESTO de tamaño: 300 tokens por sede (nombre, dirección, cantón, teléfono, especialidades, horario y una lista de precios de varios servicios; unas 200 palabras en texto). Rango: 150 a 500.
- Base en el prompt: 1.140 sedes (§03) × 300 = 342.000 tokens, más ~3.000 de instrucciones e historial (SUPUESTO) = 345.000 tokens por mensaje.
- Costo por mensaje con Claude Opus 5.5 (`04`: 4 por millón de entrada, 20 por millón de salida), con respuesta redactada de 300 tokens (SUPUESTO): 345.000 × 4 / 10⁶ + 300 × 20 / 10⁶ = 1,3800 + 0,0060 = **USD 1,386 por mensaje**. SUPUESTO: `04` no indica recargo de Opus por encima de 100.000 tokens ni el límite de contexto; si existe recargo, es peor.
- En ese diseño el modelo conduce la conversación y responde cada mensaje: 7 mensajes (el mismo conteo base de B2) × 1,386 = **USD 9,70 por conversación**.

| Comparación (base) | Costo por conversación |
|---|---|
| Modelo en el diseño de F2 (al 20%) | 0,0001 |
| Modelo en el diseño de F2 (al 100%) | 0,0005 |
| M2 con Opus 5.5 | 9,70 (~21.600 veces el diseño F2 al 100%: 9,70 / 0,00045) |
| Contacto de soporte (§03) | 1,85 |
| Consulta de telemedicina (§03) | 9,40 |

- M2 cuesta 9,70 / 1,85 = **5,2 veces un contacto de soporte** por conversación, y más que una consulta con un clínico real (9,40).
- A volumen base (11.632 conversaciones, B5): 11.632 × 9,70 = USD 112.830 al mes; por miembro 112.830 / 38.000 = USD 2,97, es decir **95,8% del margen de 3,10** (§05). Rango de tamaño: con 150 tokens por sede y 5 mensajes, 3,51 por conversación; con 500 tokens y 10 mensajes, 22,98.
- No es solo el modelo caro: el mismo método con Haiku 5.5 (tarifa de más de 100.000 tokens, `04`) cuesta 345.000 × 0,50 / 10⁶ + 300 × 2,50 / 10⁶ = 0,1725 + 0,0008 = 0,1733 por mensaje, ~385 veces la llamada del diseño F2 (0,1733 / 0,00045). El problema es el método.
- Y no cumple su objetivo: meter la base en el prompt no la vuelve actual (está mal en origen, F1 B) y envía toda la base a un tercero en cada mensaje.
- **Meta Business Agent** (`04`: ~USD 0,04 a 0,05 por mensaje): 7 × 0,04 = 0,28 a 7 × 0,05 = 0,35 por conversación, unas 600 a 780 veces el diseño F2 al 100% (0,28 / 0,00045; 0,35 / 0,00045). Se descarta por costo y porque la IA de Meta procesaría datos de salud y redactaría las respuestas, contra la regla de plantillas aprobadas (F2 A7).

## B5. Cuánto de la línea base se desplaza realmente (§06, D4), en régimen

Contactos evitados = 9.000 × (a) × (b) × (c). Todos los factores son SUPUESTO:
- (a) Parte de los 9.000 que es "¿a dónde voy para X?". El 11.300 sugiere que es el motivo dominante, pero no es usable (B1), y hay otros motivos (plan, dependientes, facturación).
- (b) Parte de esos miembros que usa el copiloto en vez de llamar. Adopción nueva en un canal nuevo; en el piloto solo tres cuentas (A4).
- (c) Parte de las conversaciones que termina sin soporte. El nivel 3 sigue yendo a soporte. Se calcula como 41% (nivel 1, §03) + 59% × tasa de confirmación del proveedor en nivel 2 (SUPUESTO: 20%, 40%, 60%).
- (d) Conversaciones necesarias por contacto evitado: la mayoría de quienes usen el copiloto no habría llamado (habría buscado en el directorio o desistido). Hoy hay 96.000 búsquedas por 9.000 contactos: 96.000 / 9.000 = 10,7 (§03), redondeado a 11 para el conservador; 8 y 6 para base y optimista (SUPUESTO).

| | Conservador | Base | Optimista |
|---|---|---|---|
| (a) "¿A dónde voy?" | 30% | 50% | 70% |
| (b) Adopción | 30% | 50% | 70% |
| (c) Resuelve sin soporte | 41% + 59% × 20% = 52,8% | 41% + 59% × 40% = 64,6% | 41% + 59% × 60% = 76,4% |
| Contactos evitados | 9.000 × 0,30 × 0,30 × 0,528 = 427,7 → **428** | 9.000 × 0,50 × 0,50 × 0,646 = 1.453,5 → **1.454** | 9.000 × 0,70 × 0,70 × 0,764 = 3.369,2 → **3.369** |
| % de la base desplazada | 428 / 9.000 = 4,8% | 1.454 / 9.000 = 16,2% | 3.369 / 9.000 = 37,4% |
| Ahorro mensual (× 1,85) | 791,80 | 2.689,90 | 6.232,65 |
| (d) Conversaciones por contacto evitado | 11 | 8 | 6 |
| Conversaciones al mes | 428 × 11 = 4.708 | 1.454 × 8 = 11.632 | 3.369 × 6 = 20.214 |
| Costo variable (× 0,0925) | 435,49 | 1.075,96 | 1.869,80 |
| Infraestructura fija (base) | 500,00 | 500,00 | 500,00 |
| **Costo mensual del copiloto** | **935,49** | **1.575,96** | **2.369,80** |
| **Neto mensual (ahorro - costo)** | **-143,69** | **+1.113,94** | **+3.862,85** |

Lecturas:
- En el conservador **el copiloto no se paga**: el costo fijo de nube (500) supera al ahorro neto del variable (791,80 - 435,49 = 356,31). Para empatar, la infraestructura debe costar menos de USD 356 al mes.
- Por contacto evitado en el base: 8 × 0,1355 = USD 1,08 frente a USD 1,85 de soporte.
- **Ahorro no es caja automática:** USD 1,85 es costo total por contacto (§03), con agentes probablemente de sueldo fijo. El ahorro se vuelve dinero solo si soporte ajusta su dotación o absorbe crecimiento sin contratar. A confirmar con el CFO.
- El valor principal del proyecto no es este ahorro sino la renovación corporativa (§02); este cálculo solo muestra que el copiloto no come margen.

## B6. Contra el margen (M4), en régimen

| | Conservador | Base | Optimista |
|---|---|---|---|
| Costo del copiloto por miembro | 935,49 / 38.000 = 0,0246 | 1.575,96 / 38.000 = 0,0415 | 2.369,80 / 38.000 = 0,0624 |
| % del margen (÷ 3,10, §05) | 0,79% | 1,34% | 2,01% |
| Neto por miembro | -143,69 / 38.000 = -0,0038 | +1.113,94 / 38.000 = +0,0293 | +3.862,85 / 38.000 = +0,1017 |

Referencias: soporte hoy cuesta 14,2% del margen (B1); M2 costaría 95,8% (B4). SUPUESTO: se usa el margen individual (3,10) para todos; el margen de planes familiares y corporativos no está en el brief (F1 A5).

Para el CFO (cifras en régimen, 38.000 miembros):
- El copiloto cuesta entre 2 y 6 centavos por miembro al mes, entre 0,8% y 2% del margen. En el escenario base ahorra unos USD 1.100 netos al mes en soporte; en el conservador pierde unos USD 140 al mes por el costo fijo de nube.
- WhatsApp es casi todo el costo variable: 0,0924 de 0,0925 (mensajes al miembro 0,0791 más mensajes al proveedor 0,0133). La línea a vigilar en la factura es Meta. La propuesta original (M2) se habría comido el 96% del margen.
- El ahorro en soporte paga la operación del copiloto; el retorno real está en no perder cuentas corporativas en la renovación (B8).

## B7. Sensibilidad (sobre el escenario base en régimen: 11.632 conversaciones, ahorro 2.689,90)

| Caso | Costo variable por conversación | Costo mensual | Neto mensual |
|---|---|---|---|
| Base | 0,0925 | 1.575,96 | +1.113,94 |
| Meta duplica la tarifa (0,0226) | 7 × 0,0226 + 0,59 × 2 × 0,0226 + 0,0001 = 0,1582 + 0,0267 + 0,0001 = 0,1850 | 11.632 × 0,1850 + 500 = 2.651,92 | +37,98 (empate) |
| Mensajes al máximo del rango | 0,1402 (B2) | 11.632 × 0,1402 + 500 = 2.130,81 | +559,09 |
| Tarifa doble y mensajes al máximo | 10 × 0,0226 + 0,59 × 4 × 0,0226 + 0,00054 = 0,2260 + 0,0533 + 0,00054 = 0,2798 | 11.632 × 0,2798 + 500 = 3.754,63 | **-1.064,73** |
| Plantilla al proveedor clasificada como marketing (0,0740) | 0,0791 + 0,59 × (0,0740 + 0,0113) + 0,0001 = 0,0791 + 0,0503 + 0,0001 = 0,1295 | 11.632 × 0,1295 + 500 = 2.006,34 | +683,56 |
| Modelo al 100% en vez de 20% | 0,0925 + (0,00045 - 0,00009) = 0,0929 | 11.632 × 0,0929 + 500 = 1.580,61 | +1.109,29 (irrelevante) |

Puntos de quiebre (donde el copiloto deja de ser más barato que el soporte que evita, escenario base):
- Costo variable máximo tolerable: (2.689,90 - 500) / 11.632 = 0,1883 por conversación.
- **Tarifa de Meta:** cada conversación base envía 7 + 0,59 × 2 = 8,18 mensajes cobrados. (0,1883 - 0,0001) / 8,18 = **USD 0,0230 por mensaje**, es decir 0,0230 / 0,0113 = **2,0 veces la tarifa actual**.
- **Mensajes al miembro** a tarifa actual: (0,1883 - 0,0133 - 0,0001) / 0,0113 = 15,5, es decir **más de 15 mensajes por conversación**.
- **Conversaciones por contacto evitado:** (2.689,90 - 500) / (1.454 × 0,0925) = 2.189,90 / 134,50 = **16,3** (hoy se supone 8).
- **Telemedicina, la variable más peligrosa:** cada derivación cuesta 9,40 (§03), lo mismo que ~69 conversaciones (9,40 / 0,1355). El neto base se agota con 1.113,94 / 9,40 = 118,5 derivaciones al mes, es decir 118,5 / 11.632 = **~1% de las conversaciones** derivadas a telemedicina que no habrían ocurrido de otra forma. Refuerza la decisión de F2: medicina general por defecto y telemedicina solo por regla.

## B8. Retorno por renovación

El ahorro neto en soporte del escenario base es pequeño: 1.113,94 × 12 = USD 13.367,28 al año (B5). El problema de negocio que plantea el brief no es el soporte sino la renovación: se pierden cuentas corporativas porque los empleados "no supieron cómo usarlo" (§02).

Datos del brief:
- Cuota corporativa: USD 10 por empleado al mes (§01).
- Renovación en cuentas de menos de 50 empleados: 71% (§03), es decir 100% - 71% = 29% no renueva.

Ejemplo (SUPUESTO de tamaño: cuenta de 30 empleados, dentro del rango de menos de 50 de §03):
- Ingreso de la cuenta: 30 × USD 10 = **USD 300 al mes**, es decir 300 × 12 = **USD 3.600 al año**.
- Cuentas de ese tamaño que hay que retener para igualar el ahorro neto en soporte del escenario base: 1.113,94 / 300 = 3,71, redondeado hacia arriba = **4 cuentas**.
- Cuentas de ese tamaño que cubren la pérdida del escenario conservador: 143,69 / 300 = 0,48, redondeado hacia arriba = **1 cuenta**.

Advertencias:
- Es ingreso, no margen. El brief no da el margen de las cuentas corporativas; solo el margen individual de USD 3,10 (§05). Comparar ingreso retenido con ahorro neto sobrestima el retorno en la proporción del costo de servir a esos empleados.
- El brief no dice cuántas cuentas corporativas hay ni cuántas se pierden al año. No se estiman aquí (pendientes en la Parte C).
- No está medido que el copiloto mejore la renovación; es la hipótesis de negocio del proyecto (§02), no un resultado (A6: no se promete).

Para el CFO: el ahorro en soporte paga la operación del copiloto. El retorno real está en no perder cuentas corporativas en la renovación: retener una sola cuenta de 30 empleados (USD 300 al mes de ingreso) ya cubre la pérdida del escenario conservador.

---

# PARTE C. PENDIENTES PARA VALIDAR CON ENRIQUE

Supuestos nuevos de F3 (también en `contexto/03-plan-y-estado.md`):
1. Capacidad: 2 ingenieros equivalentes (4 × 50%) y analista a 0,5. Reparto de 14 + 2 semanas-ingeniero (A1).
2. Calendario del consejo: reunión 1 en semana 3 y reunión 2 en semana 7; acepta revisión por escrito entre reuniones.
3. Piloto limitado a las tres cuentas corporativas más grandes y a la zona donde están sus empleados; la base de miembros identifica la cuenta de cada uno.
4. Mensajes salientes por conversación: 5, 7 y 10.
5. 59% de conversaciones pasa por el nivel 2; 1 a 4 mensajes al proveedor; la plantilla al proveedor es de utilidad.
6. Tokens por llamada al modelo: 2.000 a 8.000 de entrada, 50 a 200 de salida; 1 a 3 llamadas.
7. Todas las conversaciones por WhatsApp y con texto libre (cotas altas de costo).
8. Infraestructura incremental: USD 200, 500 y 1.000 al mes.
9. Escenarios de desplazamiento (a), (b), (c) y (d) de B5.
10. M2: 300 tokens por sede (rango 150-500) y respuesta de 300 tokens.

Dudas:
11. ¿La tarifa oficial de Meta desde octubre de 2026 es 0,0113? Es la variable que más mueve el resultado (B7: el base empata con tarifa doble).
12. **Resuelto:** política de Meta para proveedores de IA (verificada el 2026-11-09, `04`). Desde el 15 de enero de 2026 Meta prohíbe en WhatsApp Business Platform los asistentes de IA de propósito general cuando la IA es el producto principal; los bots de empresas para una función concreta siguen permitidos. El copiloto la cumple: es un bot de una función concreta (orientar a la red de proveedores y agendar), el modelo solo clasifica en una lista cerrada y el contrato con el proveedor del modelo ya exige que no entrene con los datos (F2 A6). Condición a mantener: no usar los datos de WhatsApp para entrenar modelos.
13. ¿Salud360 ya tiene cuenta de WhatsApp Business Platform (la API) o usa la app de WhatsApp Business para soporte? Cambia el plazo de la semana 1.
14. ¿El USD 1,85 de soporte incluye el costo de Meta por los mensajes que soporte envía por WhatsApp desde octubre de 2026? Si no, la línea base hoy es mayor y el ahorro también.
15. ¿El ahorro de soporte se puede convertir en caja (dotación) o solo en capacidad? Pregunta para el CFO.
16. ¿Cuántos empleados tienen las tres cuentas y dónde están? Define volumen, zona y costo del piloto (Parte B, costo del piloto).
17. Contingencia A3: ¿basta un aviso genérico de emergencias revisado por el abogado mientras no haya aprobación del consejo?
18. ¿Qué proveedor de la zona acepta participar en la demo (reserva real o solicitud de nivel 2)?
18a. ¿Cuántas cuentas corporativas tiene Salud360 y de qué tamaño? Define el retorno total por renovación (B8).
18b. ¿Cuántas cuentas corporativas se pierden al año? Define cuánto ingreso está en juego (B8).
18c. ¿Cuál es el margen de las cuentas corporativas? B8 usa ingreso porque el brief solo da el margen individual (§05).

Incoherencias detectadas con F1 y F2 (19 a 23 corregidas en F1 y F2 el 2026-11-09; 24 sigue abierta para F5):
19. F1 C (M5) dice "Meta cobra por conversación". Según `04`, cobra por mensaje entregado. Ajustar redacción.
20. F2 A4 dice que la confirmación al miembro "puede cobrarse si llega fuera de la ventana de 24 horas". Desde octubre de 2026 se cobra también dentro de la ventana (`04`): todo mensaje saliente cuesta.
21. F2 B2 lista "costo por mensaje" como desventaja de A. Con los precios de `04` el costo del modelo es despreciable (B3); la desventaja real de A es el subprocesador adicional y la carga de evaluación. Además A podría bajar el costo si ahorra mensajes de menú.
22. F1 C (M4) fija la meta "costo por interacción claramente menor a USD 1,85". La comparación correcta es por contacto evitado (8 conversaciones por contacto en base: USD 1,08), no por conversación (USD 0,14). Precisar en D4.
23. F2 A1 (punto 3) incluye elegir dependiente; F3 lo corta del piloto (A5). Es decisión de alcance, no contradicción, pero D2 y D3 deben decir lo mismo.
24. F2 A2 dejaba "proveedor y modelo concretos" para F3. F3 usa Claude Haiku 5.5 solo como ejemplo de precio (`04`), no como elección final. Falta decidir si D2 nombra proveedor.
