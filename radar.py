def analyze(prompt):
    # 🔥 這裡才是理火核心（先做最簡版）
    
    return {
        "length": len(prompt),
        "has_unknown": "unknown" in prompt,
        "structure_ok": len(prompt) > 10
    }
