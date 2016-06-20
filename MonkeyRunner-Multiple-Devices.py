
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import os
import sys

def main():
    # get all device that connected with USB 
    connected_devices = os.popen('adb devices').read().strip().split('\n')[1:]
    devices = []
    for deviceId in connected_devices:
        # get device name
        deviceName = deviceId.split('\t')[0]
        print('deviceName: ' + deviceName)
        
        #get connection of device 
        device = MonkeyRunner.waitForConnection(10.0, deviceName)
        devices.append(device)

    # set start activity
    activityName = 'com.android.settings' + '/' + 'com.android.settings.ManageApplications'     
    for device in devices:
        device.startActivity(component=activityName)
        # device.startActivity(component='com.android.settings/.Settings')
    
    print ('startActivity: Settings')

    MonkeyRunner.sleep(0.3)
    # for i in range(0, 15):
    #     for device in devices:
    #         device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
    #     MonkeyRunner.sleep(0.3)

    # for device in devices:
    #     device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    # MonkeyRunner.sleep(1.2)

    # for device in devices:
    #     device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
    # MonkeyRunner.sleep(1.2)

    print ('Applications')
    # Applications
    for device in devices:
        device.press('KEYCODE_DPAD_RIGHT', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1.8)
    
    for device in devices:
        device.press('KEYCODE_DPAD_RIGHT', MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(1.8)    

    print ('UnCheck All')
    for j in range(1, 400):
        for device in devices:    
            device.press('KEYCODE_ENTER', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1.2)

        # Detail
        for device in devices:
            device.touch(128, 1125, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
        for device in devices:
            device.touch(128, 925, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.5)
        for device in devices:
            device.touch(1285, 1685, MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1.2)
        for device in devices:
            device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.3)
        for device in devices:
            device.press('KEYCODE_ESCAPE', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(1.2)
        for device in devices:
            device.press('KEYCODE_DPAD_DOWN', MonkeyDevice.DOWN_AND_UP)
        MonkeyRunner.sleep(0.3)

if __name__ == "__main__":
    main()




