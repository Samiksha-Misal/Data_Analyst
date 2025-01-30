import matplotlib.pyplot as plt

subjects = ["DSA","web development","SAD","AI"]
Marks = [90,80,85,95]

myexplode = [0.2,0,0,0]
mycolors = ["yellow","pink","green","blue"]

plt.pie(Marks, labels=subjects, startangle=90, explode=myexplode, shadow=True, colors=mycolors)
plt.title("Marks in different subject")
plt.legend(title = "Four Subjects:")
plt.show()