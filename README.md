# VolumeChangerArduino
 Summary: Designed for changing computer volume with potentiometer.
<h2><b>How do you setup?</b></h2>
<p>
&emsp;1) Make your Arduino connections as I show in the pictures.<a href="#arduino"><sup>[1]</sup></a> <br>
&emsp;2) If you use different analog input don't forget to change Arduino code. <br>
&emsp;3) In python import the project:<br>
&emsp;&emsp;<code>from VolumeChangerArduino import VolumeChangerArduino</code><br>
&emsp;&emsp;Assign the class object to your variable:<br>
&emsp;&emsp;<kbd>x = VolumeChangerArduino(port, baudrate, sleeptime)</kbd><br>
&emsp;&emsp;&emsp;<code><kbd>port</kbd>: Arduino port as string. (port="COM6")</code><br>
&emsp;&emsp;&emsp;<code><kbd>baudrate</kbd>: Arduino baudrate as int. (baudrate=115200)</code><br>
&emsp;&emsp;&emsp;<code><kbd>sleeptime</kbd>: Waiting time before passing next loop to get serial input in seconds as int. (sleeptime=0.001)</code>
</p>

<h2><b>Images</b></h2>
<h3 id="arduino">&emsp;<b>Arduino Circuit</b></h3>
<p align="center">&emsp;<kbd>1kOhm</kbd> constant resistor used | <kbd>100kOhm</kbd> potentiometer used.</p>
<p align="center"><img src="/images/circuit.png"><br></p>
<h3>&emsp;<b>Why are there too much function created with curve_fit?</b></h3>
<p>&emsp;Because if single function used, it's error rises too much as shown in the picture.</p>
<p align="center"><img src="/images/setup_graph.png"></p>
