#Logica del juego. Tiene todas las posiciones 

class Board: 

    def __init__(self, filename):
        self.matrix = []
        file = open(filename, "r")
        self.walls = []
        self.boxes = []
        self.goals = []
        self.player = None

        self.fill_board(file)
        print(self.walls)

    def fill_board(self, file):
        lines = [line.strip("\n") for line in file if line != "\n"]
        x = 0
        y = 0
        for line in lines:
            x = 0
            for char in line:
                if(char == "#"):
                    self.walls.append((x,y))
                elif char == "^":
                    self.player = (x,y)
                elif char == "o":
                    self.goals.append((x,y))
                elif char == "x":
                    self.boxes.append((x,y))
                x += 1
            y += 1


Board('map.txt')

    