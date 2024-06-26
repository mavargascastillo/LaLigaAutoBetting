# LaLiga Automated Betting
## Repository geared towards developing a systematic strategy for betting in LaLiga

**Update 25/06**

Estoy creando una estrategia piloto para poder desarrollar un backtester. Una vez tenga la estrategia completada, puedo centrarme en el backtester para determinar la rentabilidad de la estrategia. 

Por el momento, he creado ==cuatro funciones distintas==, cuyas funciones son las siguientes:
- Extraer información sobre los goles del archivo excel
- Extraer información sobre los partidos del archivo excel
- Asignar un valor a cada apuesta del grupo "apuestas de mitades"
- Utilizar las tres funciones para reiterar sobre los 10 partidos que cada jornada contiene

Ahora mismo falta construir una función para crear las combinadas de apuestas. Una vez lo tenga, creo que ya puedo proceder a crear el backtester.

**Update 26/06**

He terminado de refinar la estrategia piloto. Ahora mismo las funciones son capaces de elegir la apuesta con la puntuación más alta de cada partido, y agruparlas en grupos de dos. Falta crear una última función que combine estas dos apuestas simples en una única combinada. Alternativamente, de esto puede encargarse el backtester, aunque creo que será más efectivo el primer método. También he limpiado las funciones, es decir, he incluido descripciones detalladas, comentarios, e intentado utilizar nombres de argumentos y variables lo menos confusos posibles.