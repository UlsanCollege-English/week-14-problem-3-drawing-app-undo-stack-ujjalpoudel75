
## main.py
"""
HW03 — Drawing App Undo Stack

Implement simulate_history(actions) that applies "UNDO" commands using a stack
and returns the final list of actions.
"""


def simulate_history(actions):
    """
    Process a list of actions for a drawing app and apply UNDO behavior.

    :param actions: list of strings; "UNDO" means remove the most recent action
    :return: list of strings representing the remaining actions
    """
    stack = []
    for action in actions:
        if action == "UNDO":
            if stack:
                stack.pop()
        else:
            stack.append(action)
    return stack


if __name__ == "__main__":
    sample = ["DRAW line", "DRAW circle", "UNDO", "FILL blue", "UNDO", "UNDO"]
    print(simulate_history(sample))
