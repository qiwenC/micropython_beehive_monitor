
## Install Atom with Pymakr plugin

1. Download the Atom from https://atom.io
2. Install Atom and open it

>3. Ensure that you have Atom installed and open.  
>4. Navigate to the Install page, via Atom > Preferences > Install.
>5. Search for Pymakr and select the official Pycom Pymakr Plugin.  
>6. You should now see and Install button. Click this to download and install the Pymakr Plugin.   

## Initial Configuration
>1. Connect your Pycom device to your computer via USB.  
>2. In the menu, go to Atom > Preferences > Packages > Pymakr.  
>3. Open the Pymakr console by clicking the 'Open' button, located in the lower right side of the Atom window.  
>4. Click, 'More' followed by 'Get Serial Ports'. This will copy the serial address of your expansion board to your clipboard.  
>5. Navigate to 'Settings' > 'Global Settings'. 
>6. Paste this into the text field 'Device Address'.  
>7. Press connect and the Pymakr console should show three arrows '>>>', indicating that you are connected!

## Flash project to the Pytrack

1. Connect your Pycom device to your computer via USB
2. Open the Atom, in the menu, go to 'File' > 'Add Project Folder'
3. Choose the project folder, and then click open
4. Code your pycom on the main.py file, save the state
5. Press 'Sync' on the right of the Pymakr console to synchronize the project to the pycom device.

### Structure of the project folder
- main.py  
- boot.py
- lib(contains all the library code)
- cert(contains all the certification)

## Troubleshooting

1. If the device cannot be recognised by the computer (shows 'Found 0 serialports' on the Atom command line), 
try to adjust the position of the wire for better connection. If not working, restart the computer. (Change another cable) 

* Do not pull out and re-plug the USB cable all they time. It will cause the USB socket on the board loose, which 
makes it hard to connect.
