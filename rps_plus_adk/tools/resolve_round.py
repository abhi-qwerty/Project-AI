import random
from schemas.game_state_schema import GameState


def bot_select_move(state: GameState):
    """
    Bot may use bomb at most once.
    Weighted chance to use bomb once.
    """

    if not state.bot_bomb_used and random.random() < 0.25:
        state.bot_bomb_used = True
        return "bomb"

    return random.choice(["rock", "paper", "scissors"])


def resolve_round(state: GameState, user_move: str):
    """
    Pure game logic + state mutation.
    """

    bot_move = bot_select_move(state)

    # track histories
    state.user_move_history.append(user_move)
    state.bot_move_history.append(bot_move)

    # mark bomb usage immediately if played
    if user_move == "bomb":
        state.user_bomb_used = True

    # ------- outcome logic -------- #

    if user_move == "bomb" and bot_move == "bomb":
        round_winner = "draw"

    elif user_move == "bomb":
        round_winner = "user"
        state.user_score += 1

    elif bot_move == "bomb":
        round_winner = "bot"
        state.bot_score += 1

    else:
        if user_move == bot_move:
            round_winner = "draw"
        elif (
            (user_move == "rock" and bot_move == "scissors")
            or (user_move == "paper" and bot_move == "rock")
            or (user_move == "scissors" and bot_move == "paper")
        ):
            round_winner = "user"
            state.user_score += 1
        else:
            round_winner = "bot"
            state.bot_score += 1

    # advance round counter
    state.round_number += 1

    # -------- game end logic ---------- #

    if state.round_number > state.max_rounds:
        state.game_over = True

        if state.user_score > state.bot_score:
            state.winner = "user"
        elif state.bot_score > state.user_score:
            state.winner = "bot"
        else:
            state.winner = "draw"

    return {
        "user_move": user_move,
        "bot_move": bot_move,
        "round_winner": round_winner,
        "user_score": state.user_score,
        "bot_score": state.bot_score,
        "game_over": state.game_over,
        "final_winner": state.winner,
    }
