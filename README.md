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
-- "simple_lower_bound" (suma de las distancias manhattan mínimas de las cajas a los goals)
-- "player_boxes"
-- "free_goals"
-- "player_box_goal"
-- "minimum_matching_lower_bound"
- "map": directorio del mapa a utilizar (Ej: "maps/easy.txt")

Una vez configurados todos los parámentros, ejecutar el siguiente comando para correr el proyecto:
```bash
$> python3 sokoban.py
```
Al encontrar una solución se abrirá una ventana monstrando los pasos que se deben seguir para llegar a la misma, junto con las métricas solicitadas en la consigna.
![window](https://lh3.googleusercontent.com/6jvXxikz0UhPVEicgaW_Mcn4zCdLvdIIl2nrn9pI1I9Cxo8InspCCZZE7GDeqaYJFa3OBOp-GJzPQIlbDZnI7UmnoXCvSGBnDjI_Kb4oht4kqOvXROxZlXtXCfkDvMehosZY8hvRMQcKBUW0vnUqA9-i8DAngPdhT0Ium2GugH8pMaswmwjyeK0REmw7ake-Eflrkmu2gB1wUQKatiVfJjnjFAlzecol7RX34vTf6ulnk5GIw1Z7eG-OTu9RTeBqI5nLFpM6QeEWbaSk-OBV2aia0shGF_Bq32l8C7rDFH53xG0po88a7mSTrxOnu4PIr4qlgiTuIP_w86s3b1UY7BVvpG_v5Bt83M6F6B2iQaAt0yNWJveQkZvaGC1qv8je4nrZBJoF0rOVu87_2AcfnNy8H1w0GlCAKxkOEGBQ18z4Qa1p8ai3MWcgEP2u5Xy6ZhAFzQiXQHG2gqgMUI0zAPWuvfzD2B6StPmGaEJa1xci1jmZ91nRFcS1cOB7qXgdkcjBYB5-nDaxmNUqqnH5Lcq1ASXq1HbZhQi4zJ3BCOwRDGnjcYLE9C2YDKUlhGoFqJeIuYIy1XsVIafLQIyRoFYSC-FB1a490Pf0veWLAv_olREznW0Yzi6RaidqR3W4y6jGzUq6TksYgUAt86eQNG2GbzegD3BRjGeNyy9PKbaDj6HDcUeNe6oKtYzLufgs1h1ZWWy0BQjrUrSSJ96whHaR=w571-h196-no?authuser=0)
![console](https://lh3.googleusercontent.com/VjABcWLrTbNUMCeGHmZUwjAFai6MCQxRlxXQil0g0itd5_dbEpiuRojER_5waZQ-N-Tmg_Ci0YN-dsvc67LoizXVfl8JL6uN6et-h1MdlBIzWbPIyHTb_NDhamisPVRMqL2jbvV4aiJR7lwzWfOFM1uue3Xnt_be1fIEyx89NebaubSPVq5DoWbPQNsAe2dsR_LVeg79YQBxWBO0l3TmIOBHYbxae_ZTmaE5iZ2yrvtE3yH2WGe72PClANx1TlCjO51NWbllMHi7WJjqTt-r_RiNxKd6fqJXEMNIpyiMPHfuydnvMqxjlQNweNwAOCN8reMgdzp96qqssa_a5FU05T5R8XlCmoOVf3YooKdxgNfb5Qn3EkJp4MR2Brp0M3lI5tTNinKdEhjIYVx8qA6vr3f1tqLdmYd3p1Hd0BHa5lonBAUBV7yoIWtDf4Q_I5XpMHMTcoBGtOeTh4_vJ7ixiBw29pfFY9Hr3rbGAbXb-Hc9KnWr_2NTm3aIihnLm9ZNbm9p0g5ejYqg1yKjJxs4h_d0BXkVM7IbyJU8NEMntTHqsoYz8c_rYdYf7rsLLiruDT0MVr7FWoLWwGzWKyJw3tO6h2lz5L-bO-gkpA41NYq1ZLJUKCNaJYJV9C_OUgmddr0JGt7Bg4clZqK4mGhrxqToPrn5-oqwmo4mA1IAkW5ZRs2xFCyL4jK86l4yMuBsO9y4ZCyTI5pBTHWEGEn54HF_=w572-h183-no?authuser=0)

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
Dentro de la carpeta maps es posible crear archivos `.txt` para representar el mapas a solucionar. Los símbolos utilizados son:

- `#`: Representa un bloque de pared
- `x`: Representa una caja
- `o`: Representa un goal
- `^`: Representa al jugador
- `%`: Representa una caja encima de un goal
- `$`: Representa un jugador encima de un goal