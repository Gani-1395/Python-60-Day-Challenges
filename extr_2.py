course = {
    "c1": 1,
    "c2": 2,
    "c3": 3,
}
x = list(course.items())
marks = [value for _, value in x for _ in range(10)]
for i in marks:
    print(i)
