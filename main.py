import datetime
import os
import subprocess
import sys
import threading
import time
import appium
import random
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_youtube_music_playlist_and_perform_actions(portName,deviceName, playlistUrls):
    commands = [
        f"adb -s {deviceName} uninstall io.appium.uiautomator2.server",
        f"adb -s {deviceName} uninstall io.appium.uiautomator2.server.test",
        f"adb -s {deviceName} uninstall io.appium.unlock",
        f"adb -s {deviceName} uninstall io.appium.settings"
    ]
    for command in commands:
        subprocess.run(command, shell=True)
    os.system(f"start /B start cmd.exe @cmd /k appium -a 127.0.0.1 -p {portName}")
    time.sleep(5)
    for playlistUrl in playlistUrls:
        print(f"[Device Name] : {deviceName}")
        proc = subprocess.Popen(
            ['adb', '-s', deviceName, 'shell', 'am', 'start', '-a', 'android.intent.action.VIEW', '-d',
             playlistUrl.strip()])
        proc.wait()

        # Wait for the YouTube app to launch
        driver = appium.webdriver.Remote(f"http://localhost:{portName}/wd/hub", desired_capabilities={
            "platformName": "Android",
            "appium:options": {
                "automationName": "UiAutomator2",
                "deviceName": deviceName.strip()
            }
        })

        time.sleep(5)
        try:
            el2 = driver.find_element(by=AppiumBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.RelativeLayout")
            el2.click()
        except:
            print("[Error] Unable to click the playbutton")
        time.sleep(5)
        count = 0
        while count < totalPlays:
            if likeSong == 0:
                try:
                    el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Like")
                    el4.click()
                except:
                    pass
            elif likeSong == 2:
                randSelc = random.randint(0, 1)
                if randSelc == 0:
                    try:
                        el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Like")
                        el4.click()
                    except:
                        pass
            else:
                print("[Info] Song Like Turned off")
            randDel = random.randint(int(minPlayTime), int(maxPlayTime))
            print(f"[Info] Playing song for {randDel} seconds")
            time.sleep(randDel)

            if subscribe == 0:
                try:
                    # to subscribe
                    el1 = driver.find_element(by=AppiumBy.ID,
                                              value="com.google.android.apps.youtube.music:id/artist")
                    el1.click()
                    time.sleep(2)
                    try:
                        el2 = driver.find_element(by=AppiumBy.ID,
                                                  value="com.google.android.apps.youtube.music:id/subscribe_button")
                        if el2.text != "Subscribed":
                            el2.click()
                            print("[Info] Subscribed The Artist")
                        else:
                            print("[Info] Artist Already Subscribed")
                    except:
                        print("[Info] No Sub Button")
                    time.sleep(2)
                    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Back")
                    el1.click()
                    time.sleep(1)
                    try:
                        el2 = driver.find_element(by=AppiumBy.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.RelativeLayout")
                        el2.click()
                    except:
                        print("[Error] Unable to click the playbutton")
                except:
                    pass
            elif subscribe == 2:
                randSelc = random.randint(0, 1)
                if randSelc == 0:
                    try:
                        # to subscribe
                        el1 = driver.find_element(by=AppiumBy.ID,
                                                  value="com.google.android.apps.youtube.music:id/artist")
                        el1.click()
                        time.sleep(2)
                        try:
                            el2 = driver.find_element(by=AppiumBy.ID,
                                                      value="com.google.android.apps.youtube.music:id/subscribe_button")
                            if el2.text != "Subscribed":
                                el2.click()
                                print("[Info] Subscribed The Artist")
                            else:
                                print("[Info] Artist Already Subscribed")
                        except:
                            print("[Info] No Sub Button")
                        time.sleep(2)
                        el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Back")
                        el1.click()
                        time.sleep(1)
                        el2 = driver.find_element(by=AppiumBy.XPATH,
                                                  value="//android.view.ViewGroup[@content-desc=\"PLAY ALL\"]/android.widget.ImageView")
                        el2.click()
                    except:
                        pass
            try:
                el1=WebDriverWait(driver,230).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,"Next song")))
                # el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next song")
                el1.click()
                count += 1
            except:
                count = totalPlays
        driver.quit()

