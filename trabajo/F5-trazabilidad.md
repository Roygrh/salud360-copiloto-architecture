# F5: Trazabilidad de cifras del entregable

Cada número que aparece en `entregable/copiloto-salud360.md` (D1 a D8), con su origen. Sirve para defender cada cifra en la sesión en vivo (§07). Orígenes: sección del brief, precio de `contexto/04-precios-referencia.md`, supuesto (registrado en `contexto/03-plan-y-estado.md`) o cálculo (con la operación y el archivo de trabajo donde se hizo).

## Datos del brief

| Número | Sección D | Origen | Operación |
|---|---|---|---|
| 38.000 miembros | D4 | §03 | |
| 500 y 748 proveedores | D7 | §03 (marketing y export) | |
| 1.140 sedes | D3, D4, D7 | §03 | |
| 18% sedes con teléfono compartido | D2 | §03 | |
| 41% con disponibilidad estructurada | D1, D2, D4, D7 | §03 | |
| 63% con precios completos | D1 | §03 | |
| 37% sin precios completos | D2 | Cálculo (F2 A5) | 100 - 63 |
| 214 formas de escribir especialidades | D1, D2, D3 | §03 | |
| 96.000 búsquedas al mes | D4 | §03 | |
| 9.000 contactos de soporte | D4, D7 | §03 (dashboard); usado como techo (supuesto F1 A2) | |
| 11.300 contactos "¿a dónde voy?" | D7 | §03 (hoja de la analista); no usado | |
| 6 min 40 s | D7 | §03 | |
| USD 1,85 por contacto | D1, D2, D3, D4 | §03 | |
| USD 3,10 margen individual | D4 | §03, §05 | |
| 2.400 y 3.200 consultas de telemedicina | D2 | §03 | |
| USD 9,40 por consulta de telemedicina | D2, D4 | §03 | |
| USD 10 por empleado corporativo | D4 | §01 | |
| 4 ingenieros | D2, D3, D5 | §03, §05 | |
| 8 semanas | todo | M3 (§04) | |
| Tres cuentas corporativas | D1, D3, D5, D7 | M3 (§04) | |
| Una reunión del consejo al mes | D3 | §05 | |
| Mitad de proveedores no contesta | D1, D7 | §02 | |

## Precios externos (contexto/04)

| Número | Sección D | Origen | Operación |
|---|---|---|---|
| USD 0,0113 por mensaje saliente | D3, D4 | contexto/04 (fuente secundaria; supuesto: tarifa oficial de octubre no verificada) | |
| 1 de octubre de 2026 (cobro de mensajes de servicio) | D4 | contexto/04 | |
| Julio de 2025 (cobro por mensaje) | D8 | bitacora-ia.md | |
| Haiku 5.5: USD 0,10 y 0,50 por millón | D4 | contexto/04 | |
| Opus 5.5: USD 4 y 20 por millón | D4 | contexto/04 | |
| 24 horas (ventana de atención) | D8 | contexto/04 | |
| 2026-11-08 y 2026-11-09 (verificación) | D4 | contexto/04 | |

## Supuestos

