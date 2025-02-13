https://adventofcode.com/2024/day/2

# Día 2: Informes de Nariz Roja
Afortunadamente, el primer lugar que los Historiadores quieren buscar no está muy lejos de la oficina del Historiador Jefe.

Aunque la planta de fusión/fisión nuclear del Reno de Nariz Roja no parece contener señales del Historiador Jefe, los ingenieros que están allí corren hacia ti tan pronto como te ven. Aparentemente, todavía hablan de la vez que salvaron a Rudolph mediante una síntesis molecular a partir de un solo electrón.

Se apresuran a añadir que, dado que ya estás aquí, agradecerían mucho tu ayuda para analizar algunos datos inusuales del reactor Red-Nosed. Te giras para comprobar si los Historiadores te están esperando, pero parece que ya se han dividido en grupos que están buscando en cada rincón de la instalación. Te ofreces a ayudar con los datos inusuales.

Los datos inusuales (la entrada de su rompecabezas) consisten en muchos informes , un informe por línea. Cada informe es una lista de números llamados niveles que están separados por espacios. Por ejemplo:
```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```
Estos datos de ejemplo contienen seis informes, cada uno con cinco niveles.

Los ingenieros están tratando de determinar qué informes son seguros. Los sistemas de seguridad del reactor de Nariz Roja solo pueden tolerar niveles que aumentan o disminuyen gradualmente. Por lo tanto, un informe solo se considera seguro si se cumplen las dos condiciones siguientes:

Los niveles son todos crecientes o todos decrecientes.
Dos niveles adyacentes difieren en al menos uno y como máximo en tres.
En el ejemplo anterior, los informes se pueden considerar seguros o inseguros verificando estas reglas:

* `7 6 4 2 1`: Es seguro porque los niveles disminuyen en 1 o 2.
* `1 2 7 8 9`: Inseguro porque `2 7` es un aumento del 5.
* `9 7 6 2 1`: Inseguro porque `6 2` es una disminución de 4.
* `1 3 2 4 5`: Inseguro porque `1 3` está aumentando pero `3 2` está disminuyendo.
* `8 6 4 4 1`: Inseguro porque `4 4` no es ni un aumento ni una disminución.
* `1 3 6 7 9`: Es seguro porque los niveles aumentan de 1, 2 o 3.

Entonces, en este ejemplo, 2 los informes están seguros.

Analice los datos inusuales de los ingenieros. ¿Cuántos informes son seguros?

Para jugar, identifícate a través de uno de estos servicios: