from __future__ import annotations
import enum
import re
from dataclasses import dataclass
from functools import cached_property

WINNING_PATTERNS = (
    "???......", # row 1
    "...???...", # row 2
    "......???", # row 3
    "?..?..?..", # col 1
    ".?..?..?.", # col 2
    "..?..?..?", # col 3
    "?...?...?", # diag 135 degree
    "..?.?.?..", # diag 45 degree
)

class Mark(str, enum.Enum):
    CROSS = "X"
    NAUGHT = "O"
    
    @property
    def other(self)->Mark:
        return Mark.NAUGHT if self is Mark.CROSS else Mark.CROSS
        
@dataclass(frozen=True)
class Grid:
    cells:str = " " * 9
    
    def __post_init__(self) -> None:
        if not re.match(r"^[\sXO]{9}$", self.cells):
            raise ValueError("Must contain 9 cells of: X, O, or space")
    
    @cached_property
    def x_count(self) -> int:
        return self.cells.count("X")
    @cached_property
    def o_count(self) -> int:
        return self.cells.count("O")
    @cached_property
    def empty_count(self) -> int:
        return self.cells.count(" ")
    
    def print_grid(self) -> None:
        print(self.cells[:3], self.cells[3:6], self.cells[6:], sep='\n')

@dataclass(frozen=True)
class Move:
    player_mark : Mark
    cell_index : int
    before_state : GameState
    after_state : GameState

@dataclass(frozen=True)
class GameState:
    grid : Grid
    starting_player_mark : Mark = Mark("X")
    
    @cached_property
    def current_player_mark(self) -> Mark:
        if self.grid.x_count == self.grid.o_count:
            return self.starting_player_mark
        else:
            return self.starting_player_mark.other
    @cached_property
    def game_not_started(self) -> bool:
        return self.grid.empty_count == 9
    
    @cached_property
    def game_over(self) -> bool:
        return self.winner is not None or self.tie
    
    @cached_property
    def game_ongoing(self) -> bool:
        return not self.game_over and not self.game_not_started
    
    @cached_property
    def tie(self) -> bool:
        return self.winner is None and self.grid.empty_count == 0
    
    @cached_property
    def winner(self) -> Mark | None:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return mark
        return None
    
    @cached_property
    def winning_cells(self) -> list[int]:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace("?", mark), self.grid.cells):
                    return [
                        match.start()
                        for match in re.finditer(r"\?", pattern)
                    ]
        return []
    

griddy = Grid("XXXOOOOOX")  
gs = GameState(grid=griddy)
print(f'{gs.game_over},{gs.game_not_started},{gs.game_ongoing}, {gs.tie}, {gs.winner}', gs.winning_cells)
gs.grid.print_grid()
