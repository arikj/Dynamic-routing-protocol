#Router A
#input file of type <src,dest,dest port,cost>
#no need to initialise the dictionary, as new keys can be added at runtime too.
import threading
import time

dv_received={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}; #dest => cost;  
my_dv={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0};
Routing_table={} #could either use a list as well.
routing_entry=[] #[dest,cost,next node]
def send_dv():
    #do something here.
    threading.Timer(5, send_dv).start();

    
#ports are predefined (either through file or hard coded)
port={'A':1000,'B':1001,'C':1002,'D':1003,'E':1004,'F':1005};
f = open('initial_dv.txt','r')

#for line in f:
#    list1= line.split(',');
#    if(list1[1]=='A'):
#        src_port=list1[2];
f = open('initial_dv.txt','r') 
for line in f:
    line=line.rstrip('\n');
    list1= line.split(',');
    #print list1;
    if(list1[0]=='A'):
        routing_entry=[list1[3],list1[1]];
        my_dv[list1[1]]=list1[3];
        Routing_table[list1[1]]=routing_entry;
        #print(routing_entry);
        #Routing_table.append(routing_entry);
        
#print(src_port);
#print(Routing_table);
print(my_dv);
send_dv();  #send your dv for the first time and evry 5 sec thereafter.
#on receipt of any other new dv: from a 'neighbour'
rcvd_from='B';
neighbour='B';
distance = my_dv[neighbour];
for key, value in dv_received.iteritems():
    if(value != 0):
        if(my_dv[key] == 0 or my_dv[key] > (value + distance)):
            my_dv[key]=(value + distance);
            routing_entry=[my_dv[key], neighbour];
            Routing_table[key]=routing_entry;


