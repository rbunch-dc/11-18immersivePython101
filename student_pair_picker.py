students = [
    'Rob',
    'Christopher',
    'Jim',
    'Jason',
    'Brian',
    'Brandon',
    'Zac',
    'JR',
    'Greg',
    'Ron',
    'Katie',
    'Sean',
    'Gbenga',
    'Khanh',
    'Connor',
    'Cody',
    'Michael',
    'Matt'
]

# Take the list "students" randomly pair 2
# students until all studetns have been used
import random
# 1. Grab a random index from the students list
# print len(students)
# 2. after printing, remove that student from the list 
# 3. Repeat until len(students) == 0

def get_student():
    # get a random student!
    rand_student_index = random.randint(0,len(students)-1)
    current_student = students[rand_student_index]
    # we have picked a student. Remove that value from the list
    students.remove(current_student)
    return current_student

while (len(students) > 0):
    student1 = get_student()
    student2 = get_student()
    print "%s is paired with %s" % (student1,student2)
    
