import matplotlib.pyplot as plt #http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
import numpy as np


#Create some data to plot
   #Create time series data
t = np.arange(0.0, 2.0, 0.01) # This creates a numpy array (much more efficient then list) from 0 to 2 every .01
s_t = np.sin(2*np.pi*t) # This takes the sin of t
s_t2 = 2*np.sin(2*np.pi/0.5*t + 1.0)

   #Create pie data
data = [33,24,15,11,7,11,1]
labels = ['Fresh','Soph','Jun','Sen','Masters','Phd','Profs']
explode = [0,0,0,0,.25,0,.25]

#Make plots
   #Line plot
   # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot(t,s_t,color = 'green', linestyle='--',label='Plot1') 
plt.plot(t,s_t2,color = '#F08000', linewidth=2,marker = 'o',label='Plot2')
plt.axis([0,1.5,-3,3]) #xmin,xmax,ymin,ymax
plt.xlabel('Time [s]',fontsize=14, color=[0,1,1])
plt.ylabel('Amplitude [m]')
plt.title('Example of how to plot')
plt.grid(True)
plt.text(.52, 2.2, 'Interesting point')
plt.legend(loc=1, fontsize=16)
plt.xticks([0,.3,.6,.9,1.2,1.5],['Zero','Point3','Point6','Point9','1Point2','1Point5'])

plt.show()

#Make 2 plots on the same figure
plt.figure(1, figsize=(5,5))
plt.subplot(1,4,1) #y,x,pick which one
plt.plot(t,s_t)
plt.xlabel('Time [s]',fontsize=14, color=[0,1,1])

plt.subplot(1,4,2) #y,x,pick which one
plt.fill(t,s_t2)
plt.xlabel('Time [s]',fontsize=14, color=[0,1,1])

plt.subplot(1,4,3) #y,x,pick which one
plt.plot(t,s_t)

plt.subplot(1,4,4) #y,x,pick which one
plt.plot(t,s_t)
plt.xlabel('Time [s]',fontsize=14, color=[0,1,1])


plt.show()

# Make two error bar graphs
plt.figure(2)
plt.subplot(2,1,1) #y,x,pick which one
plt.errorbar(t,s_t,yerr=s_t*s_t)

plt.subplot(2,1,2) #y,x,pick which one
plt.errorbar(t,s_t,xerr=.05, yerr=0.05)
plt.show()

# Make histogram, bar graph, and pie cart
plt.figure(3)
plt.subplot(1,3,1)
plt.hist(s_t,bins=5, alpha=.7, normed=True)
plt.hist(s_t2,bins=5, alpha=.7, normed=True)
plt.title('Histogram!')

plt.subplot(1,3,2)
plt.bar(range(0,5,1),s_t[0:5], 0.35, color='black', yerr = s_t[0:5]*s_t[0:5])
plt.bar(np.arange(0,5,1) + 0.35 ,s_t2[0:5], 0.35, color='red', yerr = s_t2[0:5]-1.5)
plt.ylabel('Info')
plt.title('Example of bar plot')
plt.xticks(np.arange(0,5,1) + 0.35,['First','Second','Third','Fourth','Fifth'])

plt.subplot(1,3,3)
plt.pie(data,explode = explode, labels=labels, shadow=True, startangle=90)
plt.title('% of people in class', bbox={'facecolor':'.9', 'pad' :10})
plt.axis('equal')
plt.subplots_adjust(wspace=.5, hspace=.5)
plt.suptitle('All the graphs')

plt.show()

