# YT-music-mobile-app-automation-using-appium-python
Now a days automation is one of the growing method used to promote and push your content into the algorithm.
This is one of the example how one can increase his/her views on playlist/album....

## Installation

1. Install Python 3.7 or above
2. Install Pycharm or any ide of your choice.
3. Install python module using this command ```pip install requirements.txt```
4. Install Appium: Appium requires Node.js to run, so you need to install Node.js on your system. Download and install Node.js from the official website (https://nodejs.org/en/download/). Make sure to select the appropriate version for your operating system.
5. Set up Appium Server: Open a terminal or command prompt and install the Appium server globally by running:
       ```npm install -g appium```
6.Start Appium Server: Start the Appium server by running the following command in a terminal or command prompt:
       ```appium```
7. Download and install Java (JDK) and set a path of JDK and bin folder.
   - Download the “.exe” file from [here](http://www.oracle.com/technetwork/java/javase/downloads/index.html) (Version: jdk-20 or whichever is the latest you find there).
   - Install the “.exe” file.
   - Add New Variable "Java_Home" and in path add bin folder which is present in jdk folder.
   - To make sure that the system can recognize the Java that is installed, go to the command prompt and type ```java –version```. This should return the latest version of the JDK installed in the system.
8. Install Android SDK (Software Development Kit)
   - Download the Android SDK from [here](https://developer.android.com/studio/index.html).
   - Click on the link “android-studio-2022.2.1.20-windows.exe” (or whichever is the latest you find there) and then click on the download button.
   - Install the .exe and during installation do select platform-tools to be installed along with it as well.
   - After installation we have to add two path in envirnoment variables.
       - Path of the “platform-tools” folder in the Android/SDK folder (For Example, C:\Users\Aaqib Mehrban\AppData\Local\Android\Sdk\platform-tools).
       - Path of the “build-tools” folder in the Android/SDK folder (For Example, C:\Users\Aaqib Mehrban\AppData\Local\Android\Sdk\build-tools).
     - Now add another Variable ANDRIOD_HOME and add path of Andriod SDK (For Example, C:\Users\Aaqib Mehrban\AppData\Local\Android\Sdk)
Everything is install and we are good to go now.

## Setting Andriod Device to get detected by appium server

- Enable Developer Options: On your Android device, go to Settings > About phone and locate the "Build number" entry. Tap on it seven times to enable Developer Options.
- Enable USB Debugging: In the Developer Options, locate the "USB debugging" option and enable it. This will allow your device to communicate with your computer over USB.
- Connect the Device to your Computer: Use a USB cable to connect your Android device to your computer. Ensure that the device is recognized and drivers are installed correctly. You might need to install the appropriate USB drivers for your specific device or enable USB debugging authorization on your device if prompted.
- Verify Device Connection: Open a terminal or command prompt and run the following command to verify that your device is detected by the computer: ```adb devices```

## Features
- it will run automation in parrallel. will run automation on each device at the same time.
- Random play time between minimum and maximum time assigned in config.settings.
- Randomly like song.
- Randomly Subscribe to Artist of the song.
- You can assign no of plays. so let say you assign 5 and there are 4 songs in album. what script will do is after playing 4 songs it will play first song again.

## Demo
- watch demo of its running [Youtube](https://www.youtube.com/shorts/u0UE01w_2F8) .

## How to run

- Download this repo to your local pc and open it in pycharm.
- Run main.py file and it will start opening app in all devices at once and start playing playlist.

+ Note: All devices must be unlocked. to be able to run this.
