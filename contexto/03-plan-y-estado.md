# Plan y estado

## Fases

| Fase | Qué se hace | Resultado | Estado |
|---|---|---|---|
| F0 | Repositorio y archivos de contexto | Repo listo | Hecho |
| F1 | Diagnóstico: números, causa raíz, mandato | `trabajo/F1-diagnostico.md` | Hecho, pendiente validación final |
| F2 | Arquitectura con diagrama (D2) y versión sin IA (D6) | `trabajo/F2-diseno.md`, `trabajo/F2-diagrama.mmd` | Hecho, corregido, pendiente validación |
| F3 | Plan de 8 semanas (D3) y economía unitaria (D4) | `trabajo/F3-plan-y-costos.md` | Hecho, corregido, pendiente validación |
| F4 | Validación y operación (D5), preguntas y riesgos (D7) | `trabajo/F4-operacion-y-riesgos.md` | Hecho, corregido, pendiente validación |
| F5 | D1 al final, recorte a 8 páginas, D8 | `entregable/copiloto-salud360.md` | Hecho, corregido, pendiente validación |
| F6 | Exportar PDF, revisar defendibilidad, preparar pitch de 10 min | `entregable/copiloto-salud360.pdf` (script `herramientas/generar-pdf.py`) | PDF generado, pendiente validación: 9 páginas, D1 a D7 en 8 (D8 en la página 9). Diagrama vertical (TB en el .md y en `arquitectura.mmd`) y simplificado: leyenda como línea de texto bajo el diagrama; letra efectiva 7,4 pt |

Cada fase termina con validación de Enrique antes de pasar a la siguiente.

