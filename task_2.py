from collections import deque

def is_palindrome(test_string):
    cleaned_text = ''.join(char.lower() for char in test_string if char.isalnum())
    char_queue = deque(cleaned_text)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True

while True:
    test_string = input('Print your example: ')

    if test_string in ['exit', 'e']:
        break

    result = is_palindrome(test_string)

    if result:
        print(f'"{test_string}" is a palindrome.')
    else:
        print(f'"{test_string}" is NOT a palindrome.')
