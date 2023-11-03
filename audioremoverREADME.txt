A couple preliminary points:
this audio remover is resource intensive, its recommended you run this on a
multicore system. As this script can take advantage of multiple threads.

To enable more cores on your system on windows 10/11:
1. Open search bar, type in "System Configuration".
2. go to the "boot" tab and select "advanced options"
3. you should see a checkbox with text "number of processors" and a drop down box
4. check the box and click the drop down, if more than 1 processor shows up,
you have a multicore cpu.
5. check the number of processors desired, then hit "ok"
6. the "advanced options" window will close, in the "System Configuration" window,
hit "apply"
7. you will need to reboot your computer for this change to take effect

How to use the audio remover:
1. open the python file in your IDE of choice.
2. under "videoname" type in the video name you want to remove audio from make sure to include the video type
3. if you have multiple cores in your cpu (see preliminary points above), 
type in the number of threads you want the script to use under "threadnum".
4. if you want a seperate directory for the video to be exported to, uncomment the two
lines specified in the source file
5. run the python script as you normally would, a status screen should pop up.
The text will be in red, this is normal.
6. If an error pops up, check to make sure the video actually got exported,
sometimes it will throw errors when the video comes out fine.
