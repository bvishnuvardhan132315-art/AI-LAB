initial_state = {"At_A"}

goal = "At_C"
actions = [
    {
        "name": "Move A to B",
        "pre": {"At_A"},
        "add": {"At_B"},
        "delete": {"At_A"}
    },
    {
        "name": "Move B to C",
        "pre": {"At_B"},
        "add": {"At_C"},
        "delete": {"At_B"}
    }
]
def find_action(goal):
    for action in actions:
        if goal in action["add"]:
            return action

    return None
def make_plan(goal, state, plan):
    # Goal is already true
    if goal in state:
        return True

    # Find an action that can achieve the goal
    action = find_action(goal)

    if action is None:
        return False

    # First achieve the action's preconditions
    for condition in action["pre"]:
        if not make_plan(condition, state, plan):
            return False

    # Perform the action
    state.difference_update(action["delete"])
    state.update(action["add"])
    plan.append(action["name"])

    return True
state = initial_state.copy()
plan = []

make_plan(goal, state, plan)

print("Plan:")
for step in plan:
    print(step)
