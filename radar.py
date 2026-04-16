def analyze(prompt):
    length = len(prompt)

    return {
        "path_valid": length > 0,
        "constraint_ok": length > 5,
        "paths": 2 if "or" in prompt else 1,
        "tension": "HIGH" if "?" in prompt else "LOW"
    }
