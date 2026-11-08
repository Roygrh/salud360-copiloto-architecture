# Reglas de trabajo del repositorio

## Qué es este proyecto
Documento de propuesta de arquitectura (sin código) para el challenge técnico "Copiloto Salud360". El brief está en el PDF de la carpeta `brief/` y el correo de la reclutadora en `brief/correo-reclutadora.md`. El resumen del brief está en `contexto/01-contexto-del-brief.md`.

## Fuentes de verdad
- Usar solo los archivos de este repositorio. Nada recuperado de otro sitio.
- Si un dato no está en el brief, marcarlo como supuesto y anotarlo en `contexto/03-plan-y-estado.md`.

## Reglas de contenido
- Idioma: español.
- Citar siempre la sección del brief de donde sale algo (ejemplos: §03, M2, D4).
- No inventar números. Toda cifra lleva su fuente o la aritmética visible.
- Explicar brevemente cada término técnico la primera vez que aparece.
- Prohibido usar la raya (guion largo) en `entregable/`. Usar dos puntos, paréntesis, coma o punto. El guion corto de rangos sí se permite.
- Límite: D1 a D7 suman máximo 8 páginas, incluido el diagrama. D8 no cuenta.
- El documento va dirigido a un CEO: directo, decisiones primero, razones después.

## Reglas de trabajo
- No crear ni modificar archivos en `entregable/` sin validación explícita de Enrique.
- Antes de un cambio grande, explicar qué se hará. Al terminar, resumir qué cambió y cómo verificarlo.
- Cuando Enrique corrija una salida, registrarlo en `bitacora-ia.md` (material para D8).

## Git
- Prohibido ejecutar comandos de git que modifiquen estado: add, commit, amend, checkout, stash, reset, rebase, merge, push. Los commits los hace Enrique.
- Permitido solo lectura: status, log, diff.
- Prohibido incluir firmas de coautor o menciones de herramientas en mensajes de commit.