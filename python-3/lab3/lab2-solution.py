import random

# Lab 1: Function with Multiple Return Values
def divide(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

# Lab 2: Function Arguments and Return Values
def calculate_area(length, width):
    area = length * width
    return area

# Lab 3: Variable-Length Arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

# Lab 4: Keyword and Positional-Only Arguments
def format_message(msg, /, *, uppercase=False):
    if uppercase:
        return msg.upper()
    return msg

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

# 8. Print numbers from 200 to 2 in descending order
def print_descending_numbers():
    for i in range(200, 1, -1):
        print(i)

# 9. Print multiples of 7 between 1 and 100
def print_multiples_of_7():
    for i in range(7, 101, 7):
        print(i)

# 10. Input numbers until negative and print sum
def sum_until_negative():
    sum = 0
    while True:
        try:  # Handle potential ValueError if input is not an integer
            num = int(input("Enter a number: "))
            if num < 0:
                break
            sum += num
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("The sum of the numbers is:", sum)

# 11. Calculate factorial
def calculate_factorial():
    while True: # loop for invalid input
        try:
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Factorial is not defined for negative numbers. Try again.")
                continue # go back to start of the loop
            break # exit when valid input is given
        except ValueError:
            print("Invalid input. Please enter an integer.")

    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is:", factorial)


# 12. Lucky number guessing game
def play_guessing_game():
    def generate_lucky_numbers():
        lucky_numbers = []
        while len(lucky_numbers) < 5:
            num = random.randint(2, 49)
            if num not in lucky_numbers:
                lucky_numbers.append(num)
        return lucky_numbers

    attempts = 0
    best_attempts = float('inf')  # Initialize with infinity
    while True:  # Outer loop for restarting the game if needed
        lucky_numbers = generate_lucky_numbers()
        attempts = 0
        guessed_numbers = set() # keep track of guessed numbers

        while lucky_numbers:
            try:
                guess = int(input("Guess a number: "))
                if guess < 2 or guess > 49:
                    continue  # Skip invalid input
                attempts += 1

                if guess in guessed_numbers:
                    print("You already guessed that number. Game Over!")
                    return # Exit the game due to duplicate guess
                guessed_numbers.add(guess)


                if guess in lucky_numbers:
                    lucky_numbers.remove(guess)

            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue # go to next iteration of inner loop

        if attempts < best_attempts:
            best_attempts = attempts

        if attempts <= 20:
            print("Congratulations! You guessed all the lucky numbers in", attempts, "attempts.")
            print("Best attempts:", best_attempts)
            break  # Exit the game if successful within 20 attempts
        else:
            print("Too many attempts. Restarting the game.")


# --- Main execution ---
if __name__ == "__main__":
    # Example usage (uncomment to test each part)
    # print(divide(10, 3))
    # print(calculate_area(5, 10))
    # print(sum_all(1, 2, 3, 4, 5))
    # print(format_message("hello", uppercase=True))
    # print(most_frequent(["apple", "banana", "apple", "orange", "banana", "apple"]))
    # print(first_unique_char("loveleetcode"))
    # print_descending_numbers()
    # print_multiples_of_7()
    # sum_until_negative()
    # calculate_factorial()
    play_guessing_game()