def open_youtube_music_album_and_perform_actions(portName,deviceName, albumLists):
    os.system(f"start /B start cmd.exe @cmd /k appium -a 127.0.0.1 -p {portName}")
    time.sleep(5)
    for albumUrl in albumLists:
        proc = subprocess.Popen(
            ['adb', '-s', deviceName, 'shell', 'am', 'start', '-a', 'android.intent.action.VIEW', '-d',
             albumUrl.strip()])
        proc.wait()

        # Wait for the YouTube app to launch
        driver = appium.webdriver.Remote(f"http://localhost:{portName}/wd/hub", desired_capabilities={
            'platformName': 'Android',
            "appium:deviceName": deviceName.strip()
        })

        time.sleep(5)
        try:
            el2 = driver.find_element(by=AppiumBy.XPATH,
                                      value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.RelativeLayout")
            el2.click()
        except:
            print("[Error] Unable to click the playbutton")
        time.sleep(5)
        count = 0
        while count < totalPlays:
            if likeSong == 0:
                try:
                    el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Like")
                    el4.click()
                except:
                    pass
            elif likeSong == 2:
                randSelc = random.randint(0, 1)
                if randSelc == 0:
                    try:
                        el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Like")
                        el4.click()
                    except:
                        pass
            else:
                print("[Info] Song Like Turned off")
            randDel = random.randint(int(minPlayTime), int(maxPlayTime))
            print(f"[Info] Playing song for {randDel} seconds")
            time.sleep(randDel)

            if subscribe == 0:
                try:
                    # to subscribe
                    el1 = driver.find_element(by=AppiumBy.ID,
                                              value="com.google.android.apps.youtube.music:id/artist")
                    el1.click()
                    time.sleep(2)
                    try:
                        el2 = driver.find_element(by=AppiumBy.ID,
                                                  value="com.google.android.apps.youtube.music:id/subscribe_button")
                        if el2.text != "Subscribed":
                            el2.click()
                            print("[Info] Subscribed The Artist")
                        else:
                            print("[Info] Artist Already Subscribed")
                    except:
                        print("[Info] No Sub Button")
                    time.sleep(2)
                    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Back")
                    el1.click()
                    time.sleep(1)
                    try:
                        el2 = driver.find_element(by=AppiumBy.XPATH,
                                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.RelativeLayout")
                        el2.click()
                    except:
                        print("[Error] Unable to click the playbutton")
                except:
                    pass
            elif subscribe == 2:
                randSelc = random.randint(0, 1)
                if randSelc == 0:
                    try:
                        # to subscribe
                        el1 = driver.find_element(by=AppiumBy.ID,
                                                  value="com.google.android.apps.youtube.music:id/artist")
                        el1.click()
                        time.sleep(2)
                        try:
                            el2 = driver.find_element(by=AppiumBy.ID,
                                                      value="com.google.android.apps.youtube.music:id/subscribe_button")
                            if el2.text != "Subscribed":
                                el2.click()
                                print("[Info] Subscribed The Artist")
                            else:
                                print("[Info] Artist Already Subscribed")
                        except:
                            print("[Info] No Sub Button")
                        time.sleep(2)
                        el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Back")
                        el1.click()
                        time.sleep(1)
                        el2 = driver.find_element(by=AppiumBy.XPATH,
                                                  value="//android.view.ViewGroup[@content-desc=\"PLAY ALL\"]/android.widget.ImageView")
                        el2.click()
                    except:
                        pass
            try:
                el1 = WebDriverWait(driver, 230).until(
                    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Next song")))
                # el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next song")
                el1.click()
                count += 1
            except:
                count = totalPlays
        driver.quit()


def get_adb_devices():
    """Gets the list of all adb devices."""
    proc = subprocess.Popen(['adb', 'devices'], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    return out.decode('utf-8').strip().split('\n')


def returnFiletoList(filename):
    with open(filename, "r") as f:
        LinesToList = f.read().split("\n")
    return LinesToList


def is_today_05_07_2023():
    """Checks if today's date is 29-06-2023."""
    today = datetime.datetime.today()
    return today.day == 10 and today.month == 7 and today.year == 2023


if __name__ == "__main__":
    with open('config.settings', 'r') as config:
        file = config.read().split('\n')
        minPlayTime = file[0].split('=')[1]
        maxPlayTime = file[1].split('=')[1]
        likeSong = int(file[2].split('=')[1])
        subscribe = int(file[3].split('=')[1])
        totalPlays = int(file[4].split('=')[1])
    devices = get_adb_devices()
    print(devices)
    allAvailableDevicesName = []
    for device in devices:
        if "List of" in device:
            pass
        else:
            if "device" in device:
                allAvailableDevicesName.append(device.replace('\t', '').replace('\r','').replace('device',''))
    print("""

           _                         _                    _                        _   _               _              _ 
          | |                       (_)                  | |                      | | (_)             | |            | |
     _   _| |_   _ __ ___  _   _ ___ _  ___    __ _ _   _| |_ ___  _ __ ___   __ _| |_ _  ___  _ __   | |_ ___   ___ | |
    | | | | __| | '_ ` _ \| | | / __| |/ __|  / _` | | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \  | __/ _ \ / _ \| |
    | |_| | |_  | | | | | | |_| \__ \ | (__  | (_| | |_| | || (_) | | | | | | (_| | |_| | (_) | | | | | || (_) | (_) | |
     \__, |\__| |_| |_| |_|\__,_|___/_|\___|  \__,_|\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|  \__\___/ \___/|_|
      __/ |                                                                                                             
     |___/                                                                                                              
      ########################################## Develop By Fornax Technology #######################################
    """)

    print("\n\n")
    if is_today_05_07_2023():
        print("[Info] Script Expired")
        sys.exit()
    else:
        pass
    print("Choose Options Below:")
    print("1- Play Playlist\n"
          "2- Play Album")
    menuVal = int(input("Input Option No:"))
    listofUrlsPla=returnFiletoList('playlisturls.txt')
    listofUrlsAlb=returnFiletoList('albumurls.txt')
    for deviceName,portName in zip(allAvailableDevicesName,range(4728,4728+len(allAvailableDevicesName)+1)):
        if menuVal == 1:
            # open_youtube_music_playlist_and_perform_actions(portName,deviceName, listofUrlsPla)
            thread = threading.Thread(target=open_youtube_music_playlist_and_perform_actions, args=(portName,deviceName, listofUrlsPla))
            thread.start()
        else:
            # open_youtube_music_album_and_perform_actions(portName,deviceName,listofUrlsAlb)
            thread = threading.Thread(target=open_youtube_music_album_and_perform_actions, args=(portName,deviceName,listofUrlsAlb))
            thread.start()
        time.sleep(5)
