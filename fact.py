import matplotlib.pyplot as plt
marks = []
i = 0
subject = ["tamil","ENg","maths","sci","soci"]
while i < 5:
  marks.append(int(input("enter the marks ")))

  i += 1
for j in range (len(marks)):
  print("{}.{} Marks ={}".format(j+1,subject[j],marks[j]))
plt.pie(marks,labels=subject,autopct="%.2f%%")
plt.show()
