# Chess

from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import cpu_count as threads
from enum import Enum

class PieceType(Enum):
    """Enum class storing the value of the piece."""
    PAWN = 1
    KNIGHT = 3
    BISHOP = 3
    ROOK = 5
    QUEEN = 9
    
class Piece():
    """Class for defining attributes of a chess piece."""
    def __init__(self, piece_type: PieceType, color: str, column: str, row: str):
        """Initialises a chess piece with information
        Parameters:
        piece_type - Enum object of PieceType
        color - string representation of which color the piece is. Can
                be "black" or "white"
        column - a letter between (a - h) inclusive (str)
        row - a number between (1 - 8) inclusive (str)"""
        self.__piece_type = piece_type
        self.set_color(color)
        self.set_position(column, row)

    @property
    def type(self):
        """What kind of piece it is"""
        return self.__piece_type

    @property
    def color(self):
        """Which color the piece belongs to"""
        return self.__color

    @property
    def position(self):
        """String tuple representation of the piece's position in chess notation"""
        return self.__column, self.__row

    def set_position(self, column: str, row: str):
        """Set the position of the piece"""
        # Type check
        if not isinstance(column, str): raise TypeError("Expected str for column.")
        if not isinstance(row, str): raise TypeError("Expected str for row.")

        # Check the position is valid.
        if not ("a" <= column <= "h"): raise ValueError("Expected value between a and h (inclusive) for column:", column)
        if not ("1" <= row <= "8"): raise ValueError("Expected value between 1 and 8 (inclusive) for row:", row)

        # Update position.
        self.__column = column
        self.__row = row

    def set_color(self, color: str):
        """Sets the color of the piece to the given color"""
        # Type check
        if not isinstance(color, str): raise TypeError("Expected str for color.")

        # Value check.
        if not color in ["white", "black"]: raise ValueError("Expected 'white' or 'black' for color:" + color)

        # Update color.
        self.__color = color

        
        