| Número | Sección D | Origen | Operación |
|---|---|---|---|
| 2 ingenieros equivalentes | D3 | Supuesto F3 A1 | 4 × 50% |
| Analista a 0,5 | D3 | Supuesto F3 A1 | |
| 14 semanas asignadas, 2 de reserva | D3 | Supuesto F3 A1 | 16 - 14 = 2 |
| 5, 7 y 10 mensajes al miembro | D4 | Supuesto F3 B2 | |
| 1, 2 y 4 mensajes al proveedor | D4 | Supuesto F3 B2 | |
| 4.000 tokens de entrada y 100 de salida (base) | D4 | Supuesto F3 B2 | |
| Modelo al 20% del texto libre | D2, D3, D4, D5 | Decisión F2 | |
| Infraestructura 200, 500 y 1.000 al mes | D4 | Supuesto F3 B2 | |
| 300 tokens por sede; 3.000 de instrucciones; 300 de respuesta | D4 | Supuesto F3 B4 | |
| (a) 30/50/70%; (b) 30/50/70%; confirmación 20/40/60% | D4, D7 | Supuesto F3 B5 | |
| 11, 8 y 6 conversaciones por contacto evitado | D4 | Supuesto F3 B5 (marcado "Supuesto" en la tabla de D4; el 10,7 es referencia, no derivación) | |
| Cuenta de 30 empleados | D4 | Supuesto F3 B8 | |
| 5 puntos de entrada del piloto | D1, D3 | Decisión F3 A4 | |
| 2 o 3 sedes ancla por punto de entrada | D2, D7 | Decisión F2 A4, F4 B2 | |
| 2 o 3 proveedores en el ensayo de la semana 6 | D7 | F3 A2 | |
| Calendario: reunión 1 semana 3, reunión 2 semana 7; contingencia semana 4 | D3, D7 | Supuesto F3 A2, A3 | |
| Semanas 3-5 (campaña de precios), semana 6 (prueba final), semanas 6-7 (sombra interna) | D3, D5, D7 | F3 A2, F4 A3 | |
| Semanas 9-12 (el régimen se abre desde las semanas 9-12, por zonas; la app va después) | D3 | F3 A5, F4 A5 | |
| 911 | D3 | Dato confirmado por Enrique, fuera del brief; uso en la contingencia según F3 A3 y decisión de F5 | |
| 5 días hábiles de sombra en producción | D3, D5 | Supuesto F4 A3 | |
| 400 casos: 200 (40 × 5), 80 (20 retenidos), 60, 30, 30; más 50 salidas fabricadas | D5 | Supuesto F4 A1 | 5 × 40 = 200; 200 + 80 + 60 + 30 + 30 = 400 |
| Umbrales puerta 1: 100% alarmas, 100% identificadores | D5 | F4 A2 | |
| Umbrales puerta 2: ≥ 80%, ≤ 5%, ≤ 15%, ≥ 10 puntos, 0, 0, ≥ 98% en 3 corridas, ≤ 3 s | D2, D5 | Supuesto F4 A2 | |
| Coincidencia ≥ 80% para salir de sombra | D5 | Supuesto F4 A3 | |
| Alertas: 5 puntos, > 15%, > 25%, > 0,5%, > 40%, < 40% y < 20%, > 10 mensajes | D5, D7 | Supuesto F4 A4 | |
| 500 conversaciones con IA y 2.000 sin IA | D5 | Supuesto F4 A5 | 500 / 0,20 = 2.500; 2.500 - 500 = 2.000 |
| Criterio en régimen: ≥ 5 puntos, 5 puntos de pérdida, corrección > 25%, 1 mensaje | D5 | Supuesto F4 A5 | |
| Bloques de 2 semanas hasta 8 | D5 | F4 A5 | |
| 4 semanas (ventana del experimento; revisión de proveedores) | D5, D7 | F4 A5, F4 B2 | |
| Corrida a las 6:00 | D5 | F4 A6 | |
| Tiempos de respuesta: 1 minuto, 10 minutos, 1 hora, 1 a 3 días | D5 | Supuesto F4 A6 | |
| 3 sedes en la demo; 3 semanas en el mensaje del hombro | D3 | F3 A6 (guion) | |

## Cálculos

