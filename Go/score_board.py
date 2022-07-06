from PyQt5 import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QWidget, QLabel, \
    QPushButton, QTextEdit, QDialog, QFrame  # TODO import additional Widget classes as desired
from PyQt5.QtCore import pyqtSlot
from piece import Piece


class ScoreBoard(QDockWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''inicia la interfaz de usuario del tablero de puntuación'''
        self.resize(250, 250)
        self.setFixedWidth(250)
        self.center()
        self.setWindowTitle('Tablero de Puntuacion.')
        # crear un widget para contener otros widgets
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()

        # crear dos etiquetas que serán actualizadas por señales
        self.instructions = QLabel("Instrucciones\n 1. Haga clic en cualquier lugar" 
                                   "\n para colocar una piedra"
                                   "\n 2. Presiona P para pasar. \n 3. Presiona R para reiniciar el Juego")

        self.label_turn = QLabel("Turno Actual: ")
        self.label_clickLocation = QLabel("Ubicacion: ")
        self.label_timeRemaining = QLabel("Tiempo Restante: ")
        self.label_PrisonersBlack = QLabel("Prisioneros tomados por Negro: ")
        self.label_PrisonersWhite = QLabel("Prisioneros tomados por Blanco: ")
        self.label_TerritoriesBlack = QLabel("Territorios tomados por Negros: ")
        self.label_TerritoriesWhite = QLabel("Territorios tomados por Blancos: ")
        col = QColor(Qt.white)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(20, 20, 100, 100)

        self.mainWidget.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.instructions)
        self.mainLayout.addWidget(self.label_turn)
        self.mainLayout.addWidget(self.frm)
        # self.mainLayout.addWidget(self.passbutton)
        self.mainLayout.addWidget(self.label_clickLocation)
        self.mainLayout.addWidget(self.label_timeRemaining)
        self.mainLayout.addWidget(self.label_PrisonersBlack)
        self.mainLayout.addWidget(self.label_PrisonersWhite)
        self.mainLayout.addWidget(self.label_TerritoriesBlack)
        self.mainLayout.addWidget(self.label_TerritoriesWhite)

        self.setWidget(self.mainWidget)
        self.show()

    def center(self):
        '''centers the window on the screen, you do not need to implement this method'''

    def make_connection(self, board):
        '''Metodo que maneja una señal enviada desde la clase de tablero'''
        # when the clickLocationSignal is emitted in board the setClickLocation slot receives it
        board.clickLocationSignal.connect(self.setClickLocation)
        # when the updateTimerSignal is emitted in the board the setTimeRemaining slot receives it
        board.updateTimerSignal.connect(self.setTimeRemaining)
        # when the updatePrionersSignal is emitted in the board the updatePrisoners slot receives it
        board.updatePrionersSignal.connect(self.updatePrisoners)
        board.updateTerritoriesSignal.connect(self.updateTerritories)
        board.showNotificationSignal.connect(self.displaynotification)
        board.displaychangeturnSignal.connect(self.updateturn)

    @pyqtSlot(str)  # comprueba para asegurarse de que la siguiente ranura está recibiendo un argumento del tipo 'int
    def setClickLocation(self, clickLoc):
        '''actualiza la etiqueta para mostrar la ubicación del click'''
        self.label_clickLocation.setText("Ubicacion:\n" + clickLoc)
        # print('slot ' + clickLoc)

    @pyqtSlot(int)
    def setTimeRemaining(self, timeRemainng):
        '''actualiza la etiqueta de tiempo restante para mostrar el tiempo restante'''
        update = "Tiempo Restante:" + str(timeRemainng)
        self.label_timeRemaining.setText(update)

    def updateturn(self, Piece):
        if (Piece == 1):
            self.label_turn.setText("Turno Actual: Blanco")
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % QColor(Qt.white).name())
        elif (Piece == 2):
            self.label_turn.setText("Turno Actual: Negro")
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % QColor(Qt.black).name())

    def updatePrisoners(self, n, Player):
        if (Player == Piece.Black):
            update = "Prisioneros tomados por negros: " + n
            self.label_PrisonersBlack.setText(update)

        elif (Player == Piece.White):
            update = "Prisioneros tomados por blancos: " + n
            self.label_PrisonersWhite.setText(update)


    def updateTerritories(self, n, Player):
        if (Player == Piece.Black):
            update = "Territorios tomados por negros: " + n
            self.label_TerritoriesBlack.setText(update)

        elif (Player == Piece.White):
            update = "Territorios tomados por blancos: " + n
            self.label_TerritoriesWhite.setText(update)


    def passevent(self):
        print("Pass clicked")


    def displaynotification(self, message):
        dlg = QDialog(self)
        dlg.setFixedWidth(300)

        dlg.setWindowTitle("Notificacion!")
        self.modallayout = QVBoxLayout()
        # self.modallayout.resize(200, 200)
        self.modallayout.addWidget(QLabel(message))
        dlg.setLayout(self.modallayout)
        dlg.exec_()
