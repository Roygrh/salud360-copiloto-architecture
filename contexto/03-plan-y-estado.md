# Plan y estado

## Fases

| Fase | Qué se hace | Resultado | Estado |
|---|---|---|---|
| F0 | Repositorio y archivos de contexto | Repo listo | Hecho |
| F1 | Diagnóstico: números, causa raíz, mandato | `trabajo/F1-diagnostico.md` | Hecho, pendiente validación final |
| F2 | Arquitectura con diagrama (D2) y versión sin IA (D6) | `trabajo/F2-diseno.md`, `trabajo/F2-diagrama.mmd` | Hecho, corregido, pendiente validación |
| F3 | Plan de 8 semanas (D3) y economía unitaria (D4) | `trabajo/F3-plan-y-costos.md` | Hecho, corregido, pendiente validación |
| F4 | Validación y operación (D5), preguntas y riesgos (D7) | `trabajo/F4-operacion-y-riesgos.md` | Pendiente |
| F5 | D1 al final, recorte a 8 páginas, D8 | `entregable/copiloto-salud360.md` | Pendiente |
| F6 | Exportar PDF, revisar defendibilidad, preparar pitch de 10 min | PDF enviado | Pendiente |

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
- F2: lanzamiento con B para todo el tráfico y A para el 20% de las conversaciones con texto libre desde el primer día, tras pasar una prueba con conjunto de casos; si en 4 semanas mejora la conversión a cita sin aumentar alarmas mal resueltas sube al 100%, si no se apaga (umbrales en F4).
- F3: única fuente de precios: `contexto/04-precios-referencia.md` (WhatsApp USD 0,0113 por mensaje saliente; Haiku 5.5 y Opus 5.5 como referencia).
- F3: ruta crítica: consejo médico, reunión 1 en semana 3 (aprueba catálogo) y reunión 2 en semana 7 (ajustes); contingencia: puntos de entrada sin juicio clínico, solo botones y sin modelo.
- F3: piloto de semana 8 solo por WhatsApp, para empleados de las tres cuentas corporativas de la demo, sedes publicables de su zona y cinco puntos de entrada (medicina general, odontología, laboratorio e imágenes con orden, nutrición).
- F3: se cortan el copiloto en la app (primero en semanas 9-12), psicología como punto de entrada, dependientes, recordatorios y modelo para limpieza.
- F3: demo del CEO: caso del hombro hasta cita, caso de alarma a emergencias, y apagado del modelo en vivo con el mismo resultado.
- F3: el costo dominante es el canal WhatsApp, no el modelo (~1.000 veces más en base); se diseña para minimizar mensajes salientes.
- F3: M2 cuesta ~USD 9,70 por conversación (5,2 veces un contacto de soporte, 95,8% del margen a volumen base): rechazo cuantificado.
- F3: Meta Business Agent descartado por costo y porque la IA de Meta procesaría datos de salud y redactaría respuestas.
- F3: el retorno principal del copiloto es la renovación de cuentas corporativas; el ahorro en soporte paga la operación (B8).
- F3: la política de Meta para proveedores de IA está verificada (`04`) y el copiloto la cumple: bot de una función concreta, sin usar datos de WhatsApp para entrenar modelos.

## Supuestos vigentes
- Contactos de soporte: se usa 9.000 al mes como techo (dato medido).
- Unidad del directorio: sedes (1.140), no proveedores.
- F2: la base de miembros tiene el número de WhatsApp del titular.
- F2 (respaldado por §01): la app ya tiene reservas. Falta confirmar si usa la disponibilidad estructurada del 41%.
- F2: la consulta presencial la paga el miembro y no cuesta a Salud360.
- F2: las sedes tienen dirección suficiente para filtrar por cantón.
- F2 (respaldado por §01): soporte ya atiende por WhatsApp. Falta confirmar que su herramienta permita recibir conversaciones traspasadas con contexto.
- F3: capacidad de 2 ingenieros equivalentes (4 × 50%) y analista a 0,5; 16 semanas-ingeniero, 14 asignadas y 2 de reserva.
- F3: calendario del consejo (reuniones en semanas 3 y 7) y que acepta revisión por escrito entre reuniones.
- F3: la base de miembros identifica la cuenta corporativa de cada miembro; la zona del piloto se define con los empleados de las tres cuentas.
- F3: mensajes salientes al miembro por conversación: 5, 7 y 10; 59% de conversaciones pasa por nivel 2 con 1 a 4 mensajes al proveedor (plantilla de utilidad).
- F3: llamada al modelo de 2.000 a 8.000 tokens de entrada y 50 a 200 de salida; todas las conversaciones por WhatsApp y con texto libre (cota alta).
- F3: infraestructura incremental de USD 200, 500 y 1.000 al mes, a validar con la factura real de nube.
- F3: desplazamiento de soporte: conservador 4,8%, base 16,2%, optimista 37,4% de los 9.000 contactos; 11, 8 y 6 conversaciones por contacto evitado.
- F3: margen individual (USD 3,10) aplicado a los 38.000 miembros.
- F3: cuenta corporativa de ejemplo de 30 empleados (dentro del rango de menos de 50, §03) para el retorno por renovación (B8).

## Preguntas pendientes para el cliente
1. ¿Por qué los 11.300 contactos "¿a dónde voy para X?" superan los 9.000 totales?
2. ¿Qué cuenta como "cita agendada" en el 4,8%?
3. ¿Los 38.000 miembros incluyen dependientes?