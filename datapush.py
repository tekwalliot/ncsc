import json
import requests
from datetime import datetime, timedelta
from swpsdata.models import DeviceData

headers = {'Content-Type': 'text/json'}                                                                          
url = "https://nredcap-api.smartcenter.co.in/api/FarmerInstallationData"
url1 = 'https://nredcap-api.smartcenter.co.in/api/DayWiseData'                                
url2 = 'https://nredcap-api.smartcenter.co.in/api/AgencyDeviceData'                                                  
access = "$solar@ACCESS!17^"     

serial_no=['18170']                                                                                                                                                     

for i in range(len(serial_no)):
  try:
     a = DeviceData.objects.values( ).get(devNo = serial_no[i])
     fardet = {
          "agencykey":access,
          "first_Name": str(a['name']),
          "last_Name": " ",
          "gender": str(a['gender']),
          "dob":" ",
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
          "mfg": str(a['conMake'] ),
          "sno": int(a['devNo']) ,
          "controller_Capacity": "5HP",
          "controller_Version": "",
          "no_Of_Stages": "5",
          "type": "AC",
          "aC_Voltage": 415,
          "aC_Current": 9.5,
          "date_Of_Installation": str(a['dateInst']),
          "installer_Name": str(a['InstName']),
          "installer_Serial_No": 0,
          "motor_Manufacturer": str(a['pumpMfg']),
          "motor_Depth": 150,
          "motor_Capacity": "5 HP",
          "controller_Motor_Distance": 10,
          "no_of_Panels_in_series": 16,
          "no_of_Panels_in_Parallal":  0,
          "panel_Wattage": 300,
          "total_Power": 4800,
          "voc": 720,
          "vmp": 575,
          "imp": "8.4", 
	    "isc": "9.5",
          "rotating_Frequency": "50 Hz",
          "controllerPowerCapacity": "5.0 Kw",
          "solarDCV": 750,
          "pvModuleMake": str(a['pvMake']),
     }

     data = json.dumps(fardet)
     r = requests.post(url,data=data,headers=headers)
     print(i,r.status_code,r.text)
  except Exception as e:
       print(i,e)