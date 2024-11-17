import matplotlib as plt
x=[10,20,30,40,50,60,70]
y1=[10,40,30,50,60,20,70]
y2=[20,50,40,30,60,10,40]

plt.plot(x,y1,'g',linestyle='dashed')
plt.plot(x,y2,'r',linestyle='dashed')
plt.xlabel('Velocity')
plt.ylabel('Time')
plt.title('Velocity Time graph')
plt.show()