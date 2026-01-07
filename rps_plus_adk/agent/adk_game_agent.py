from google.adk.agents import Agent
from pydantic import PrivateAttr

from services.state_service import GameStateService
from tools.validate_move import validate_move
from tools.resolve_round import resolve_round


class RPSPlusAgent(Agent):
    name: str = "rps_plus_referee"

    _state_service: GameStateService = PrivateAttr(default_factory=GameStateService)

    def handle_message(self, message: str):
        state = self._state_service.get_state()

        if state.game_over:
            return "Game already finished. Restart the program to play again."

        validation = validate_move(state, message)

        # invalid wastes round
        if not validation["is_valid"]:
            state.round_number += 1

            if state.round_number > state.max_rounds:
                state.game_over = True
                return f"Invalid move: {validation['reason']}\nGame over."

            return f"Invalid move: {validation['reason']}"

        # valid → resolve round
        result = resolve_round(state, validation["normalized"])

        # game ended
        if result["game_over"]:
            return (
                f"Round {state.round_number - 1}\n"
                f"You: {result['user_move']} | Bot: {result['bot_move']}\n"
                f"Round winner: {result['round_winner']}\n\n\n"
                f"Final Score — You {result['user_score']} : Bot {result['bot_score']}\n"
                f"Game result: {result['final_winner']}"
            )

        # game continues
        return (
            f"Round {state.round_number - 1}\n"
            f"You: {result['user_move']} | Bot: {result['bot_move']}\n"
            f"Winner: {result['round_winner']}\n"
            f"Score — You {result['user_score']} : Bot {result['bot_score']}"
        )
