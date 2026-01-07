from schemas.game_state_schema import GameState


class GameStateService:
    """
    Holds and mutates persistent game state.
    """

    def __init__(self):
        self.state = GameState()

    def get_state(self) -> GameState:
        return self.state

    def reset(self):
        self.state = GameState()
