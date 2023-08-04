# Test firebase realtime database connection using firebase-admin
# Created on July 28 2023
# By Jin Zhu
# 
# required package: firebase-admin 
# $sudo pip3 install firebase-admin==5.4.0

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#modify the json file name and the database URL for your firebase project
cred=credentials.Certificate('\home\pi\IIoT_Case2\iiot-nodemcu-example.json')
firebase_admin.initialize_app(cred, {'databaseURL':'https://iiot-nodemcu-example.firebaseio.com'})

#example access
#read the data
ref1=db.reference('test')
print(ref1.get())

ref2=db.reference('sensor 15')
print(ref2.get())  #return none if it is empty

#write data using push
ref2.push().set({'humidity': 68, 'pressure': 1000, 'temperature': 24})
ref2.push().set({'temperature (degC)': 25, 'humidity (%)': 65, 'pressure (Pa)': 100955})

#read again
snapshot = ref2.order_by_key().get()
print(snapshot)  #should output the two entries just added
