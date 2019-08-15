import pandas

datContent = [read.strip().split() for read in open("inputnon_premp_prio.dat").readlines()]
n = int(datContent[0][0])

j =1
arrival = []
burst = []
arrival2=[]
burst2=[]
process= []
priority = []
priority2=[]
for i in range(0,n):
    a ,b,c = datContent[j][0] ,  datContent[j][1], datContent[j][2]
    a = int(a)
    b = int(b)
    c = int(c)
    arrival.append(a)
    arrival2.append(a)
    burst.append(b)
    burst2.append(b)
    priority.append(c)
    priority2.append(c)
    
    j = j+1

quantum = int(datContent[n + 1][0])
queue = int(datContent[n + 2][0])

for i in range(1,n+1):
    process.append(i)
quantum = 1
zipp = zip(process,arrival,burst,priority)
tag = sorted((zipp),key=lambda x: (x[1],x[3]))

arr2 = []
bur2 = []
proc2 =[]
prio2= []
for i in tag:
    arr2.append(i[1])
    bur2.append(i[2])
    proc2.append(i[0])
    prio2.append(i[3])

progress = []
time = min(arrival)
temp_arr= []
temp_bur = []
temp_prio = []
exit_time = []
p =n
while(len(progress)!= sum(burst)):
    
    
    temp_arr = []
    temp_bur = []
    temp_prio = []
    for i in range(0,len(arr2)):
        if arr2[i] <= time:
            temp_arr.append(arr2[i])
    for j in range(0,len(temp_arr)):        
        temp_bur.append(bur2[j])
        temp_prio.append(prio2[j])
    for j in range(0, len(temp_bur)):
        if temp_bur[j]==0:
            temp_prio[j]=1000
            
    min_prio = min(temp_prio)
    
    ind = temp_prio.index(min_prio)
    while(bur2[ind]!=0):
        ind = temp_prio.index(min_prio)
        bur2[ind] = bur2[ind]  - 1
        progress.append(proc2[ind])
        time = time + 1

print("Gantt Chart is(no. show the process no.)",progress)
    
rev_progress = progress[::-1]
print("Order in which following process outputs are written",end =' ')  
for i in range(0,n):
    print(i+1,end=' ')    
print(" ")  
counter_exit = []    
counter_start = []
for j in range(1,n+1):
    a = rev_progress.index(j)
    b = progress.index(j)
    counter_exit.append(len(progress)-a)
    counter_start.append(b)
print("Completion Time",counter_exit)  
# Turnaround Time = Exit time - Arrival Time
turn_around = []
for j in range(0,n):
    turn_around.append(counter_exit[j]- arrival[j])
    
print("Turn-Around",turn_around)
      
# Waiting Time 
wait_time = []
for j in range(0,n):
    wait_time.append(turn_around[j]- burst[j])
    
print("Waiting-Time",wait_time) 

#Response Time = Start Time - Arrival Time
 
print("Start-time",counter_start)
response_time = []
for j in range(0,n):
    response_time.append(counter_start[j] - arrival[j])
    
print("Response Time",response_time)    

print("Avg Turn-Around",sum(turn_around)/n)
print("Avg Waiting",sum(wait_time)/n)
print("Avg Response",sum(response_time)/n)        

            
            