## Decisiones tomadas
- Idioma del entregable: español.
- Un solo diagrama de arquitectura, en Mermaid, de media página aproximadamente.
- La solución no tiene que ser un agente de IA: la IA entra solo donde aporte lo que el software tradicional no puede (§09, D6).
- Mandato (detalle en F1): M1 modificar y rechazar la parte clínica; M2 rechazar el método y mantener el objetivo; M3 aceptar la fecha con alcance recortado; M4 aceptar y cuantificar; M5 aceptar con condiciones.
- F2: flujo determinista (máquina de estados) con el modelo como pieza opcional; con el modelo apagado queda la versión sin IA.
- F2: el modelo solo clasifica texto libre en una lista cerrada de puntos de entrada validada por el consejo médico; el miembro confirma con un botón.
- F2: todo texto que lee el miembro es plantilla aprobada; el modelo no redacta respuestas.
- F2: precios, disponibilidad y ranking salen de consultas SQL a la base limpia; el modelo no ve la base de proveedores.
- F2: reglas de alarma deterministas antes del modelo; el modelo solo puede escalar, nunca bajar la urgencia.
- F2: valor por defecto medicina general; telemedicina ($9,40, §03) solo por regla del consejo o pedido explícito.
- F2: agendamiento en tres niveles: reserva directa (41% con disponibilidad, §03), solicitud al proveedor por WhatsApp, contacto asistido por soporte.
- F2: el ranking premia disponibilidad y confirmación como incentivo a proveedores (§05).
- F2: limpieza de datos fuera de línea con aprobación de la analista; el modelo solo propone; nunca se estiman precios.
- F2: consentimiento por botón antes de cualquier texto libre; texto libre se borra al cerrar la conversación; al modelo viaja solo el texto, tras un filtro que elimina los identificadores conocidos (el texto libre puede traer otros datos personales); contrato de subprocesador obligatorio y consentimiento que nombra al proveedor del modelo.
- F2: servicios administrados (serverless, base relacional, cola) y un solo backend para WhatsApp y app.
- F2: lanzamiento con B para todo el tráfico y A para el 20% de las conversaciones con texto libre tras pasar una prueba con conjunto de casos y 5 días hábiles en modo sombra; sube al 100% si mejora la conversión a cita sin aumentar alarmas mal resueltas, si no se apaga (umbrales en F4 A5).
- F3: única fuente de precios: `contexto/04-precios-referencia.md` (WhatsApp USD 0,0113 por mensaje saliente; Haiku 5.5 y Opus 5.5 como referencia).
- F3: ruta crítica: consejo médico, reunión 1 en semana 3 (aprueba catálogo) y reunión 2 en semana 7 (ajustes); contingencia: puntos de entrada sin juicio clínico, solo botones y sin modelo.
- F3: piloto de semana 8 solo por WhatsApp, para empleados de las tres cuentas corporativas de la demo, sedes publicables de su zona y cinco puntos de entrada (medicina general, odontología, laboratorio e imágenes con orden, nutrición).
- F3: se cortan el copiloto en la app (después de abrir el régimen por zonas), psicología como punto de entrada, dependientes, recordatorios y modelo para limpieza.
- F3: demo del CEO: caso del hombro hasta cita, caso de alarma a emergencias, y apagado del modelo en vivo con el mismo resultado.
- F3: el costo dominante es el canal WhatsApp, no el modelo (~1.000 veces más en base); se diseña para minimizar mensajes salientes.
- F3: M2 cuesta ~USD 9,70 por conversación (5,2 veces un contacto de soporte, 95,8% del margen a volumen base): rechazo cuantificado.
- F3: Meta Business Agent descartado por costo y porque la IA de Meta procesaría datos de salud y redactaría respuestas.
- F3: el retorno principal del copiloto es la renovación de cuentas corporativas; el ahorro en soporte paga la operación (B8).
- F3: la política de Meta para proveedores de IA está verificada (`04`) y el copiloto la cumple: bot de una función concreta, sin usar datos de WhatsApp para entrenar modelos.
- F4: dos puertas de lanzamiento: alarmas y filtro de identificadores al 100% para cualquier texto libre (incluida B); validador al 100% y umbrales del modelo para encender A.
- F4: el modelo solo se enciende si supera al diccionario de B en el mismo conjunto de casos; si no, agrega un subprocesador sin aportar.
- F4: modo sombra en dos tramos: pruebas internas en semanas 6-7 y primeros 5 días hábiles de producción sobre el 20% asignado; A se hace visible después (adoptado en F2 y F3).
- F4: asignación A/B por miembro, no por conversación; comparación solo entre conversaciones con texto libre.
- F4: registros sin texto crudo: eventos por paso con códigos, versión del modelo, del catálogo y de las instrucciones.
- F4: responsable de la semana rotativo entre los 4 ingenieros, en horario laboral; sin guardia, porque el modelo se degrada solo a menú.
- F4: versión del modelo fijada por identificador exacto; corrida diaria del conjunto (USD 5,40 al mes) y apagado automático ante criterios duros.
- F4: cualquier alarma no detectada conocida apaga el modelo y se revisa con el consejo por escrito.
- F4: en el piloto A se valida solo en seguridad y calidad (cero alarmas mal resueltas, corrección, "no sé"); la decisión A frente a B se toma con volumen de régimen, desde las semanas 9-12 (validado por Enrique, 2026-11-09).
- F4: si aun en régimen falta volumen, no se decide: se extiende en bloques de 2 semanas hasta 8; opción 50/50 si no hubo incidentes.
- F3/F4: si hay retraso, A (el modelo) es lo primero que se corta; B sale igual en la semana 8 porque no depende del modelo.
- F4: riesgo que puede matar el proyecto: los proveedores no responden. Mitigación: prueba de vida para entrar al nivel 2, sedes ancla por punto de entrada, medición de respuesta desde la campaña de precios (semanas 3-5).
- F2/F4: prueba de vida y sedes ancla adoptadas para el nivel 2: solo entra al nivel 2 la sede que respondió a la campaña de precios; 2 o 3 sedes ancla por punto de entrada.
- F5: definición de régimen: el copiloto abierto a todos los miembros, desde las semanas 9-12. Se usa igual en D3, D4 y D5.
- F5: el régimen se abre por zonas a medida que sus sedes quedan publicables; el copiloto en la app va después.
- F5: en la contingencia, el aviso de emergencias es texto estándar con el 911 aprobado por el abogado y ratificado por el consejo.

