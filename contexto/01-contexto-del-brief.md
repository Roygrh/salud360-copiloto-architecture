# Contexto del brief

Resumen del PDF del challenge, con referencia a su sección. Las secciones del brief son §00 a §10; los entregables son D1 a D8.

## Qué es Salud360 (§01)
- Plataforma de membresía de salud privada en Costa Rica. No es un seguro: no adjudica reclamos.
- Cuota mensual aproximada: $11 individual, $27 familia, $10 por empleado en cuentas corporativas.
- A cambio, el miembro obtiene precios fijos negociados con proveedores independientes: medicina general, especialistas, laboratorios, imágenes, odontología, nutrición, psicología.
- Productos: directorio público (abierto a cualquiera), app del miembro (plan, dependientes, reservas, historial), telemedicina (llamada de orientación con clínico real, incluida), soporte humano por teléfono y WhatsApp.
- Los proveedores son negocios independientes: no usan el software de Salud360. Solo aceptaron una lista de precios.

## El problema según el negocio (§02)
- Jefa de experiencia del miembro: un miembro con dolor de hombro abre el directorio, ve una lista sin orden útil, con y sin precios; la mitad no contesta el teléfono; llama a soporte; un agente tarda unos 7 minutos; el miembro le dice a RR.HH. que el beneficio no funciona y la empresa no renueva el contrato.
- Jefe de ventas corporativas: las cuentas pequeñas y medianas renuevan poco; en entrevistas de salida los empleados dicen "no supe cómo usarlo".

## Los números (§03)
El recuadro "Fair warning" advierte que algunas cifras se contradicen y que detectarlo es parte del ejercicio.

| Dato | Valor | Fuente |
|---|---|---|
| Miembros activos | 38.000 | facturación |
| Proveedores en la red | 500 | sitio de marketing |
| Proveedores en la red | 748 | export de base de proveedores |
| Sedes registradas | 1.140 | export de base de proveedores |
| Sedes que comparten teléfono con otra | 18% | hoja de la analista |
| Proveedores con disponibilidad estructurada | 41% | hoja de la analista |
| Proveedores con lista de precios completa | 63% | hoja de la analista |
| Formas distintas de escribir especialidades | 214 | hoja de la analista |
| Búsquedas en el directorio por mes | 96.000 | dashboard de producto |
| Búsquedas que terminan en cita | 4,8% | dashboard de producto |
| Contactos de soporte por mes, todos los motivos | 9.000 | dashboard de soporte |
| Contactos de soporte por mes, "¿a dónde voy para X?" | 11.300 | hoja de la analista |
| Tiempo mediano de atención en soporte | 6 min 40 s | dashboard de soporte |
| Costo total por contacto de soporte | ~$1,85 | finanzas |
| Margen bruto por miembro individual al mes | ~$3,10 | finanzas |
| Consultas de telemedicina por mes | 2.400 | dashboard de producto |
| Capacidad de telemedicina por mes | ~3.200 | operaciones, estimado |
| Costo total por consulta de telemedicina | ~$9,40 | finanzas |
| Tasa de renovación, cuentas de menos de 50 empleados | 71% | ventas |
| Ingenieros disponibles | 4 | sin fuente |

## El mandato (§04)
Las cinco órdenes de la dirección, tal como se dieron. El §00 advierte: tratarlas como especificación es la forma más común de fallar, y al menos una parte probablemente no se debería construir.

| Código | Quién | Qué pide |
|---|---|---|
| M1 | CEO | El miembro describe sus síntomas en la app, se le dice qué especialista ver y agenda la cita en el mismo flujo |
| M2 | CTO | Usar el mejor modelo y darle toda la base de proveedores en el prompt para que precios y disponibilidad estén siempre al día |
| M3 | CEO | En producción en 8 semanas; ese día lo presenta a sus tres cuentas corporativas más grandes |
| M4 | CFO | No puede agregar costo de infraestructura significativo; mirar el margen por miembro |
| M5 | Jefa de experiencia del miembro | Debe funcionar por WhatsApp |

## Restricciones fijas (§05)
- Datos de salud: dato personal sensible bajo la Ley 8968 de Costa Rica (regulador PRODHAB). Requiere consentimiento expreso e informado. Salud360 responde por lo que haga cualquier subprocesador (tercero que procesa los datos por cuenta de Salud360).
- Los proveedores no pueden ser obligados a adoptar nada. Se puede incentivar y facilitar.
- Equipo: 4 ingenieros y una analista de datos a tiempo parcial. Sin ingenieros de ML, sin equipo de plataforma, sin SRE de guardia. Los mismos 4 mantienen la app actual.
- Sin médico en planta. Hay un consejo médico asesor que se reúne una vez al mes. Los clínicos de telemedicina se contratan por consulta.
- Margen: $3,10 por miembro individual al mes. El CFO revisa la factura de nube línea por línea.

## Glosario
- **Mandato:** las cinco órdenes M1 a M5 del §04.
- **Renovación corporativa:** la empresa cliente decide si sigue pagando la membresía de sus empleados al vencer el contrato.
- **Subprocesador:** tercero que procesa datos personales por cuenta de Salud360 (por ejemplo, el proveedor del modelo de IA o Meta en WhatsApp).
- **Triaje:** decidir la urgencia o el tipo de atención a partir de síntomas. Es un acto clínico.