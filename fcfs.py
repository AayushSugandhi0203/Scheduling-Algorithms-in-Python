import pandas

datContent = [read.strip().split() for read in open("inputfcfs.dat").readlines()]



n = int(datContent[0][0])
j = 1

arrival = []
burst = []
priority = []
for i in range(0,n):
    a ,b,c = datContent[j][0] ,  datContent[j][1], datContent[j][2]
    a = int(a)
    b = int(b)
    c = int(c)
    arrival.append(a)
    burst.append(b)
    priority.append(c)
    j = j + 1
process_no = []
for i in range(0,n):
    process_no.append(i+1)
quantum = int(datContent[n + 1][0])
queue = int(datContent[n + 2][0])
zipp = zip(arrival,burst,process_no)
tag = sorted(list(zipp),key = lambda x:(x[0]))

  
exit_time = []
exit_time.append(tag[0][1])
j = 1
for i in range(1,n):
    j = tag[i]
    if exit_time[-1]>=arrival[i]:
        exit_time.append(j[1]+ exit_time[i-1])
    else:  
        
        exit_time.append(j[1]+ exit_time[i-1] + j[0]-exit_time[-1])
print("Completion -time",exit_time)    


# Turnaround Time = Exit time - Arrival Time

print("Order in which following process outputs are written",end = ' ')  
for i in range(0,n):
    print(tag[i][2],end = ' ')  
turn_around = []
print(" ")
for j in range(0,n):
    turn_around.append(exit_time[j]- tag[j][0])
    
print("Turn-Around",turn_around)
      
# Waiting Time 
wait_time = []
for j in range(0,n):
    wait_time.append(turn_around[j]- tag[j][1])
    
print("Waiting-Time",wait_time)
#Response Time

print("Response Time",wait_time) 

print("Avg Turn-Around",sum(turn_around)/n)
print("Avg Waiting",sum(wait_time)/n)
print("Avg Response",sum(wait_time)/n)   
    

        