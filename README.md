# Remotealert
Allows sending notifications which can be retreived using the RemoteAlert notification app in the store
https://play.google.com/store/apps/details?id=com.soy.remotealert

# Installing:
```
git clone https://github.com/Ritiek/Remotealert
```

# Usage:
```
cd Remotealert
sudo python Remotealert.py
```
You can add your Device names and their ID's to simply send notification using the Device name instead of typing the full ID by editing the script:
```
sudo nano Remotealert.py
```
Replace "device1" with your device name like "galaxys6" and add its ID replacing "device1_id", similary you can add more devices..

Then you can use:
e.g. ```sudo python Remotealert.py galaxys6 'my_message'```
and you will receive a notification on your device.
