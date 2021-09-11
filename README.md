# VolumeChangerArduino
**Summary:** Designed for changing computer volume with potentiometer.
## **How do you setup?**
&emsp;**1)** Make your Arduino connections as I show in the [pictures](#arduino).
&emsp;**2)** If you use different analog input don't forget to change Arduino code.
&emsp;**3)** In python import the project:
&emsp;&emsp;```python from VolumeChangerArduino import VolumeChangerArduino```
&emsp;&emsp;Assign the class object to your variable:
&emsp;&emsp;<code><var>yourVariable</var> = VolumeChangerArduino(<kbd>port</kbd>, <kbd>baudrate</kbd>, <kbd>sleeptime</kbd>)</code><br>
&emsp;&emsp;&emsp;<kbd>port</kbd>: Arduino port as string. (port="COM6")<br>
&emsp;&emsp;&emsp;<kbd>baudrate</kbd>: Arduino baudrate as int. (baudrate=115200)<br>
&emsp;&emsp;&emsp;<kbd>sleeptime</kbd>: Waiting time before passing next loop to get serial input in seconds as int. (sleeptime=0.001)<br>
&emsp;<b>4)</b> Run the app:<br>
&emsp;&emsp;<code><var>yourVariable</var>.run()</code>


<h2><b>Images</b></h2>
<h3 id="arduino">&emsp;<b>Arduino Circuit</b></h3>
<p align="center">&emsp;<kbd>1kOhm</kbd> constant resistor used | <kbd>100kOhm</kbd> potentiometer used.</p>
<p align="center"><img src="/images/circuit.png" width=40% height=auto><br></p>
<h3>&emsp;<b>Why are there too much function created with curve_fit?</b></h3>
<p>&emsp;Because if single function used, it's error rises too much as shown in the picture.</p>
<p align="center"><img src="/images/setup_graph.png" width=40% height=auto></p>
