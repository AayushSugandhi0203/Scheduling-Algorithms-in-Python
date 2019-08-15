
import pandas

datContent = [read.strip().split() for read in open("input_roundrobin.dat").readlines()]
n = int(datContent[0][0])
j = 1
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

for i in range(0,n):
    process.append(i)

zipp = zip(process,arrival,burst,priority)
tag = sorted((zipp),key=lambda x: (x[1],x[2],))

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
time = 0
time_count  = 0
turn_around= []
wait_time = []
temp_proc = []
exit_time = []
rem_time = []
for i in bur2:
    rem_time.append(i)
remain = n 
rq = 0
flag = 0
time = 0
start = []
count = 0
fire = 1

time_count = []
time_count.append(0)
progress_count = []

print(rem_time)
while ( remain !=0  ):
    if rem_time[count] <= quantum and rem_time[count] >0 :
        if fire ==1:
            progress.append(count)
            
        time = time + rem_time[count]
        time_count.append(time)
        progress_count.append(proc2[count])
        rem_time[count] = 0
        flag = 1
    elif rem_time[count] >0:
        if fire==1:
            progress.append(count)
            
        rem_time[count] = rem_time[count] - quantum
        time = time + quantum
        time_count.append(time)
        progress_count.append(proc2[count])
            
    if rem_time[count]==0 and flag==1:
        if fire ==1:
            progress.append(count)
            fire =1
        exit_time.append(time)    
        remain = remain - 1
        temp_proc.append(proc2[count])
        turn_around.append(time - arr2[count])
        
        wait_time.append(time - arr2[count]-bur2[count])
        flag=0
        
        
    if count == n-1:
        
        count = 0
    elif arr2[count +1]<=time:
        
        count = count + 1
        #time_me.append([time,count])
        start.append(time)
    else:
        count = 0 
        
print("Printing Order",temp_proc)               
print("Turn Around",turn_around)
print("Wait Time",wait_time)
print("Gantt Time",start)  
print("Progress",progress)   
print("Time count",time_count)
print("Progress Count",progress_count)
start_time = []
for i in temp_proc:
    k = progress_count.index(i)
    start_time.append(time_count[k])
print("Start time",start_time)    

#Response Time 
response_time = []
for i in range(0,n):
    
    k = temp_proc[i]
    response_time.append(start_time[i]-arrival2[k])
    
print("Response Time",response_time)

print("Avg Turn-Around",sum(turn_around)/n)
print("Avg Waiting",sum(wait_time)/n)
print("Avg Response",sum(response_time)/n) 
        
        
          
        
        

