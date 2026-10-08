import matplotlib.pyplot as plt
courses=['Python','Java','C++','JavaScript']
students=[50, 40, 30, 20]
plt.pie(students, labels=courses, autopct='%2.1f%%')
plt.title("Course Enrollment")
plt.show()