Gantt=[]
def Waiting_time(Processes,n,bt,wt,Quantum):
    Remaining_burstTime=[0]*n
    for i in range(n):
        Remaining_burstTime[i]=bt[i]
    t=0
    while(1):
        done=True
        for i in range(n):
            if(Remaining_burstTime[i]>0):
                done=False
                if(Remaining_burstTime[i]>Quantum):
                    t+=Quantum
                    Gantt.append(("P"+str(i))*(Quantum))
                    Remaining_burstTime[i]-=Quantum
                else:
                    t+=Remaining_burstTime[i]
                    wt[i]=t-bt[i]
                    Gantt.append(("P"+str(i))*(Remaining_burstTime[i]))
                    Remaining_burstTime[i]=0
        if(done==True):
            break
def TurnAroundTime(Processes,n,bt,wt,tat):
    for i in range(n):
        tat[i]=bt[i]+wt[i]
def FindAvgTime(Processes,n,bt,Quantum):
    wt=[0]*n
    tat=[0]*n
    Waiting_time(Processes,n,bt,wt,Quantum)
    TurnAroundTime(Processes,n,bt,wt,tat)
    print("Processes  Burst_Time  Waiting_Time", "Turn_Around_time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt+=wt[i]
        total_tat+=tat[i]
        print(" ",i+1, "\t\t", bt[i],"\t\t", wt[i], "\t\t", tat[i])
    print("\nAverage waiting time = %.2f "%(total_wt /n) ) 
    print("Average turn around time = %.2f "% (total_tat /n)) 
    
Process_count=int(input("Enter The number of Processes-->"))
Quantum=int(input("Enter The quantum period-->"))
Burst_time=[]
Process_id=[0,1,2,3]
for i in range(Process_count):
    Burst_time.append(int(input("Enter Burst_Time of Process "+str(i)+" ")))
FindAvgTime(Process_id,Process_count,Burst_time,Quantum)
Index=[int(i) for i in range(sum(Burst_time)+1)]
print("Gantt---->",*Gantt,"\nIndex---->",*Index)