## Supuestos vigentes
- Contactos de soporte: se usa 9.000 al mes como techo (dato medido).
- Unidad del directorio: sedes (1.140), no proveedores.
- F2: la base de miembros tiene el número de WhatsApp del titular.
- F2 (respaldado por §01): la app ya tiene reservas. Falta confirmar si usa la disponibilidad estructurada del 41%.
- F2: la consulta presencial la paga el miembro y no cuesta a Salud360.
- F2: las sedes tienen dirección suficiente para filtrar por cantón.
- F2 (respaldado por §01): soporte ya atiende por WhatsApp. Falta confirmar que su herramienta permita recibir conversaciones traspasadas con contexto.
- F3: capacidad de 2 ingenieros equivalentes (4 × 50%) y analista a 0,5; 16 semanas-ingeniero, 14 asignadas y 2 de reserva (la reserva la consumen casi por completo las extensiones del modelo de F4).
- F3: calendario del consejo (reuniones en semanas 3 y 7) y que acepta revisión por escrito entre reuniones.
- F3: la base de miembros identifica la cuenta corporativa de cada miembro; la zona del piloto se define con los empleados de las tres cuentas.
- F3: mensajes salientes al miembro por conversación: 5, 7 y 10; 59% de conversaciones pasa por nivel 2 con 1 a 4 mensajes al proveedor (plantilla de utilidad).
- F3: llamada al modelo de 2.000 a 8.000 tokens de entrada y 50 a 200 de salida; todas las conversaciones por WhatsApp y con texto libre (cota alta).
- F3: infraestructura incremental de USD 200, 500 y 1.000 al mes, a validar con la factura real de nube.
- F3: desplazamiento de soporte: conservador 4,8%, base 16,2%, optimista 37,4% de los 9.000 contactos; 11, 8 y 6 conversaciones por contacto evitado.
- F3: margen individual (USD 3,10) aplicado a los 38.000 miembros.
- F3: cuenta corporativa de ejemplo de 30 empleados (dentro del rango de menos de 50, §03) para el retorno por renovación (B8).
- F4: conjunto de casos de 400 (200 comunes, 80 alarmas con 20 retenidas, 60 ambiguos, 30 inyección, 30 datos personales) más 50 salidas fabricadas para el validador; soporte con ~6 agentes equivalentes (1.000 horas al mes / 160).
- F4: umbrales del modelo: acierto ≥ 80%, propuesta equivocada ≤ 5%, "no sé" ≤ 15%, ventaja ≥ 10 puntos sobre el diccionario de B, estabilidad ≥ 98% en 3 corridas, demora ≤ 3 s; cero alarmas rebajadas y cero salidas fuera de la lista.
- F4: sombra en producción de 5 días hábiles; pasa a visible con coincidencia ≥ 80% con la elección del miembro.
- F4: experimento (en régimen): mínimo 500 conversaciones con texto libre en A (± 5 puntos), es decir 625 por semana en 4 semanas; A sube al 100% con ≥ 5 puntos de mejora en conversión, corrección ≤ 15% y sin alarmas mal resueltas; se apaga con ≤ -5 puntos o corrección > 25%; empate se decide por ahorro de al menos 1 mensaje saliente.
- F4: alertas: "no sé" > 25% diario, corrección > 15% semanal, telemedicina "no ubicado" > 0,5%, nivel 3 > 40%, respuesta de proveedores < 40% (crítico < 20%), más de 10 mensajes al miembro por conversación.
- F4: clínicos de telemedicina o miembros del consejo disponibles por horas para redactar las alarmas retenidas.
- F4: sedes ancla aceptan responder el mismo día hábil a cambio de ranking y sello.

## Preguntas pendientes para el cliente
1. ¿Por qué los 11.300 contactos "¿a dónde voy para X?" superan los 9.000 totales?
2. ¿Qué cuenta como "cita agendada" en el 4,8%?
3. ¿Los 38.000 miembros incluyen dependientes?