| Número | Sección D | Origen | Operación |
|---|---|---|---|
| 16 semanas-ingeniero | D3 | Cálculo F3 A1 | 2 × 8 |
| ~1,9 reuniones del consejo | D3 | Cálculo F2 A3 | 8 / ~4,3 semanas por mes |
| ~5 veces (telemedicina frente a soporte) | D2 | Cálculo F2 A3 | 9,40 / 1,85 = 5,1 |
| ~800 consultas libres | D2 | Cálculo F1 A4 | 3.200 - 2.400 |
| 59% al nivel 2 | D4, D7 | Supuesto con cálculo F3 B2 | 100% - 41% |
| USD 16.650 al mes | D4 | Cálculo F1 A2, F3 B1 | 9.000 × 1,85 |
| USD 0,44 por miembro | D4 | Cálculo F3 B1 | 16.650 / 38.000 |
| 14,2% del margen | D4 | Cálculo F3 B1 | 0,44 / 3,10 |
| 0,0565; 0,0791; 0,1130 | D4 | Cálculo F3 B2 | 5, 7, 10 × 0,0113 |
| 0,0067; 0,0133; 0,0267 | D4 | Cálculo F3 B2 | 0,59 × 1, 2, 4 × 0,0113 |
| 0,000045; 0,000090; 0,000540 | D4 | Cálculo F3 B2 | (llamada) × 0,20; base (4.000 × 0,10 + 100 × 0,50) / 10⁶ = 0,000450 |
| 0,0172; 0,0430; 0,0860 | D4 | Cálculo F3 B2 | 200, 500, 1.000 / 11.632 |
| Variable 0,0632; 0,0925; 0,1402 | D4 | Cálculo F3 B2 | suma de canal y modelo |
| Total 0,0804; 0,1355; 0,2262 | D4 | Cálculo F3 B2 | variable + infraestructura |
| 0,0924 canal; ~1.027 veces | D4; D1 y D8 (~1.000) | Cálculo F3 B3 | 0,0791 + 0,0133; 0,0924 / 0,000090 |
| ~25 llamadas por mensaje ahorrado | D4 | Cálculo F3 B3 | 0,0113 / 0,000450 |
| 345.000 tokens | D4 | Cálculo F3 B4 | 1.140 × 300 + 3.000 |
| USD 1,386 por mensaje | D4 | Cálculo F3 B4 | 345.000 × 4 / 10⁶ + 300 × 20 / 10⁶ |
| USD 9,70 por conversación | D1, D4 | Cálculo F3 B4 | 7 × 1,386 |
| 5,2 contactos de soporte | D4 | Cálculo F3 B4 | 9,70 / 1,85 |
| USD 112.830 al mes | D4 | Cálculo F3 B4 | 11.632 × 9,70 |
| 95,8% del margen | D4 | Cálculo F3 B4 | 112.830 / 38.000 = 2,97; 2,97 / 3,10 |
| ~385 veces (método M2 con modelo pequeño) | D4 | Cálculo F3 B4 | 0,1733 / 0,00045 |
| 52,8%; 64,6%; 76,4% | D4 | Cálculo F3 B5 | 41% + 59% × 20%, 40%, 60% |
| 428; 1.454; 3.369 contactos evitados | D4 | Cálculo F3 B5 | 9.000 × a × b × c |
| 4,8%; 16,2%; 37,4% | D4 | Cálculo F3 B5 | evitados / 9.000 |
| 791,80; 2.689,90; 6.232,65 | D4 | Cálculo F3 B5 | evitados × 1,85 |
| 10,7 búsquedas por contacto | D4 (línea de referencia bajo la tabla; no deriva 11, 8 ni 6) | Cálculo F3 B5 | 96.000 / 9.000 |
| 4.708; 11.632; 20.214 conversaciones | D4, D5 | Cálculo F3 B5 | evitados × 11, 8, 6 |
| 935,49; 1.575,96; 2.369,80 | D4 | Cálculo F3 B5 | conversaciones × 0,0925 + 500 |
| -143,69; +1.113,94; +3.862,85 | D4, D7 | Cálculo F3 B5 | ahorro - costo |
| 356,31 | D4 | Cálculo F3 B5 | 791,80 - 435,49 (435,49 = 4.708 × 0,0925) |
| 0,0246; 0,0415; 0,0624 por miembro | D4; D1 y D3 paso 7 de la demo (~4 centavos) | Cálculo F3 B6 | costo / 38.000 |
| 0,79%; 1,34%; 2,01% del margen | D1, D4 | Cálculo F3 B6 | por miembro / 3,10 |
| USD 1,08 por contacto evitado | D4 (ya no en el paso 7 de la demo de D3) | Cálculo F3 B5 | 8 × 0,1355 |
| USD 300 al mes por cuenta | D4 | Cálculo F3 B8 | 30 × 10 |
| 3,71 → 4 cuentas | D4 | Cálculo F3 B8 | 1.113,94 / 300 |
| 0,48 → 1 cuenta | D4 | Cálculo F3 B8 | 143,69 / 300 |
| USD 0,0230 por mensaje (2,0 veces) | D4 | Cálculo F3 B7 | (0,1883 - 0,0001) / 8,18; 0,0230 / 0,0113 |
| Más de 15 mensajes | D4 | Cálculo F3 B7 | (0,1883 - 0,0133 - 0,0001) / 0,0113 = 15,5 |
| 16,3 conversaciones por contacto | D4 | Cálculo F3 B7 | 2.189,90 / (1.454 × 0,0925) |
| ~1% a telemedicina; 118,5 derivaciones | D4, D5 | Cálculo F3 B7 | 1.113,94 / 9,40; 118,5 / 11.632 |
| ± 5 puntos | D5 | Cálculo F4 A5 | 2 × raíz(0,25 / 500 + 0,25 / 2.000) = 2 × 0,025 |
| 625 por semana | D5, D8 | Cálculo F4 A5 | 2.500 / 4 |
| USD 0,18 por corrida; USD 5,40 al mes | D5 | Cálculo F4 A6 | 400 × 0,000450; × 30 |
| 20% y 80% (peor caso de la mañana) | D5 | F4 A6 | 100% - 20% |
