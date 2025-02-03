import matplotlib.pyplot as plt

#plot:1
days = ["Sunday","Monday","Tuesday","Wednesday","Thusday","Friday","Saturday"]
sales = [160,150,140,145,175,165,180]
price = [174,160,185,150,160,175,190]

plt.subplot(1,2,1)
plt.plot(days, sales, marker="*",  ms = 15, mec="brown", mfc="pink", linestyle="dashed", color="green", linewidth="1")
plt.plot(days,price, marker="*",  ms = 15, mec="black", mfc="pink", linestyle="dashed", color="blue", linewidth="1")

plt.title("Sales over Days", fontsize=15, color="brown", loc="left")
plt.xlabel("Days", fontsize=15)
plt.ylabel("Sales & Price", fontsize=15)
plt.grid(axis = 'y', color="grey", linestyle='--' ,linewidth=0.5)


#plot:2
subjects = ["DBMS","CC","OS","AIML","DSA","Python","TOC"]
marks = [75,80,65,74,90,84,70]

plt.subplot(1,2,2)
plt.plot(subjects ,marks, marker="*",  ms = 15, mec="black", mfc="pink", linestyle="dashed", color="blue", linewidth="1")

plt.title("Marks in different subjects", fontsize=15, color="brown", loc="left")
plt.xlabel("Subjects", fontsize=15)
plt.ylabel("Marks", fontsize=15)
plt.grid(axis = 'y', color="grey", linestyle='--' ,linewidth=0.5)
plt.show()
