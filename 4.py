import matplotlib.pyplot as plt

x=[15,16,17,18,19,20,21]
y=[]

plt.plot(x,y, marker='0', linestyle='--', color='red', label='temperature')
plt.title("Daily temperature trend")
plt.xlabel('Time(hour)')
plt.ylabel('Temperature (c)')
plt.legend()
plt.grid(True)
plt.savefig('./results/linechart.png')