import matplotlib.pyplot as plt

Fruits = ["Apple","Banana","Orange","Mango","Grapes"]
Quantity = [10,20,15,25,30]

plt.bar(Fruits,Quantity ,width=0.4 ,color="green",align="center",edgecolor="black",linewidth=3,linestyle=":")

plt.title("Fruits vs Quantity",fontsize=15)
plt.xlabel("Fruits" ,fontsize=15)
plt.ylabel("Quantity" ,fontsize=15)
plt.show()