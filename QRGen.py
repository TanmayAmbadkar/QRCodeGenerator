import pyqrcode 
import os
from pyqrcode import QRCode 
import pandas as pd
dataset=pd.read_csv("Fresher1.csv")  
RollNo=dataset.iloc[:,[0]].values
Name=dataset.iloc[:,[1]]
os.mkdir("QRCodes")
# String which represent the QR code 
for i in RollNo:
    url = pyqrcode.create(i[0])   
    url.svg("QRCodes\\{}.svg".format(i[0]), scale = 8)