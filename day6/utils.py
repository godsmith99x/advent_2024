from enum import Enum
from typing import List, Set, Tuple

class Lab:
    def __init__(self, lines: List[str]) -> None:
        self.row_count = len(lines) - 1
        self.col_count = len(lines[0]) - 1
        self.guard_initial_position = tuple()
        self.obstructions = set()
        
        for row, line in enumerate(lines):
            for index, char in enumerate(line):
                char = char.strip()

                if char == "#":
                    self.obstructions.add((row, index))
                
                if char == "^":
                    self.guard_initial_position = (row, index)



class Guard:
    class Direction(Enum):
        UP = (-1, 0)
        RIGHT = (0, 1)
        DOWN = (1, 0)
        LEFT = (0, -1)

    def __init__(self, lab: Lab) -> None:
        self.direction = Guard.Direction.UP
        self.positions = set()
        self.positions.add(lab.guard_initial_position) 
        self.current_position = lab.guard_initial_position
        # self.next_position = self._update_next_position()
        self.next_position = tuple(a + b for a, b in zip(self.current_position, self.direction.value))

        if self._next_in_bounds(lab):
            self.touring = True
        else:
            self.touring = False

    def _update_next_position(self) -> None:
        self.next_position = tuple(a + b for a, b in zip(self.current_position, self.direction.value))

    def _next_in_bounds(self, lab: Lab) -> bool:
        return 0 <= self.next_position[0] <= lab.row_count and 0 <= self.next_position[1] <= lab.col_count
    
    def _turn_right(self) -> None:
        match self.direction:
            case Guard.Direction.UP:
                self.direction = Guard.Direction.RIGHT
            case Guard.Direction.RIGHT:
                self.direction = Guard.Direction.DOWN
            case Guard.Direction.DOWN:
                self.direction = Guard.Direction.LEFT
            case Guard.Direction.LEFT:
                self.direction = Guard.Direction.UP
    
    def move(self, lab: Lab) -> None:
        if not self._next_in_bounds(lab): 
            self.touring = False
            return
        
        if self.next_position in lab.obstructions:
            self._turn_right()
            self._update_next_position()
            return
        
        self.current_position = self.next_position
        self.positions.add(self.current_position)
        self._update_next_position()
