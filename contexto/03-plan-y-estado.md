# Plan y estado

## Fases

| Fase | Qué se hace | Resultado | Estado |
|---|---|---|---|
| F0 | Repositorio y archivos de contexto | Repo listo | Hecho |
| F1 | Diagnóstico: números, causa raíz, mandato | `trabajo/F1-diagnostico.md` | Hecho, pendiente validación final |
| F2 | Arquitectura con diagrama (D2) y versión sin IA (D6) | `trabajo/F2-diseno.md`, `trabajo/F2-diagrama.mmd` | Hecho, corregido, pendiente validación |
| F3 | Plan de 8 semanas (D3) y economía unitaria (D4) | `trabajo/F3-plan-y-costos.md` | Pendiente |
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

## Supuestos vigentes
- Contactos de soporte: se usa 9.000 al mes como techo (dato medido).
- Unidad del directorio: sedes (1.140), no proveedores.
- F2: la base de miembros tiene el número de WhatsApp del titular.
- F2 (respaldado por §01): la app ya tiene reservas. Falta confirmar si usa la disponibilidad estructurada del 41%.
- F2: la consulta presencial la paga el miembro y no cuesta a Salud360.
- F2: las sedes tienen dirección suficiente para filtrar por cantón.
- F2 (respaldado por §01): soporte ya atiende por WhatsApp. Falta confirmar que su herramienta permita recibir conversaciones traspasadas con contexto.

## Preguntas pendientes para el cliente
1. ¿Por qué los 11.300 contactos "¿a dónde voy para X?" superan los 9.000 totales?
2. ¿Qué cuenta como "cita agendada" en el 4,8%?
3. ¿Los 38.000 miembros incluyen dependientes?