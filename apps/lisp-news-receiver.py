#
# lisp-news-receiver.py
#
# Listen on the (S,G) and print messages received.
#
# Usage: python lisp-news-receiver.py <source> <group>
#

import sys
import socket
import datetime
import struct
import threading

#------------------------------------------------------------------------------

usage = "Usage: python lisp-news-receiver.py <source> <group>"
source = ""
group = ""
port = ""
msocket = None
timer = None

#------------------------------------------------------------------------------

def keep_joining(msocket, group):
    global timer

    mreq = struct.pack("4sl", socket.inet_aton(group), socket.INADDR_ANY)
    msocket.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)
    msocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    timer = threading.Timer(30, keep_joining, [msocket, group])
    timer.start()
#enddef

#------------------------------------------------------------------------------
#
# Get command line parameters.
# 
if (len(sys.argv) < 3):
    print usage
    exit(1)
#endif

source = sys.argv[1]
group = sys.argv[2]

if (source.find(".") == -1 or group.find(".") == -1):
    print "Must supply IPv4 address in dotted decimal"
    exit(1)
#endif

port = group.split(".")
port = 0x800 + int(port[-2]) + int(port[-1])

#
# Open send UDP socket.
#
print "Open listen socket ({} -> {}:{}) ... ".format(source, group, port),

try:
    msocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msocket.bind((group, port))
    msocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mreq = struct.pack("4sl", socket.inet_aton(group), socket.INADDR_ANY)
    msocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    print "succeeded"
except:
    print "failed"
    exit(1)
#endtry

timer = threading.Timer(15, keep_joining, [msocket, group])
timer.start()

#
# Start off looping and sending system status.
#
while (True):
    try: 
        message = msocket.recvfrom(1000)
        message = message[0]
    except: 
        break
    #endtry

    ts = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S.%f")
    print "Message received {}:\n{}\n".format(ts, message[0:-1]),
    for i in range(40): print "-",
    print ""
#endwhile

timer.cancel()
msocket.close()
exit(0)

#------------------------------------------------------------------------------

