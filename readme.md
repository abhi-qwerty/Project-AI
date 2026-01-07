# Rock–Paper–Scissors–Plus — AI Referee Chatbot

This project implements a **minimal Rock–Paper–Scissors–Plus game referee** using the **Google ADK framework**. The agent validates moves, tracks game state, enforces rules, and responds conversationally while the user plays against the bot.

## 🎮 Game Rules

* **Format:** Best of 3 rounds.
* **Valid Moves:** `rock`, `paper`, `scissors`, `bomb`.
* **The "Bomb" Rule:**
    * Beats everything (Rock, Paper, and Scissors).
    * Can only be used **once** per player per game.
    * *Bomb vs Bomb* results in a **Draw**.
* **Penalties:** Invalid input wastes a round (automatic loss for that turn).
* **Termination:** The game automatically ends after Round 3.

---

## 🧠 Architecture Overview

The system is intentionally small but cleanly separated into distinct components:

### 1. State Management
* **File:** `services/state_service.py`
* **Function:** Centralized `GameStateService`.
* **Details:** Stores rounds, scores, bomb usage, and history. Allows safe reset and access to ensure state persists strictly between turns.

### 2. Schemas
* **File:** `schemas/game_state_schema.py`
* **Function:** Defines the `GameState` dataclass.
* **Contains:**
    * Current round & Max rounds
    * User & Bot scores
    * Move history
    * Bomb usage flags
    * Game-over flag & Final Winner

### 3. Tools
Tools are explicit ADK-style utilities that perform state mutation and validation.

| Tool Name | Responsibility |
| :--- | :--- |
| `validate_move` | Normalizes input and validates moves against rules. |
| `resolve_round` | Applies game logic, determines winner, and updates scores. |
| `bot_select_move` | Chooses bot moves and manages bot's bomb usage logic. |

### 4. Agent
* **File:** `agent/adk_game_agent.py`
* **Responsibilities:**
    * Interpret user intent (read move text).
    * Call validation tools.
    * Call round-resolution tools.
    * Format user-facing responses.
    * Stop the game cleanly when finished.

### 5. Runner / CLI Loop
* **File:** `main.py`
* **Function:**
    * Prints rules (concise, ≤ 5 lines).
    * Loops for user input.
    * Ends automatically.
    * *Constraint:* No web APIs, databases, servers, or UI frameworks.

---

## ✅ Why This Meets Requirements

- [x] **Best‑of‑3 enforced**
- [x] **Bomb only once per player**
- [x] **Invalid input wastes a round**
- [x] **State persists between turns**
- [x] **Game ends automatically**
- [x] **Clear round feedback** (Round #, Moves, Winner, Score)
- [x] **Final winner reported**
- [x] **Clean separation** of intent, logic, and response formatting
- [x] **Uses Google ADK agents + tools**
- [x] **No external APIs or databases**

---

## ⚖️ Tradeoffs & Future Improvements

**Tradeoffs Made:**
* Simple random bot (not strategic).
* In‑memory session service only (no database).
* CLI instead of chat UI (per constraints).

**Future Improvements:**
* Add configurable game length.
* Improve bot strategy.
* Add test coverage.
* Support restarting games gracefully.
* Persist history across sessions.

---

## ▶️ How to Run

1.  Clone the repository.
2.  Run the main script:

```bash
python main.py