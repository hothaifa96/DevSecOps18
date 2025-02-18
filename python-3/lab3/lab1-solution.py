תשובות לשיעורי בית
1. מתי כדאי להשתמש ב-range בלולאת for?

כאשר רוצים לחזור על קטע קוד מספר מוגדר של פעמים.
כאשר יש צורך באינדקס מספרי של האיבר בלולאה.
כאשר רוצים ליצור רצף של מספרים.
2. כיצד אפשר להגדיר range עם קפיצות? כיצד אפשר להגדיר range עם מספרים בסדר יורד?

קפיצות: ניתן להשתמש בפרמטר השלישי של range כדי להגדיר את גודל הקפיצה. לדוגמה, range(0, 10, 2) ייצור רצף של מספרים: 0, 2, 4, 6, 8.
סדר יורד: ניתן להשתמש בפרמטר השלישי של range עם ערך שלילי כדי ליצור רצף של מספרים בסדר יורד. לדוגמה, range(10, 0, -1) ייצור רצף של מספרים: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1.
3. כיצד אפשר לייצר list מתוך range?

ניתן להשתמש בפונקציה list() כדי להמיר אובייקט range לרשימה. לדוגמה:

Python

my_list = list(range(1, 6))  # my_list יהיה שווה ל [1, 2, 3, 4, 5]
4. מדוע יש צורך בלולאות מסוג while ו-do-while?

while: כאשר מספר החזרות על הלולאה אינו ידוע מראש ותלוי בתנאי שצריך להתקיים.
do-while: כאשר רוצים לבצע את הלולאה לפחות פעם אחת, ורק לאחר מכן לבדוק את התנאי.
5. מה ההבדל בין לולאת while לבין לולאת do-while?

while: התנאי נבדק לפני ביצוע גוף הלולאה. אם התנאי לא מתקיים, גוף הלולאה לא יבוצע כלל.
do-while: גוף הלולאה מבוצע לפחות פעם אחת, ורק לאחר מכן התנאי נבדק.
6. כיצד אפשר בפייטון לממש לולאת do-while?

ניתן לדמות לולאת do-while בפייטון על ידי שימוש בלולאת while אינסופית ושבירה ממנה באמצעות הפקודה break.

Python

while True:
    # do something
    if condition:
        break
7. מה ההבדל בין break לבין continue? מדוע כדאי להשתמש ב-continue?

break: יוצא מהלולאה לחלוטין.
continue: מדלג על האיטרציה הנוכחית של הלולאה וממשיך לאיטרציה הבאה.
מדוע כדאי להשתמש ב-continue?

כאשר רוצים לדלג על איבר מסוים בלולאה מבלי לצאת מהלולאה לחלוטין.
כאשר יש תנאי שצריך להתקיים כדי לבצע איטרציה מסוימת, ואם התנאי לא מתקיים רוצים לדלג על האיטרציה.
תוכניות
8. תוכנית להדפסת מספרים מ-200 עד 2 בסדר יורד
Python

for i in range(200, 1, -1):
    print(i)
9. תוכנית להדפסת כפולות של 7 בין 1 ל-100
Python

for i in range(7, 101, 7):
    print(i)
10. תוכנית לקליטת מספרים עד לקלט שלילי והדפסת סכום
Python

sum = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    sum += num
print("The sum of the numbers is:", sum)
11. תוכנית לחישוב עצרת
Python

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is:", factorial)
12. תוכנית משחק ניחוש מספרי מזל
Python

import random

def generate_lucky_numbers():
    lucky_numbers = []
    while len(lucky_numbers) < 5:
        num = random.randint(2, 49)
        if num not in lucky_numbers:
            lucky_numbers.append(num)
    return lucky_numbers

def play_guessing_game():
    lucky_numbers = generate_lucky_numbers()
    attempts = 0
    while lucky_numbers:
        guess = int(input("Guess a number: "))
        if guess < 2 or guess > 49:
            continue
        attempts += 1
        if guess in lucky_numbers:
            lucky_numbers.remove(guess)
        # אתגר 1: אם המשתמש ניחש פעמיים את אותו המספר - צא מהלולאה
        # אתגר 2: אם לקח למשתמש יותר מ-20 ניחושים - חזור שוב על הלולאה
    print("Congratulations! You guessed all the lucky numbers in", attempts, "attempts.")

play_guessing_game()