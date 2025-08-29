if __name__ == "__main__":
    N = 5  # Grid size
    X = 10  # Battery capacity
    entry_point = (0, 0)
    gold_location = (3, 3)  # Gold is located at this room
    charging_station = (0, 0)

    env = GridEnvironment(N, entry_point, gold_location, charging_station)
    agent = Agent(env, X)

    agent.explore()

    print(f"Total steps taken: {agent.steps_taken}")
