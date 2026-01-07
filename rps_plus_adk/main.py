from agent.adk_game_agent import RPSPlusAgent


def main():
    print("Rock–Paper–Scissors–Plus")
    print("- Best of 3")
    print("- Moves: rock, paper, scissors, bomb")
    print("- Bomb beats everything once")
    print("- Invalid input wastes a round")

    agent = RPSPlusAgent()

    while True:
        user_text = input("\nYour move: ")

        reply = agent.handle_message(user_text)
        print(reply)

        if "Game result" in reply:
            break


if __name__ == "__main__":
    main()
