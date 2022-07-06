from piece import Piece
from stone import Stone


class GameLogic():

    print("Game Logic Object Created")
    # Agrega código aquí para administrar la lógica de tu juego
    turn = Piece.Black
    Xpos = 0
    Ypos = 0
    boardArray = 0
    whiteprisoners = 0
    blackprisoners = 0
    whiteterritories = 0
    blackterritories = 0


    def updateparams(self,boardArray,xpos,ypos):
        #Actualizar las variables actuales
        self.Xpos = xpos
        self.Ypos = ypos
        self.boardArray=boardArray


    def checklogic(self,boardArray,xpos,ypos):
        #Actualizar las variables actuales
        self.Xpos = xpos
        self.Ypos = ypos
        self.boardArray=boardArray


    def checkvacant(self):
        #Comprobar si el puesto está vacante o no
        if self.boardArray[self.Ypos][self.Xpos].Piece==Piece.NoPiece :
            return True
        else :
            return False


    def changeturn(self):
        # Función para intercambiar turnos
        print("turn changed")
        if self.turn == Piece.Black:
            self.turn = Piece.White
        else:
            self.turn = Piece.Black


    def placestone(self):
       # Función para colocar la piedra en el tablero
        if self.turn == Piece.Black:
            self.boardArray[self.Ypos][self.Xpos].Piece = Piece.Black
        else:
            self.boardArray[self.Ypos][self.Xpos].Piece = Piece.White

        print("Liberties = " + str(self.boardArray[self.Ypos][self.Xpos].liberties) + "x pos = " + str(
            self.boardArray[self.Ypos][self.Xpos].x) + "y pos = " + str(self.boardArray[self.Ypos][self.Xpos].y))


    def updateLiberties(self):
        #Actualizar las libertades de todas las piedras disponibles
        count = 0
        for row in self.boardArray :
            for cell in row :
                count=0
                if cell.Piece != Piece.NoPiece :
                    Stonecolor=cell.Piece

                    if cell.getup(self.boardArray) != None and (cell.getup(self.boardArray).Piece == Stonecolor or cell.getup(self.boardArray).Piece == Piece.NoPiece) :
                        count=count+1
                    if cell.getright(self.boardArray) != None and (cell.getright(self.boardArray).Piece == Stonecolor or cell.getright(self.boardArray).Piece == Piece.NoPiece) :
                        count=count+1
                    if cell.getleft(self.boardArray) != None and (cell.getleft(self.boardArray).Piece == Stonecolor or cell.getleft(self.boardArray).Piece == Piece.NoPiece) :
                        count=count+1
                    if cell.getdown(self.boardArray) != None and (cell.getdown(self.boardArray).Piece == Stonecolor or cell.getdown(self.boardArray).Piece == Piece.NoPiece) :
                        count=count+1
                    cell.setLiberties(count)


    def updatecaptures(self):
        # Actualizar las capturas de todo el tablero, es decir, eliminar todas las piedras a las que les quedan 0 libertades
        for row in self.boardArray :
            for cell in row :
                if(cell.liberties==0 and cell.Piece != Piece.NoPiece):
                    if(cell.Piece== Piece.Black):
                        self.whiteprisoners=self.whiteprisoners+1
                        self.boardArray[cell.y][cell.x]=Stone(Piece.NoPiece,cell.x,cell.y)
                        print("Black Stone Captured at x: "+str(cell.x) + ", y: "+str(cell.y))
                        return "Black Stone Captured at x: "+str(cell.x) + ", y: "+str(cell.y)
                    elif(cell.Piece== Piece.White):
                        self.blackprisoners=self.blackprisoners+1
                        self.boardArray[cell.y][cell.x] = Stone(Piece.NoPiece, cell.x, cell.y)
                        print("White Stone Captured at x: " + str(cell.x) + ", y: " + str(cell.y))
                        return "White Stone Captured at x: " + str(cell.x) + ", y: " + str(cell.y)


    def updatecaptures2(self):
        # Función para verificar si alguna de las piedras vecinas de la ubicación actual tiene 0 libertades restantes, si es así, entonces captúrelas
        if self.boardArray[self.Ypos][self.Xpos].getup(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getup(self.boardArray).liberties == 0 and self.boardArray[self.Ypos][
                self.Xpos].getup(self.boardArray).Piece != Piece.NoPiece :

            return self.capturePiece(self.Xpos,self.Ypos-1)
        elif  self.boardArray[self.Ypos][self.Xpos].getright(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getright(self.boardArray).liberties == 0 and self.boardArray[self.Ypos][
                self.Xpos].getright(self.boardArray).Piece != Piece.NoPiece :
            return self.capturePiece(self.Xpos+1, self.Ypos)
        elif  self.boardArray[self.Ypos][self.Xpos].getleft(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getleft(self.boardArray).liberties == 0 and self.boardArray[self.Ypos][
                self.Xpos].getleft(self.boardArray).Piece != Piece.NoPiece :
            return self.capturePiece(self.Xpos-1, self.Ypos)
        elif  self.boardArray[self.Ypos][self.Xpos].getdown(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getdown(self.boardArray).liberties == 0 and self.boardArray[self.Ypos][
                self.Xpos].getdown(self.boardArray).Piece != Piece.NoPiece :
            return self.capturePiece(self.Xpos, self.Ypos+1)


    def capturePiece(self,xpos,ypos):
        # Captura una pieza en la posición dada
        if self.boardArray[ypos][xpos].Piece == 1:  # Si la pieza es Blanca.
            self.blackprisoners = self.blackprisoners + 1
            self.boardArray[ypos][xpos] = Stone(Piece.NoPiece, xpos, ypos)
            return "White Stone Captured at x: " + str(xpos) + ", y: " + str(ypos)

        else:  # Si la pieza es Negra.
            self.whiteprisoners = self.whiteprisoners + 1
            self.boardArray[ypos][xpos] = Stone(Piece.NoPiece, xpos, ypos)
            return "Black Stone Captured at x: " + str(xpos) + ", y: " + str(ypos)


    def checkforSuicide(self):
        oppositeplayer=Piece.NoPiece
        if self.turn==Piece.Black :
            oppositeplayer=Piece.White
        else :
            oppositeplayer =Piece.Black
        count=0
        # Cuenta las posiciones vecinas para piedras opuestas o nulos (final del tablero)
        if self.boardArray[self.Ypos][self.Xpos].getup(self.boardArray) == None or self.boardArray[self.Ypos][self.Xpos].getup(self.boardArray).Piece == oppositeplayer :
            count=count+1
        if self.boardArray[self.Ypos][self.Xpos].getleft(self.boardArray) == None or self.boardArray[self.Ypos][self.Xpos].getleft(self.boardArray).Piece == oppositeplayer :
            count = count + 1
        if self.boardArray[self.Ypos][self.Xpos].getright(self.boardArray) == None or self.boardArray[self.Ypos][self.Xpos].getright(self.boardArray).Piece == oppositeplayer :
            count = count + 1
        if self.boardArray[self.Ypos][self.Xpos].getdown(self.boardArray) == None or self.boardArray[self.Ypos][self.Xpos].getdown(self.boardArray).Piece == oppositeplayer :
            count = count + 1

        if(count==4) : # this means all side are of opposite color or end of board
            # now checking if any of the neighbours have a single liberty, if they do then by placing this stone, their liberties would turn to zero so it wont be suicide
            if self.boardArray[self.Ypos][self.Xpos].getup(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getup(self.boardArray).liberties == 1:
                return False
            if self.boardArray[self.Ypos][self.Xpos].getleft(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getleft(self.boardArray).liberties == 1:
                return False
            if self.boardArray[self.Ypos][self.Xpos].getright(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getright(self.boardArray).liberties == 1:
                return False
            if self.boardArray[self.Ypos][self.Xpos].getdown(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getdown(self.boardArray).liberties == 1:
                return False
            return True
        else :
            return False


    def getBlackPrisoner(self):
        return str(self.blackprisoners)


    def getWhitePrisoner(self):
        return str(self.whiteprisoners)


    def getBlackTerritories(self):
        return str(self.blackterritories)


    def getWhiteTerritories(self):
        return str(self.whiteterritories)


    def updateTeritories(self):
        # Actualizar las posiciones actuales ocupadas por cada jugador
        countb = 0
        countw = 0
        for row in self.boardArray:
            for cell in row:
                if cell.Piece == Piece.Black:
                    countb = countb + 1
                elif cell.Piece == Piece.White:
                    countw=countw+1
        self.whiteterritories=countw
        self.blackterritories=countb


    def getScore(self,Piece):
        if Piece==2:
            return self.blackterritories+self.blackprisoners
        else:
            return self.whiteterritories+ self.whiteprisoners









