lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
_class = [lloyd, alice, tyler]
# Add your function below!
def average(n):
    total = 0
    total = sum(n)
    total = float(total)
    total /= len(n)
    return total

def get_average(student):
    total = 0
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    total = 0.1 * homework + 0.3 * quizzes + 0.6 * tests
    return total

def get_letter_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade
    
def get_class_average(students):
    results = []
    for student in _class:
        results.append(get_average(student))
    result = average(results)
    return result

print get_class_average(alice)