from jovian.pythondsa import evaluate_test_cases


"""
LINEAR SEARCH ALGORITHM

1. Create a variable position = 0
2. Check whether the number at index position in cards equals query
3. If it does, position is the answer and can be returned from the function
4. If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position
5. If the number was not found, return -1
"""


def locate_cards(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position

        position += 1

        if position == len(cards):
            return -1
    return -1

tests = []

# query occurs in the middle
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 2, 1, 0],
        'query': 7
    },
    'output': 3
})

# query occurs at last
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 2, 1, 0],
        'query': 1
    },
    'output': 7
})

# query occurs first
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# is the only element
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# is not in the list
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# list is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# repeating numbers
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# repeating query
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

# locate_cards(**tests[0]['input']) == tests[0]['output']
# for test in tests:
#     var = locate_cards(**test['input']) == test['output']
#     print(var)


evaluate_test_cases(locate_cards, tests)
