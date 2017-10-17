# How to publish message to Adafruit

Following this file, you should be able to get your accelerations and GPS coordinates by Pytrack and
publish the x-axis as the data and pin it by your location on the map of adafruit dashboard.

## What you'll need

1. Adafruit account
2. Atom Pymakr
3. Pytrack with WiPy

## Getting Start

1. Download PublishMsg folder 
2. Open Atom Pymakr Plugin 
3. Add PublishMsg project to Pymakr
4. Modify the code below in main.py to your own details. 

5. Setting your adafruit, create a new feeds named 'GPS', create a new map type block in the dashboard fed
by 'GPS'

6. Synchronize the project to the Pytrack

## Results
1. On the Pymakr Console, you should see

2. Open the Adafruit feeds, you should see


## Troubleshooting

* When sending GPS signals, it is better to be outside, so that you will get a better signal.
* The message published by the pyTrack should be 'String' type, using str() function to change the type.
* Installtion and configuration of Pymakr Plugin is in the Instalation, settings and configuration file
* The way to access your adafruit username and AIO Key is in the Instalation, settings and configuration file.
* The details of adafruit feeds and dashboard setting is in the Instalation, settings and configuration file.

