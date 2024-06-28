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

**Update 28/06**

He experimentado en agrupar las funciones por clases. Estos experimentos se ven reflejados en el archivo "classes.py". He logrado de manera efectiva recoger en una clase las funciones que se encargan de recolectar datos. Sin embargo, se me ha complicado agrupar el resto de funciones por clases. Considero que debo familiarizarme más con Python para que este proyecto se me facilite aún más. 
Tras los intentos, he vuelto al módulo de funciones y he agregado una función para terminar de procesar las combinadas. Por lo tanto, hay una función que agrupa de forma aleatorio los diccionarios de apuestas simples en pares, y hay otra función que calcula la cuota combinada y creo tuples de tríos con las dos apuestas más la combinada. 
Si no me equivoco, se podría proceder a crear un backtester piloto para ensayar la estrategia piloto. No obstante, creo que voy a enfocarme en profundizar mis conocimientos/habilidades de Python.