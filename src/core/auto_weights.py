# src/core/auto_weights.py
def night_optimize_weights(memory):
    for name in memory.weights:
        if name in memory.archive:
            memory.weights[name] = max(1.0, memory.weights[name] - 0.2)
        else:
            memory.weights[name] = min(memory.weights[name] + 0.05, 10.0)
