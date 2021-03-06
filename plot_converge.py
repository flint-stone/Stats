#706:EvenScheduler:bolt_output_0,bolt_output_1,bolt_output_2,bolt_output_3,bolt_output_4,:star5-1-1411511789:3004
from pylab import *
import matplotlib.pyplot as plt
import sys
import numpy as np

START1=400
END1=800
START2=1200
END2=1600

def mean(data):
    a = np.array(data)
    return np.mean(a)

def stdev(data):
    a=np.array(data)
    return np.std(a)

pre = dict()
post = dict()
strategies=[]
throughput_dict=dict()
time_dict=dict()
post_time_dict=dict()
convergence_dict=dict()

file = open(sys.argv[1], "r")
for line in file.readlines():
    data = line.strip().split(":")
   
    time = data[0]
    sched_type = data[1]
    topology = data[3]
    throughput = data[4]
    element_id = sched_type
    
    if (int(time) > START1 and int(time)<END1):
        if ((element_id in pre) == False):
            pre[element_id]=[]
        pre[element_id].append(int(throughput))
    elif(int(time) >START2 and int(time)<END2):
        if ((element_id in post) == False):
            post[element_id]=[]
            post_time_dict[element_id]=[]
        post[element_id].append(int(throughput))
        post_time_dict[element_id].append(int(time))

file.close()    

pre_avg=[]
pre_stdev=[]
post_avg=[]
post_stdev=[]
convergence=[]

print "Pre Rebalance avg:"
for key in pre:
    print key
    print pre[key]
    print key+" "+str(mean(pre[key]))+" "+str(stdev(pre[key]))
    pre_avg.append(mean(pre[key]))
    pre_stdev.append(stdev(pre[key]))
    strategies.append(key)
print "Post Rebalance avg:"
for key in post:
    print key
    print post[key]
    print key+" "+str(mean(post[key]))+" "+str(stdev(post[key]))
    m=mean(post[key])
    up=0
    down=0
    idx=0
    while up<=3 and down<=3:
        if (post[key][idx]>m):
            up=up+1
        else:
            down=down+1
        idx=idx+1
    post_avg.append(mean(post[key]))
    post_stdev.append(stdev(post[key]))
    convergence.append(post_time_dict[key][idx]-870)

fig, ax = plt.subplots()
index = np.arange(len(pre_avg))


bar_width = 0.5
opacity = 0.4
error_config = {'ecolor': '0.3'}


print str(len(pre_avg))+" "+str(len(pre_stdev))
print index

i=0;
j=0;
patterns = ('+','-', 'x','/','//','o','O','.','*','\\','\\\\')
print "convergence:"
print convergence
#rects1 = plt.bar(np.arange(11),tuple(convergence), bar_width,color=cm.jet(2.5*i/len(pre)),label=strategies,alpha=opacity)

#rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)
for key,pattern in zip(pre, patterns):
    print [0+i,10+i]
    rects1 = plt.bar(0+i,convergence[j], bar_width,
                 alpha=opacity,
                 color=cm.jet(2.5*i/len(pre)),
                 error_kw=error_config,
                 label=key,
				 hatch=pattern)
    i+=bar_width
    j=j+1

'''
patterns = ('+','-', 'x','/','//','o','O','.','*','\\','\\\\')
for key,pattern in zip(pre, patterns):
    print [0+i,10+i]
    rects1 = plt.bar([0+i,bar_width*(len(pre)+2)+i],[mean(pre[key]), mean(post[key])], bar_width,
                 alpha=opacity,
                 color=cm.jet(2.5*i/len(pre)),
                 yerr=[stdev(pre[key]), stdev(post[key])],
                 error_kw=error_config,
                 label=key,
				 hatch=pattern)
    i+=bar_width
'''
'''
rects1 = plt.bar([0,0.5,1,1.5,2.0,2.5,3,3.5], pre_avg, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=pre_stdev,
                 error_kw=error_config,
                 label='Pre-rebalance')
rects2 = plt.bar(index+10, post_avg, bar_width,
                 alpha=opacity,
                 color='g',
                 yerr=post_stdev,
                 error_kw=error_config,
                 label='post-rebalance')
'''

plt.ylabel('Convergence time')
plt.title('Post-balance Throughput Convergence')

plt.xlabel("strategies")
#http://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01),ncol=3, fancybox=True, shadow=True)

#plt.tight_layout()
plt.show()




