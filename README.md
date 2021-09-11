# VolumeChangerArduino
**Summary:** Designed for changing computer volume with potentiometer.
## **How do you setup?**
&emsp;**1)** Make your Arduino connections as I show in the [pictures](#arduino).<br>
&emsp;**2)** If you use different analog input don't forget to change Arduino code.<br>
&emsp;**3)** In python import the project:
```python 
from VolumeChangerArduino import VolumeChangerArduino
```
&emsp;**4)** Assign the class object to your variable:<br>
```python
yourVariable = VolumeChangerArduino(port, baudrate, sleeptime)
```
>`port`: Arduino port as string. (port="COM6")<br>
>`baudrate`: Arduino baudrate as int. (baudrate=115200)<br>
>`sleeptime`: Waiting time before passing next loop to get serial input in seconds as int. (sleeptime=0.001)<br>

&emsp;**5)** Run the app:<br>
```python
yourVariable.run()
```

## **Images**
<h3 id="arduino">&emsp;<b>Arduino Circuit</b></h3>
<p align="center">&emsp;<kbd>1kOhm</kbd> constant resistor used | <kbd>100kOhm</kbd> potentiometer used.</p>
<p align="center"><img src="/images/circuit.png" width=60% height=auto><br></p>
<h3>&emsp;<b>Why are there too much function created with curve_fit?</b></h3>
<p>&emsp;Because if single function used, it's error rises too much as shown in the picture.</p>
<p align="center"><img src="/images/setup_graph.png" width=60% height=auto></p>
