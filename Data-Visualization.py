#Data Visualization 
"""Data Visualization is the presentataion of data in a pictorial or graphical formate 
"""
# Process 
"""
1-Visualize
2-Analyse
3-Document Insight
4-Transform Data Set


"""

# Matplolib


"""Matplotlib is a python package used for 2D graphic """

#types of Plots 
"""
1-Bar Graph- 
2-Histograms
3-Scatter Plot 
4-Pie Plot 
5-Hexagonal Bin Plot 
6-Area Plot
"""

from matplotlib import pyplot as plt


# plt.plot([4,2,9],[45,5,1])
# here we give vlaue fist is x-axis and 2nd value is y-axis

# plt.plot([10,4,2],[8,5,3])
# plt.show()  
# this is used to show the blog 


##label to Graph 
# ploting with variable 

x=[5,8,10]
y=[12,15,6]
# draw the plot usign the variable as x and y 

plt.plot(x,y)

 # here we give the title and name to axis 
plt.title("info")
plt.ylabel("y axis")
plt.xlabel("X axis")
plt.show()


#sytle the graph  
#import sytle from matplotlib

from matplotlib import style

style.use("ggplot")


x2=[6,9,11]
y2=[6,15,7]

plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'b',label='line two',linewidth=5)

plt.title("Epic Info")
plt.ylabel("y axis")
plt.xlabel("x asix")


plt.legend()

plt.grid(True, color='k')
plt.show()
