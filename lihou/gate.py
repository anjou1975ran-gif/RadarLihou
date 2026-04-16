
def evaluate(prompt):
    if len(prompt) < 10:
        return "HOLD"
    elif "unknown" in prompt:
        return "STOP"
    return "PASS"
