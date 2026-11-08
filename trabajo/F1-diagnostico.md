# F1: Diagnóstico

Resultado interno. No es una sección del entregable; alimenta D1, D2, D3, D4 y D7.

## A. Reconciliación de números (§03)

### 1. Proveedores: 500 vs 748
- Marketing (500) probablemente redondea o está desactualizado. La base (748) puede incluir inactivos o duplicados.
- Hay 1.140 sedes y el 18% comparte teléfono con otra sede: señal de duplicados o de centrales telefónicas compartidas.
- Supuesto: el número de proveedores activos es desconocido. Unidad del directorio: sedes (1.140).

### 2. Soporte: 9.000 totales vs 11.300 "¿a dónde voy para X?"
- Contradicción: un subconjunto no puede superar al total.
- Causas posibles: la hoja cuenta mensajes y no casos; mide otro período; el dashboard no incluye WhatsApp.
- Supuesto: 9.000 al mes como techo, por ser el dato medido.
- Costo actual de soporte: 9.000 × $1,85 = $16.650 al mes. Por miembro: $16.650 / 38.000 = ~$0,44 al mes.
- Coherencia interna: $1,85 por 6 min 40 s equivale a ~$16,65 por hora de agente, costo total. Plausible.

### 3. Búsquedas y citas
- 96.000 × 4,8% = ~4.600 citas al mes.
- Solo el 41% de proveedores tiene disponibilidad estructurada, por lo que no está claro qué significa "cita agendada" (reserva real o clic en llamar).
- El directorio es público: parte de las búsquedas son de no miembros.

### 4. Telemedicina
- 3.200 de capacidad (estimado) menos 2.400 usadas = ~800 consultas libres al mes.
- Costo por consulta: $9,40, unas cinco veces un contacto de soporte ($1,85).
- Hallazgo: derivar a telemedicina no es gratis; es la salida más cara. Se usa solo donde hace falta un clínico.
- Costo actual: 2.400 × $9,40 = $22.560 al mes.

### 5. Margen
- $3,10 por miembro individual al mes. Se desconoce el margen de planes familiares y corporativos, y si los 38.000 incluyen dependientes.

### 6. Calidad de datos
- 41% con disponibilidad estructurada, 63% con precios completos, 214 formas de escribir especialidades, 18% de sedes con teléfono compartido.
- Coincide con el relato de §02 (lista sin orden, sin precios, la mitad no contesta).

### 7. Equipo
- 4 ingenieros, sin fuente. Según §05 también mantienen la app actual: la capacidad real para el proyecto es menor a 4.

## B. Causa raíz
El problema no es la falta de IA. El catálogo de proveedores está incompleto y desordenado, y la app no ayuda a pasar de "me duele el hombro" a "este tipo de proveedor".

1. Datos malos: precios faltantes, 214 nombres de especialidades, sedes duplicadas.
2. Falta navegación por necesidad: el miembro no sabe qué especialidad buscar.
3. Proveedores que no responden: sin disponibilidad estructurada, agendar depende de que alguien conteste.

Un modelo sobre datos malos produce respuestas incorrectas con confianza. Los datos van primero.

La baja renovación ("no supe cómo usarlo", §02) es síntoma de las tres causas, más posiblemente un problema de comunicación del beneficio a los empleados.

## C. Mandato

| Código | Decisión | Razón |
|---|---|---|
| M1 | Modificar; rechazar la parte clínica | Un modelo no debe recomendar especialista a partir de síntomas: no hay médico en planta (§05) y son datos de salud sensibles. En su lugar, orientación hacia una lista cerrada de puntos de entrada validada por el consejo médico, con señales de alarma que derivan a emergencias o telemedicina. Agendar en el mismo flujo solo es posible para el 41% con disponibilidad |
| M2 | Rechazar el método, mantener el objetivo | Meter la base en el prompt no la vuelve actual (está mal en origen), cuesta en cada mensaje y envía toda la base a un subprocesador. Precios y disponibilidad salen de la base de datos; el modelo nunca los genera. No hace falta el modelo más caro para interpretar texto |
| M3 | Aceptar la fecha, recortar alcance | Con menos de 4 ingenieros efectivos sale un piloto acotado (pocas especialidades y datos limpios), no el producto completo |
| M4 | Aceptar y cuantificar | Meta: costo por interacción claramente menor a $1,85 (contacto de soporte). Se demuestra en D4 |
| M5 | Aceptar con condiciones | Los miembros ya usan WhatsApp con soporte (§01). Meta cobra por conversación y es subprocesador de datos de salud: consentimiento al inicio y mínimo dato clínico en el canal |

Lo que se rechaza construir: un modelo que decide por sí solo a qué especialista ir según los síntomas.

## D. Conclusión
- Problema real: que el miembro pase de describir su necesidad con sus palabras a un proveedor que lo atienda a precio conocido, sin llamar a soporte.
- Prioridades: (1) limpiar datos de proveedores, (2) navegación por necesidad, (3) IA como capa delgada que solo interpreta el lenguaje del usuario.