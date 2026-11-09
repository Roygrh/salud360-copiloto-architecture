# Bitácora de uso de IA (material para D8)

## Herramientas
| Herramienta | Para qué parte |
|---|---|
| | |

## Registro de correcciones
Anotar cada vez que una salida de la IA sea incorrecta, superficial o se modifique por criterio propio.

| Fecha | Fase | Qué dijo la IA | Qué estaba mal | Cómo se detectó | Qué se decidió |
|---|---|---|---|---|---|
| 2026-11-08 | F2 | Que al modelo solo viaja el texto "sin identificadores" | Es una afirmación absoluta imposible de garantizar; el texto libre puede traer nombres de terceros y lugares | Revisión del diseño con un ejemplo concreto ("a mi hija María le duele la muela") | Filtro de identificadores conocidos más contrato de subprocesador obligatorio y consentimiento que nombra al proveedor del modelo |
| 2026-11-08 | F2 | Diagrama con identidad, alarmas y modelo en paralelo desde el orquestador | Contradecía el diseño escrito; sugería que el modelo podía recibir texto sin consentimiento ni filtro de alarmas | Comparando el diagrama con la tabla A2 y la sección A6 | Cadena explícita orquestador, identidad, alarmas, modelo |
| 2026-11-09 | F1 | Que Meta cobra WhatsApp "por conversación" y que las respuestas dentro de la ventana de 24 horas son gratis | Información desactualizada. Meta cobra por mensaje desde julio de 2025 y cobra las respuestas desde octubre de 2026 | Al buscar los precios oficiales de Meta para calcular D4 | Usar solo precios verificados con fuente (`contexto/04-precios-referencia.md`) y recalcular. El costo dominante resultó ser el canal, no el modelo |
| 2026-11-09 | F4 | Que el experimento A frente a B se decidiría en 4 semanas dentro del piloto | No verificó si el piloto tenía volumen suficiente; el propio cálculo de F4 exigía unas 625 conversaciones con texto libre por semana, que el piloto de tres cuentas no alcanza | Revisando la coherencia entre el tamaño del piloto (F3) y el volumen mínimo (F4) | En el piloto el modelo se valida solo en seguridad y calidad; la decisión A frente a B se toma con volumen de régimen |
| 2026-11-09 | F6 | Que el diagrama de D2 quedaba "legible" en el PDF forzando en el script la dirección vertical (letra efectiva ~5,6 pt), con el .md aún en horizontal | 5,6 pt no se lee en papel, y el diagrama se lleva a la sesión en vivo (§08); además el PDF dejaba de coincidir con el .md | Revisión de Enrique del PDF y del informe de la fase | Meta de al menos 7 pt; dirección vertical en el .md y en `arquitectura.mmd`, leyenda como línea de texto y ajuste de parámetros de render. Resultado: 7,4 pt sin tocar etiquetas ni nodos del flujo |

## Para el apéndice
- Caso donde se equivocó con confianza o fue superficial:
- Algo que se corrigió y por qué el criterio propio fue mejor:
- Parte que nunca se delegaría a un modelo y por qué:
- Tiempo total aproximado: