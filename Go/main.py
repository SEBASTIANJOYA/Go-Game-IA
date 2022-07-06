import sys
import random

# 5x5 GO 
board_5x5= [
    7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 7, 
    7, 0, 0, 0, 0, 0, 7, 
    7, 0, 0, 0, 0, 0, 7, 
    7, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 
   
]

# 9x9 coordenadas
coords_5x5 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'XX', 
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'XX', 
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
]

# 9x9 GO 
board_9x9 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 9x9 coordenadas
coords_9x9 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
]

# 13x13 GO 
board_13x13 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 13x13 coordenadas.
coords_13x13 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A13','B13','C13','D13','E13','F13','G13','H13','J13','K13','L13','M13','N13','XX',
    'XX', 'A12','B12','C12','D12','E12','F12','G12','H12','J12','K12','L12','M12','N12','XX',
    'XX', 'A11','B11','C11','D11','E11','F11','G11','H11','J11','K11','L11','M11','N11','XX',
    'XX', 'A10','B10','C10','D10','E10','F10','G10','H10','J10','K10','L10','M10','N10','XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'K9', 'L9', 'M9', 'N9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'K8', 'L8', 'M8', 'N8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'K7', 'L7', 'M7', 'N7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'K6', 'L6', 'M6', 'N6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'K5', 'L5', 'M5', 'N5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'K4', 'L4', 'M4', 'N4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'K3', 'L3', 'M3', 'N3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'K2', 'L2', 'M2', 'N2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'K1', 'L1', 'M1', 'N1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
]

# 19x19 GO.
board_19x19 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

# 19x19 coordenadas
coords_19x19 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A19','B19','C19','D19','E19','F19','G19','H19','J19','K19','L19','M19','N19','O19','P19','Q19','R19','S19','T19','XX',
    'XX', 'A18','B18','C18','D18','E18','F18','G18','H18','J18','K18','L18','M18','N18','O18','P18','Q18','R18','S18','T18','XX',
    'XX', 'A17','B17','C17','D17','E17','F17','G17','H17','J17','K17','L17','M17','N17','O17','P17','Q17','R17','S17','T17','XX',
    'XX', 'A16','B16','C16','D16','E16','F16','G16','H16','J16','K16','L16','M16','N16','O16','P16','Q16','R16','S16','T16','XX',
    'XX', 'A15','B15','C15','D15','E15','F15','G15','H15','J15','K15','L15','M15','N15','O15','P15','Q15','R15','S15','T15','XX',
    'XX', 'A14','B14','C14','D14','E14','F14','G14','H14','J14','K14','L14','M14','N14','O14','P14','Q14','R14','S14','T14','XX',
    'XX', 'A13','B13','C13','D13','E13','F13','G13','H13','J13','K13','L13','M13','N13','O13','P13','Q13','R13','S13','T13','XX',
    'XX', 'A12','B12','C12','D12','E12','F12','G12','H12','J12','K12','L12','M12','N12','O12','P12','Q12','R12','S12','T12','XX',
    'XX', 'A11','B11','C11','D11','E11','F11','G11','H11','J11','K11','L11','M11','N11','O11','P11','Q11','R11','S11','T11','XX',
    'XX', 'A10','B10','C10','D10','E10','F10','G10','H10','J10','K10','L10','M10','N10','O10','P10','Q10','R10','S10','T10','XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'K9', 'L9', 'M9', 'N9', 'O9', 'P9', 'Q9', 'R9', 'S9', 'T9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'K8', 'L8', 'M8', 'N8', 'O8', 'P8', 'Q8', 'R8', 'S8', 'T8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'K7', 'L7', 'M7', 'N7', 'O7', 'P7', 'Q7', 'R7', 'S7', 'T7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'K6', 'L6', 'M6', 'N6', 'O6', 'P6', 'Q6', 'R6', 'S6', 'T6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'K5', 'L5', 'M5', 'N5', 'O5', 'P5', 'Q5', 'R5', 'S5', 'T5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'K4', 'L4', 'M4', 'N4', 'O4', 'P4', 'Q4', 'R4', 'S4', 'T4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'K3', 'L3', 'M3', 'N3', 'O3', 'P3', 'Q3', 'R3', 'S3', 'T3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'K2', 'L2', 'M2', 'N2', 'O2', 'P2', 'Q2', 'R2', 'S2', 'T2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
]

# Podemos buscar los tableros de diferentes tamaños ya sea 
# 9x9 - 13x13 - 15x15
BOARDS = {
    '5': board_5x5,
     '9': board_9x9,
    '13': board_13x13,
    '19': board_19x19
}

# Busqueda de coordenadas
COORDS = {
    '5': coords_5x5,
     '9': coords_9x9,
    '13': coords_13x13,
    '19': coords_19x19,
}

#Piedras
EMPTY = 0
BLACK = 1
WHITE = 2
MARKER = 4
OFFBOARD = 7
LIBERTY = 8

# Contar
liberties = []
block = []

# Tablero actual utilizado
board = None
coords = None

BOARD_WIDTH = 0
BOARD_RANGE = 0
MARGIN = 2

# filas marcadas
files = '     a b c d e f g h j k l m n o p q r s t'

# ASCII representacion de piedras
pieces = '.#o  bw +'

def print_board():
    # bucle sobre las filas del tablero
    for row in range(BOARD_RANGE):
        # bucle sobre las columnas del tablero
        for col in range(BOARD_RANGE):
            # cuadro inicial
            square = row * BOARD_RANGE + col
            
            # piedra inicial
            stone = board[square]
            
            # rango de impresion
            if col == 0 and row > 0 and row < BOARD_RANGE - 1:
                rank = BOARD_RANGE - 1 - row
                space = '  ' if len(board) == 121 else '   '
                print((space if rank < 10 else '  ') + str(rank), end='')
            
            # imprime el contenido
            print(pieces[stone] + ' ', end='')
        print()
    
    # notacion de impresion
    print(('' if len(board) == 121 else ' ') + files[0:BOARD_RANGE*2] + '\n')

# Metodo para establecer el tamaño
def set_board_size(command):
    # Definimos variables globales
    global BOARD_WIDTH, BOARD_RANGE, board, coords
    
    # Analiza el tamaño del tablero
    size = int(command.split()[-1])
    
    #Lanza error si el tamaño no es compatible 
    if size not in [5, 9, 13, 19]:
        print('? current board size not supported\n')
        return

    # Calcular el tamaño actual de la placa
    BOARD_WIDTH = size
    BOARD_RANGE = BOARD_WIDTH + MARGIN
    board = BOARDS[str(size)]
    coords = COORDS[str(size)]

# Metodo para contar libertades.
def count(square, color):
    # pieza inicial
    piece = board[square]
    if piece == OFFBOARD: return
    if piece and piece & color and (piece & MARKER) == 0:
        # guarda la coordenada de la pidera
        block.append(square)
    
        board[square] |= MARKER
        count(square - BOARD_RANGE, color) # walk north
        count(square - 1, color)           # walk east
        count(square + BOARD_RANGE, color) # walk south
        count(square + 1, color)           # walk west
    
    
    elif piece == EMPTY:
        # MARCA LIBERTADES
        board[square] |= LIBERTY
        
        # GUARDA LIBERTADES
        liberties.append(square)

# Metodo para eliminar las piedras capturadas
def clear_block():
    for captured in block: board[captured] = EMPTY

# Limpiar grupos
def clear_groups():
    # definir varibles globales
    global block, liberties
    
    # limpiar listas de bloques y libertades
    block = []
    liberties = []

# restauara el tablero antes de contar piedras
def restore_board():
    clear_groups()
    
    # desmarcar piedras.
    for square in range(BOARD_RANGE * BOARD_RANGE):
        # restore piece if the square is on board
        if board[square] != OFFBOARD: board[square] &= 3

# tablero limpiar.
def clear_board():
    clear_groups()
    
    for square in range(len(board)):
        if board[square] != OFFBOARD: board[square] = 0

# realiza el movimiento en el tablero
def set_stone(square, color):

    board[square] = color
    
    # maneja las capturas
    captures(3 - color)

# Metodo para generar el movimiento aleatorio
def make_random_move(color):
    # encontar una zona vacia al azar.
    random_square = random.randrange(len(board))
    while board[random_square] != EMPTY:
        random_square = random.randrange(len(board))
    
    # realiza el movimiento
    set_stone(random_square, color)
    
    # contar libertades
    count(random_square, color)
    
    # movimiento suicida
    if len(liberties) == 0:
        # restaurar tablero
        restore_board()
        
        # quitar la piedra
        board[random_square] = EMPTY
        
        # buscar otro movimiento
        try:
            # moviiento de retorno no suicida
            return make_random_move(color)
        except:
            # pasar el movimiento
            return '' 
    
    # restaura el tablero
    restore_board()
    
    # devuelve el movimiento
    return coords[random_square]

# Metodo para reproducir el juego
def play(command):
    #  Analiza el color
    color = BLACK if command.split()[0] == 'B' else WHITE
    if command.split()[-1] == 'pass': return
    
    # analiza el cuadrado 
    square_str = command.split()[-1]
    col = ord(square_str[0]) - ord('A') + 1 - (1 if ord(square_str[0]) > ord('I') else 0)
    row_count = int(square_str[1:]) if len(square_str[1:]) > 1 else ord(square_str[1:]) - ord('0')
    row = (BOARD_RANGE - 1) - row_count
    square = row * BOARD_RANGE + col

    set_stone(square, color)


def captures(color):
    # recorre el cuadrado
    for square in range(len(board)):
        
        piece = board[square]
        
        if piece == OFFBOARD: continue
        
        # piedra corresponde al color dado?
        if piece & color:
            # cuenta libertades
            count(square, color)
            
            # si no quedan libertades quita las piedras.
            if len(liberties) == 0: clear_block()
            
            # restaura el tablero
            restore_board()

# deteccion de bordes
def detect_edge(square):
    # recoorre en cuatro direcciones.
    for direction in [BOARD_RANGE, 1, -BOARD_RANGE, -1]:
        if board[square + direction] == OFFBOARD: return 1

    return 0


 
# generar movimiento
def genmove(color): 
    
    best_move = 0
    capture = 0
    save = 0
    defend = 0
    surround = 0
    # capturar el grupo del oponente
    for square in range(len(board)):
        # inicializa pieza
        piece = board[square]
    
        if piece & (3 - color):
            # cuenta las libertades para el grupo del oponente
            count(square, (3 - color))
            
            # si queda una sola libertad
            if len(liberties) == 1:
                # alamacena el movimiento de captura
                target_square = liberties[0]
                best_move = target_square
                capture = target_square
                break
            
            # restaura el tablero.
            restore_board()
            
    # Guarda grupo propio
    for square in range(len(board)):
        # inicializa la pieza
        piece = board[square]
        #coincide con el propio grupo
        if piece & (color):
            # cuenta las libertades para el propio grupo
            count(square, (color))
            
            # si solo queda una libertad
            if len(liberties) == 1:
                # almacena la pieza en esa liberta
                target_square = liberties[0]
                
                # deteccion de bordes
                if not detect_edge(target_square):
                    best_move = target_square
                    save = target_square
                    break
            
            # restaura el tablero
            restore_board()
 

    # Encontrar movimiento
    if best_move:
    
   
        # acciones defensa y ataque aleatorio
        random_action = random.randrange(2)
        
        #manejar las prioridades de la IA
        if not capture and not defend and not save: best_move = surround
        if not capture and not save and defend: best_move = defend if random_action else surround
        if not capture and not defend and save: best_move = save
        if capture: best_move = capture
        
        # hacer movimiento
        set_stone(best_move, color)
        
        # validar movimiento
        count(best_move, color)
        
        # contar las libertades almacenadas
        legal = len(liberties)
        
        # restaura el tablero
        restore_board()
        
        # movimiento suicida
        if not legal:
            # rompe piedra del tablero
            board[best_move] = EMPTY
            
            # considera un movimiento aleatorio en su lugar
            return make_random_move(color)
        
       
        return coords[best_move]

    # si se empieza con negro.
    return make_random_move(color)


def main():

    decision=True
    while True:
        command = input()      
        if 'tamaño' in command: set_board_size(command); print('=\n')
        elif 'limpiar' in command: clear_board(); print('=\n')
        elif 'jugar' in command: 
          while decision==True:
              in1=input("DIGITAR JUGADA : ") 
              if 'S' in in1:
                decision=False;
              else:
                play(in1); print('\n Movimiento Jugador = \n')
                print('='); print_board();
                print('\n Movimiento Maquina = '+genmove(WHITE)+'\n')
                print('='); print_board();  
        elif 'quit' in command: sys.exit()
        else: print('=\n') 
main()