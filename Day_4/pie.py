import matplotlib.pyplot as plt

subjects = ["DSA","web development","OS","AI"]
mark = [65,70,80,75,90]
Marks = [90,80,85,95]

myexplode = [0.2,0,0,0]
mycolors = ["yellow","pink","green","blue"]
c = ["magenta","orange","red","yellow","green"]

plt.pie(Marks, labels=subjects, startangle=90, explode=myexplode, shadow=True, colors=mycolors, autopct="%0.2f%%",radius=1.2
    ,labeldistance=1.3, textprops={"fontsize":15},counterclock=False,wedgeprops={"linewidth":4,"edgecolor":"grey"})

plt.pie(mark,radius=0.5,colors=c, startangle=90,autopct="%0.2f%%")
plt.title("Marks in different subject", fontsize=18, pad=20)
plt.legend(title = "Four Subjects:",loc=1,bbox_to_anchor=(1.5, 1))
plt.show()