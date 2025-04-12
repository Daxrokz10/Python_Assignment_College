# Find the student with the highest marks.

dict_marks = {
    "John": 85,
    "Jane": 90,
    "Doe": 78
}
print(max(dict_marks, key=dict_marks.get))