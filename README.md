# Remotealert

Allows sending notifications which can be retreived using the RemoteAlert notification app in the store
https://play.google.com/store/apps/details?id=com.soy.remotealert

## Installation & Usage:
```
git clone https://github.com/Ritiek/Remotealert
cd Remotealert
sudo python Remotealert.py
```
ex. `sudo python Remotealert.py a32b831c-7623-4c43-99cf-b614ff54e902 'my_message'`

## Alias for ID:

You can add your Device names and their ID's to simply send notification using the Device name instead of typing the full ID everytime by editing the script:

`sudo nano Remotealert.py`

Replace "device1" with your device name like "galaxys6" and add its ID replacing "device1_id", similary you can add more devices..

Then you can use:
ex. `sudo python Remotealert.py galaxys6 'my_message'`
and you will receive a notification on your device.
