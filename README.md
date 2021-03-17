# TP1-SIA 2021 1er C.

Proyecto hecho en Python para encontrar soluciones a mapas del juego `sokoban` utilizando métodos de búsqueda informados y desinformados.
```
Integrantes:
- Eugenia Sol Piñeiro
- Scott Lin
- Nicolás Comerci Wolcanyik
```

### Requerimientos previos
- Python 3
- PC compatible con OpenGL 3.3+

### Instalación
1. Como primera instancia clonar el proyecto en algun directorio de preferencia:
```bash
$> git clone https://github.com/scottlin19/TP1-SIA
```
2. Dentro de la carpeta del proyecto, instalar los módulos requeridos que se encuentran en requirements.txt:
```bash
$> pip3 install -r requirements.txt
```

### Configuración y ejecución
Dentro del archivo `config.json`, que está en directorio raíz del proyecto, se encuentran todos los parámetros posibles de configuración:

- "algorithm": algoritmo de búsqueda a utilizar (BFS, DFS, IDDFS, A*, GGS, IDA*).
- "checkDeadlocks": booleano para indicar si se deben verificar los estados muertos o no.
- "heuristic": heurística a utilizar (solo tiene efecto en los métodos informados). Las posibilidades son:
    - "simple_lower_bound" (suma de las distancias manhattan mínimas de las cajas a los goals)
    - "player_boxes" (Suma de las distancias entre jugador y cada caja)
    - "free_goals" (Cantidad de goals que quedan libres)
    - "player_box_goal" (Suma de las distancias entre jugador y caja + caja y goal mas cercano)
    - "minimum_matching_lower_bound" (suma de las distancias manhattan mínimas de las cajas a los goals con asignación)
- "map": directorio del mapa a utilizar (Ej: "maps/easy.txt")

Una vez configurados todos los parámentros, ejecutar el siguiente comando para correr el proyecto:
```bash
$> python3 sokoban.py
```
Al encontrar una solución se abrirá una ventana monstrando los pasos que se deben seguir para llegar a la misma, junto con las métricas solicitadas en la consigna.
![window](https://lh3.googleusercontent.com/uk-x8IAORDmxe_WRFjRDl3w6MlBTO8avlU5yu9aAYU-mZrX0n7nbC1AEbkY39bMz6H4hkgr5cRAR-0FhEbgy6NLNNFF9Kb28TLHJ6ei4GPBbC5QFhDVir9MuIFxmHBEyeQiO4Fcjwg=w2400)
![console](https://lh3.googleusercontent.com/KhIsVPl5HGEINSx_vnG6Tb9LMYvgqwtuArz7w_H5yhpsz2leEDXg9BZmoIyMqPYq6L3m_10rbJrUS-DGjRG0ug4gaveEoP2P6mfX3Qmr7u_a-r7etPxXjK3FOZeYuc_TzHmJmT3wrw=w2400)

### Posibles configuraciones de ejecución: `config.json`
Mapa 'soko1' con algoritmo BFS y sin chequeo de deadlocks:
```json
{
    "algorithm": "BFS", 
    "checkDeadlocks": false,
    "heuristic": "simple_lower_bound",
    "map": "maps/soko1.txt"
}
```

Mapa 'soko1' con A*, heurística simple lower bound y con chequeo de deadlocks:
```json
{
    "algorithm": "A*", 
    "checkDeadlocks": true,
    "heuristic": "simple_lower_bound",
    "map": "maps/soko1.txt"
}
```

### Mapas personalizados de Sokoban
Dentro de la carpeta maps es posible crear archivos `.txt` para representar mapas a solucionar. Los símbolos utilizados son:

- `#`: Representa un bloque de pared
- `x`: Representa una caja
- `o`: Representa un goal
- `^`: Representa al jugador
- `%`: Representa una caja encima de un goal
- `$`: Representa un jugador encima de un goal
