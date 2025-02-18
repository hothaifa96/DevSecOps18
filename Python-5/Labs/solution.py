# Lab 1: Function with Multiple Return Values
def divide(x, y):
    quotient = x // y  # Integer division to get the quotient
    remainder = x % y   # Modulo operator to get the remainder
    return quotient, remainder

quotient, remainder = divide(10, 3)
print(quotient, remainder)  # Output: 3 1


# Lab 2: Function Arguments and Return Values
def calculate_area(length, width):
    area = length * width
    return area

print(calculate_area(5, 10))  # Output: 50


# Lab 3: Variable-Length Arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print(sum_all())               # Output: 0


# Lab 4: Keyword and Positional-Only Arguments
def format_message(msg, /, *, uppercase=False): # / marks positional-only, * marks keyword-only
    if uppercase:
        return msg.upper()
    return msg

print(format_message("hello"))          # Output: hello
print(format_message("hello", uppercase=True))  # Output: HELLO


# Challenge 1: Most Frequent Word
def most_frequent(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_frequent_word = None
    max_count = 0
    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_word = word
    return most_frequent_word

print(most_frequent(["apple", "banana", "apple", "orange", "banana", "apple"]))
# Output: apple


# Challenge 2: Find the First Non-Repeating Character
def first_unique_char(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i
    return -1

print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("loveleetcode"))  # Output: 2
print(first_unique_char("aabb"))  # Output: -1