# Read the file
students = []
try:
    with open('01_feladat.txt', 'r') as f:
        for line in f:
            name, score = line.strip().split(';')
            students.append({'name': name, 'score': int(score)})
except FileNotFoundError:
    print("Error: 01_feladat.txt not found.")
    exit()

# Calculate total score and average
total_score = sum(student['score'] for student in students)
average_score = total_score / len(students) if students else 0

# Count students with at least 60 points
count_above_60 = sum(1 for student in students if student['score'] >= 60)

# Find the best and weakest students
best_student = max(students, key=lambda x: x['score']) if students else None
weakest_student = min(students, key=lambda x: x['score']) if students else None

# Write results to a new file
with open('01_eredmeny.txt', 'w') as f:
    f.write(f"Total score: {total_score}\n")
    f.write(f"Average score: {average_score}\n")
    f.write(f"Number of students with at least 60 points: {count_above_60}\n")
    if best_student:
        f.write(f"Best student: {best_student['name']} ({best_student['score']} points)\n")
    if weakest_student:
        f.write(f"Weakest student: {weakest_student['name']} ({weakest_student['score']} points)\n")

print("Results written to 01_eredmeny.txt")