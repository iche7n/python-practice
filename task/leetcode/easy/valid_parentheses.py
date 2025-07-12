"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

def valid_parentheses(s: str):
    characters_list = {
        0: "(",
        1: ")",
        2: "{",
        3: "}",
        4: "[",
        5: "]"
    }

    result = []

    for i in s:
        for key, value in characters_list.items():
            if value == i:
                result.append(key)

    if 1 in result:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    valid_parentheses("()")