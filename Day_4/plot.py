import matplotlib.pyplot as plt

#plot:1
days = ["Sunday","Monday","Tuesday","Wednesday","Thusday","Friday","Saturday"]
sales = [160,150,140,145,175,165,180]
price = [174,160,185,150,160,175,190]

plt.subplot(1,2,1)
plt.plot(days, sales, marker="s",  ms = 5, mec="black", mfc="Green", linestyle="-", color="Green", linewidth="1", label = "Sales")
plt.plot(days,price, marker="o",  ms = 5, mec="black", mfc="Lightcoral", linestyle="-", color="Lightcoral", linewidth="1", label = "Price")

plt.legend(fontsize = 8)
plt.title("Sales over Days", fontsize=15, color="Black", loc="center", fontweight = "bold")
plt.xticks(rotation = 45)
plt.xlabel("Days", fontsize=11, color = "grey")
plt.ylabel("Sales & Price", fontsize = 11, color = "grey")
plt.grid(axis = 'both', color="grey", linestyle='-' ,linewidth=0.5, alpha  = 0.4)


#plot:2
subjects = ["DBMS","CC","OS","AIML","DSA","Python","TOC"]
marks = [75,80,65,74,90,84,70]

plt.subplot(1,2,2)
plt.plot(subjects ,marks, marker="s",  ms = 5, mec="black", mfc="orange", linestyle="-", color="orange", linewidth="1", label = "Marks")

plt.legend(fontsize = 8, frameon = False, loc = "upper left")
plt.title("Marks in different subjects", fontsize=15, color="black", loc="center", fontweight = "bold")
plt.xlabel("Subjects", fontsize=11, color = "grey")
plt.ylabel("Marks", fontsize = 11, color = "grey")
plt.grid(axis = 'both', color="grey", linestyle='-' ,linewidth=0.5, alpha = 0.4)
plt.show()