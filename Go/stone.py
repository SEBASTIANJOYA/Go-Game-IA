from piece import Piece

class Stone(object):
    Piece = Piece.NoPiece
    liberties = 0
    x = -1
    y = -1


    def __init__(self, Piece,x,y):  # Constructor Inicializando Variables
        self.Piece = Piece
        self.liberties = 0
        self.x = x
        self.y = y

    def getPiece(self): # Metodo que retorna la pieza
        return self.Piece


    def getLiberties(self): # Metodo que retorna la libertad
        return self.liberties


    def setLiberties(self,liberties):   # Metodo para establecer libertades
        self.liberties =liberties


    def getup(self,boardArray):
        if self.y == 0:
            return None
        else :
            return boardArray[self.y-1][self.x] # Mueve la coordenada y hacia arriba


    def getright(self,boardArray):
        if self.x == 6:
            return None
        else :
            return boardArray[self.y][self.x+1] # Mover la coordenada x a la derecha


    def getleft(self,boardArray):
        if self.x == 0:
            return None
        else :
            return boardArray[self.y][self.x-1] # Mover la coordenada x a la izquierda

    def getdown(self,boardArray):
        if self.y == 6:
            return None
        else :
            return boardArray[self.y+1][self.x] # mover la coordenada y hacia abajo


