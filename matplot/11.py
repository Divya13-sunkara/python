import matplotlib.pyplot as plt
courses=['Python','Java','C++','JavaScript']
students=[50, 40, 30, 20]
explode = (0.1, 0,0.2, 0) 
plt.pie(students, labels=courses, explode=explode, autopct='%2.1f%%')
plt.title("Course Enrollment")
plt.show()