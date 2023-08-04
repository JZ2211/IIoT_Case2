# access to Google Firebase Realtime database
#
# Modified 7/31/2023
# by Jin Zhu
#
# required package: firebase-admin 
# $sudo pip3 install firebase-admin==5.4.0

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#modify the json file name and the database URL for your firebase project
cred=credentials.Certificate('/home/pi/IIoT_Case2/iiot-nodemcu-example.json')
firebase_admin.initialize_app(cred, {'databaseURL':'https://iiot-nodemcu-example.firebaseio.com/'})

#push new message to the firebase
def push_tofirebase(nodeID, currentdate, currenttime, msglist):
    # obtain the value for each field and prepare the entry to be pushed to firebase
    entry = {"date":currentdate, "time": currenttime} #include the date and time
    for item in msglist:
        key=item.split(":")[0].strip() #seperate the key and value in each pair
        value=float(item.split(":")[1]) #convert a string back to the float number
        entry[key]=value  #add to the dictionary
    ref1=db.reference(nodeID)
    #print(entry) #for debugging
    ref1.push().set(entry)

# obtain data on the given date with the max number of entries 
def inquery_by_date(nodeID,date,max):
    ref1=db.reference(nodeID)
    snapshot=ref1.order_by_child('date').equal_to(date).get()
    for key, val in snapshot.items():
        print(val)
    return snapshot

