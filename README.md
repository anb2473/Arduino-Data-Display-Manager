# Arduino-Data-Display-Manager

A system to collect and display data from an Arduino system.

**NOTICE:** This system was created solely by Austin Nabil Blass for the Norwood School Green Hawks team. (The website for the team can be found at https://gmo-coral-reefs.netlify.app/, this website has been made entirely bu Austin Nabil Blass)

### Installation

Please go to our releases section to learn how to install the most recent version of our application.

### How to use

* Download the Arduino IDE, open up the CoralTank.ino file in the IDE, and upload the file to your arduino.
* Type in the COM port of your arduino if your arduino is connected by a physical cable in the port section. (i.e., COM9)
* Type in the baud rate of your arduino in the baud section. (Unless altered, this will always be 9600)
* Then press the enter key, and you will connect to that arduino.
* If you want to remotely connect to a server, you can run the `Server.py` file by installing python.
   * To install python, open your terminal in your start menu on mac and windows, or in the application folders on linux.
   * Then type python into your terminal, which will bring you to the python installation.
   * Once python is installed, type `pip install pyserial`, `pip install cryptography`, and `pip install socket`.
   * Then run the `Server.py` file with `python path/to/Server.py`.
* Once your server is running, it will ask you to fill our information on the baud rate and COM port of your arduino, and port the server will run on.
* The server will print out an IP address, which you can put in the baud section of the application, and you can put the port you entered in your server in the port section.
* From there you will be able to remotely see all data.
* Press the `V` at the top of the window to switch between the CSV visualizer. This will allow you to search through the existing CSV files, and see all recorded data. In the visualizer you will be able to see the raw CSV data, and a graph of all of the data.
* You can also edit the `run.json` file to change the application configurations. 
  
**NOTICE:** If you want to conenct to a server on a seperate router, you will need to do a little more configuring. You will need to use your routers admin password to set a port to your servers IP that you saw when you executed the server. From there, get your routers public IP. (Simply search `what is my public IP`) Enter that public IP in the app, and the port you set in your router configurations.

### System Details

The system itself works as follows:
* The Arduino file constantly prints out data from sensors.
* The python file reads the data with PySerial.
* The first 3 letters of the data are used to identify what category of data it is in. Once identified, the data is loaded into a hashmap.
* The system then reads the `run.json` file to identify how to properly process the data.
* It uses the csv section to identify which csv file each categories data should be loaded into, and how often new data should be stored.
* And it uses the configuration section to identify how to render each category.
* With that data, it renders all of the desired data.
* When connecting to a server system, it uses AESGCM encryption, private public keys, hashed passwords, and Fernet keys to ensure all data is secured.
