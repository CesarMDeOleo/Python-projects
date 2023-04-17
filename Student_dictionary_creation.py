def process_students(student_list):
    updated_student_list = {} #creates the new dictionary
    for student, student_details in student_list.items():
        graduation = student_details[0] 
        grades = student_details[1]
        GPA = sum(grades) / len(grades) # calculate GPA
        if graduation in updated_student_list:
            updated_student_list[graduation].append((student, GPA))
        else:
            updated_student_list[graduation] = [(student, GPA)]
    return updated_student_list


student_list = {'Alice':(2023, [3.5, 2.9, 3.1, 3.8]), 'Bob':(2024, [3.0, 2.6]), 'Morgan':(2024, [2.8, 3.9, 3.7]), 'Tim':(2023, [2.5])}
print(process_students(student_list))