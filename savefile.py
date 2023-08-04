# Save the received messages to a local .txt file
# Modified 07/31/2023
# by Jin Zhu

import re
from os import path
import os

#save the received message to a local .txt file
def save_tofile(homepath, nodeID, currentdate, currenttime, message):
    if not path.exists(homepath+nodeID):
        os.mkdir(homepath+nodeID)
    filename = homepath+nodeID+'/log_' + re.sub('-','_',currentdate)+'.txt'  #log file will be named as log_yyyy_mm_dd.txt
    if path.exists(filename):  #is the log file exist?
        #if yes, append data
        with open(filename,'a', buffering=1) as f1:
            f1.write(currentdate + ', ' + currenttime + ', ' + message+'\n')
    else:
        #if no, create the file and write the message
        with open(filename,'w', buffering=1) as f1:
            f1.write(currentdate + ', ' + currenttime + ', ' + message+'\n')
