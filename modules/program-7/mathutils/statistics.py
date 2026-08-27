"""Statistical operations module."""

def mean(data):
    if not data:
        raise ValueError("Data list cannot be empty.")
    return sum(data) / len(data)

def maximum(data):
    if not data:
        raise ValueError("Data list cannot be empty.")
    return max(data)

def minimum(data):
    if not data:
        raise ValueError("Data list cannot be empty.")
    return min(data)

