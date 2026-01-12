import random

mock_quest = [
    {
        "id": 1,
        "name": "FizzBuzz",
        "description": "Schreibe eine Funktion fizzbuzz(n), die alle Zahlen von 1 bis n durchgeht. Für jede Zahl gilt: Wenn sie durch 3 teilbar ist, gib 'Fizz' aus. Wenn sie durch 5 teilbar ist, gib 'Buzz' aus. Wenn sie durch 3 und 5 teilbar ist, gib 'FizzBuzz' aus. Andernfalls gib die Zahl selbst zurück.",
        "difficulty": "easy",
        "topic": "conditions_and_loops",
        "example_input": 15,
        "example_output": "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz",
        "testcases": [
            {"input": 3, "expected_output": "Fizz"},
            {"input": 5, "expected_output": "Buzz"},
            {"input": 15, "expected_output": "FizzBuzz"}
        ]
    },
    {
        "id": 2,
        "name": "Sum of Numbers",
        "description": "Schreibe eine Funktion sum_numbers(numbers), die eine Liste von Positiven Zahlen erhält und die Summe aller Zahlen zurückgibt.",
        "difficulty": "easy",
        "topic": "lists_and_loops",
        "example_input": [1, 2, 3, 4],
        "example_output": 10,
        "testcases": [
            {"input": [1, 2, 3], "expected_output": 6},
            {"input": [5, 10, 15], "expected_output": 30},
            {"input": [2, 4, 6, 8], "expected_output": 20}
        ]
    }
]


def get_quest(quest_id: int | None = None) -> dict:
    if quest_id is None:
        return random.choice(mock_quest)

    for quest in mock_quest:
        if quest["id"] == quest_id:
            return quest

    raise ValueError(f"quest with id {quest_id} not found")
