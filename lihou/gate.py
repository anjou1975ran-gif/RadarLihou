from .radar import analyze

def evaluate(prompt):
    r = analyze(prompt)

    if not r["path_valid"]:
        return "STOP"

    if not r["constraint_ok"]:
        return "HOLD"

    if r["paths"] == 1:
        return "EXPAND"

    if r["tension"] == "HIGH":
        return "DELAY"

    return "PASS"
