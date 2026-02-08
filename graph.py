import matplotlib.pyplot as plt
marks=[]
i=0
subjects=["Tamil","English","Maths","Science","Social"]
while i<5:
    marks.append(int(input("Enter Marks =")))
    i=i+1
for j in range(len(marks)):
    print("{}.{} Mark = {}".format(j+1,subjects[j],marks[j]))
plt.pie(marks,labels = subjects,autopct = "%.2f")
plt.show()
