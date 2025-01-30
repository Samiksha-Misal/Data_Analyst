import matplotlib.pyplot as plt

subjects = ["DSA","web development","SAD","AI"]
Marks = [90,80,85,95]
plt.pie(Marks, labels=subjects, startangle=90)
plt.title("Marks in different subject")
plt.show()