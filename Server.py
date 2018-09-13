import socket, ssl, random, subprocess, time, os
from thread import * 
import threading
from subprocess import call


bindsocket = socket.socket()
bindsocket.bind(('10.0.1.101', 1023))
bindsocket.listen(20)
print ("server started and listening")
 

def port():
    x1,x2,x3 = random.sample(range(1024,65536),3)
    
    return x1,x2,x3



def do_something(connstream, data):

    return False

    
def deal_with_client(connstream):

    data = connstream.read()
        
    while data:

        if not do_something(connstream, data):

            break



    A = port()
    
    print "message: ", data
   
    
    connstream.send(str(A))

    proc = subprocess.call(["sshpass", "-p", 'osboxes.org', "ssh", "-t", "-o", "StrictHostKeyChecking=no", "osboxes@10.0.1.100", "sudo", "python", "Desktop/SRPLG_RULE/rule.py", str(ip),str(A[0]),str(A[1]),str(A[2])])

   

    connstream.close
    

def flush_rule():

  #  try:
   #         proc = subprocess.call(["sshpass", "-p", 'osboxes.org', "ssh", "-t", "-o", "StrictHostKeyChecking=no", "osboxes@$server", "sudo", "python", "Desktop/SRPLG_RULE/flush.py"])

#    except subprocess.CalledProcessError as e:

#        output= e.output
     
    call(["./hapus.sh"],shell=True)






while True:



    conn, fromaddr = bindsocket.accept()
    
    ip = fromaddr[0]

    
    connstream = ssl.wrap_socket(conn,ssl_version=ssl.PROTOCOL_TLSv1,



                                 server_side=True,



                                 certfile="server.crt",



                                 keyfile="server.key")



    try:

        flush_rule()
        
        start_new_thread(deal_with_client, (connstream,))
      


        print "connected from Ip Address", ip
 


    finally:

        
        print("The time procces is"), time.clock()


bindsocket.close()