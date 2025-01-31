import matplotlib.pyplot as plt

Subjects = ["DSA","web development","OS","AI"]
Mark = [65,70,80,75,90]
Marks = [90,80,85,95]

myexplode = [0.2,0,0,0]
mycolors = ["yellow","pink","green","blue"]
c = ["magenta","orange","red","yellow","green"]

plt.pie(Marks, labels=Subjects, startangle=90, explode=myexplode, shadow=True, colors=mycolors, autopct="%0.2f%%", radius=1.2
    , labeldistance=1.3, textprops={"fontsize":15}, counterclock=False, wedgeprops={"linewidth":4,"edgecolor":"grey"})

plt.pie(Mark, radius=0.5, colors=c, startangle=90, autopct="%0.2f%%")
plt.title("Marks in different Subject", fontsize=18)
plt.legend(title = "Four Subjects:", loc=1, bbox_to_anchor=(1.5, 1))
plt.show()