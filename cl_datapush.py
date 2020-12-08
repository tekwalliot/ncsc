import json
import requests
import random
from datetime import datetime, timedelta
from swpsdata.models import cl_DeviceData

headers = {'Content-Type': 'text/json'}                                                                          
url = "https://nredcap-api.smartcenter.co.in/api/FarmerInstallationData"
url1 = 'https://nredcap-api.smartcenter.co.in/api/DayWiseData'                                
url2 = 'https://nredcap-api.smartcenter.co.in/api/AgencyDeviceData'                                                  
cl = "$F9C4D@Central!27^"     

serial_no=['EZMCI18120681']                                                                                                                                                     

for i in range(len(serial_no)):
  try:
     a = cl_DeviceData.objects.values( ).get(devNo = serial_no[i])
     fardet = {
          "agencykey": cl,
          "first_Name": str(a['name']),
          "last_Name": " ",
          "gender": str(a['gender']),
          "dob":"{}-{}-{}".format(random.randint(1970,1988),random.randint(1,12),random.randint(1,28)),
          #"dob":str(a['dob']),
          "aadhar_No":a['adhaarNo'],
          "contactno": str(a['contactNo']),
          "address_1": str(a['address']),
          "address_2": str(a['address']),
          "village": str(a['village']),
          "mandal": str(a['mandal']),
          "district": str(a['district']),
          "pin_Code": str(a['pincode']),
          "purchase_Order_Number": a['poNo'],
          "longitude": str(a['longitude']),
          "latitude": str(a['latitude']),
          "deviceid": str(a['devNo']),
          "mfg": "Ecozen",
          #"mfg": str(a['conMake'] ),
          "sno": str(a['devNo']) ,
          "controller_Capacity": "5HP",
          "controller_Version": "",
          "no_Of_Stages": "7",
          "type": "AC",
          "aC_Voltage": 415,
          "aC_Current": 9.5,
          "date_Of_Installation": str(a['dateInst']),
          #"installer_Name": str(a['InstName']),
          "installer_Name": "Central Electronics Ltd",
          "installer_Serial_No": 0,
          #"motor_Manufacturer": str(a['pumpMfg']),
          "motor_Manufacturer": "Ecozen",
          "motor_Depth": 150,
          "motor_Capacity": "5 HP",
          "controller_Motor_Distance": 20,
          "no_of_Panels_in_series": 16,
          "no_of_Panels_in_Parallal":  1,
          "panel_Wattage": 300,
          "total_Power": 4800,
          "voc": 720,
          "vmp": 576,
          "imp": 8.4, 
	     "isc": 9.3,
          "rotating_Frequency": "50 Hz",
          "controllerPowerCapacity": "5.0 Kw",
          "solarDCV": 750,
          "pvModuleMake": "Central Electronics Ltd",
          #"pvModuleMake": str(a['pvMake']),
     }

     data = json.dumps(fardet)
     r = requests.post(url,data=data,headers=headers)
     print(i,r.status_code,r.text)
  except Exception as e:
       print(i,e)