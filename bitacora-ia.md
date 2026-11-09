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

## Para el apéndice
- Caso donde se equivocó con confianza o fue superficial:
- Algo que se corrigió y por qué el criterio propio fue mejor:
- Parte que nunca se delegaría a un modelo y por qué:
- Tiempo total aproximado: