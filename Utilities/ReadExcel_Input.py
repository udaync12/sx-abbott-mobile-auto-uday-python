import sys
import unittest
import os
import pandas as pd

sys.path.append(sys.path[0] + "/...")
cwd = os.getcwd()
print(cwd)
filepath = f'.\\DataInput\\General_Store_Input_Master.xlsx'


class ReadExcelInput:

    def read_device_configuration(self):
        df = pd.read_excel(filepath, 'DeviceConf')
        print(df)
        print("Total Rows in Sheet:", len(df.index))
        rCnt = 0
        device_config = {}
        # Fetch the device configuration details from the 'Device' sheet of the Excel where 'SKIP' is Null
        while rCnt < len(df.index):
            if pd.isnull(df.loc[rCnt, 'SKIP']) is True:
                print("Device Configuration from this row to be selected")
                print(df.loc[rCnt, 'DeviceName'])
                device_config = dict({'DeviceName': df.loc[rCnt, 'DeviceName'],
                                      'PlatformName': df.loc[rCnt, 'PlatformName'],
                                      'AppPackage': df.loc[rCnt, 'AppPackage'],
                                      'UDID': df.loc[rCnt, 'UDID']})
                return device_config
                break
            else:
                rCnt += 1


