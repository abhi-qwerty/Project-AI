from schemas.game_state_schema import GameState, VALID_MOVES


def validate_move(state: GameState, move: str):
    """
    Intent understanding + validation.
    Does not mutate state.
    """

    if not move:
        return {"is_valid": False, "normalized": None, "reason": "Empty move."}

    normalized = move.strip().lower()

    if normalized not in VALID_MOVES:
        return {
            "is_valid": False,
            "normalized": None,
            "reason": "Invalid move. Use rock, paper, scissors, bomb.",
        }

    if normalized == "bomb" and state.user_bomb_used:
        return {
            "is_valid": False,
            "normalized": None,
            "reason": "Bomb already used once this game.",
        }

    return {"is_valid": True, "normalized": normalized, "reason": None}
