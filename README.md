# VolumeChangerArduino
**Summary:** Designed for changing computer volume with potentiometer.
## **How do you setup?**
    **1)** Make your Arduino connections as I show in the [pictures](#arduino).
    **2)** If you use different analog input don't forget to change Arduino code.
    **3)** In python import the project:
        ```python from VolumeChangerArduino import VolumeChangerArduino```
        Assign the class object to your variable:<br>
        <code><var>yourVariable</var> = VolumeChangerArduino(<kbd>port</kbd>, <kbd>baudrate</kbd>, <kbd>sleeptime</kbd>)</code><br>
            <kbd>port</kbd>: Arduino port as string. (port="COM6")<br>
            <kbd>baudrate</kbd>: Arduino baudrate as int. (baudrate=115200)<br>
            <kbd>sleeptime</kbd>: Waiting time before passing next loop to get serial input in seconds as int. (sleeptime=0.001)<br>
    <b>4)</b> Run the app:<br>
    &emsp;<code><var>yourVariable</var>.run()</code>


<h2><b>Images</b></h2>
<h3 id="arduino">&emsp;<b>Arduino Circuit</b></h3>
<p align="center">&emsp;<kbd>1kOhm</kbd> constant resistor used | <kbd>100kOhm</kbd> potentiometer used.</p>
<p align="center"><img src="/images/circuit.png" width=40% height=auto><br></p>
<h3>&emsp;<b>Why are there too much function created with curve_fit?</b></h3>
<p>&emsp;Because if single function used, it's error rises too much as shown in the picture.</p>
<p align="center"><img src="/images/setup_graph.png" width=40% height=auto></p>
