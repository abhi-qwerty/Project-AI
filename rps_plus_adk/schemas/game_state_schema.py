from dataclasses import dataclass, field
from typing import Optional, List

VALID_MOVES = ["rock", "paper", "scissors", "bomb"]


@dataclass
class GameState:
    round_number: int = 1
    max_rounds: int = 3

    user_score: int = 0
    bot_score: int = 0

    user_move_history: List[str] = field(default_factory=list)
    bot_move_history: List[str] = field(default_factory=list)

    user_bomb_used: bool = False
    bot_bomb_used: bool = False

    game_over: bool = False
    winner: Optional[str] = None
