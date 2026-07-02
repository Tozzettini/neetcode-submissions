from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    if not scores:
        raise ValueError("score cannot be empty")
    best_name, high_score = scores[0]
    # iterate through the list
    for name, score in scores[1:]:
        if score > high_score:
            best_name = name
    return best_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
