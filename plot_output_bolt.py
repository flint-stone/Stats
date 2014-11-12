#706:EvenScheduler:bolt_output_0,bolt_output_1,bolt_output_2,bolt_output_3,bolt_output_4,:star5-1-1411511789:3004
from pylab import *
import matplotlib.pyplot as plt
import sys

throughput_dict=dict()
time_dict=dict()
file = open(sys.argv[1], "r")
for line in file.readlines():
	data = line.strip().split(":")

	time = data[0]
	sched_type = data[1]
	topology = data[3]
	throughput = data[4]

	element_id = sched_type
	#print "{"+element_id+"}-->["+time+", "+throughput+"]"
	if ((element_id in throughput_dict) == False):
		throughput_dict[element_id]=[]
	if ((element_id in time_dict) == False):
		time_dict[element_id]=[]
	throughput_dict[element_id].append(int(throughput))
	time_dict[element_id].append(int(time))
file.close()	
for key in throughput_dict:
	print "{"+key+"}-->"
	print str(throughput_dict[key])
	print str(time_dict[key])
	print "\n"

	line1=plt.plot(time_dict[key], throughput_dict[key], label=key)
plt.xlabel("Time (s)")
plt.ylabel("Throughput-Tuples/10sec")
plt.grid()
#plt.legend([line1,line2], ["line1","line2"])
#plt.legend()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)
plt.show()

