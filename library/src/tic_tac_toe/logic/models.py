from __future__ import annotations
import enum

class Mark(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"
    
    @property
    def other(self)->Mark:
        return Mark.NAUGHT if self is Mark.CROSS else Mark.CROSS
        
    
print(type(Mark.CROSS))
print(Mark.CROSS.value)
print(Mark.CROSS.value == 'X')
print(Mark.CROSS == "X")