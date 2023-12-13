DISCLAIMER: REMOVING AUDIO IS ONLY NECESSARY FOR 4K QUALITY VIDEOS: removing audio prevents running out of memmory
before the video is finished creating

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

you will need "moviepy", open a command prompt window and type in:
"pip install moviepy"
after its installed, proceed below:

How to use the audio remover:
1. open the python file in your IDE of choice.
2. under "videoname" type in the video name you want to remove audio from make sure to include the video type
3. if you have multiple cores in your cpu (see preliminary points above), 
type in the number of threads you want the script to use under "threadnum".
4. if you want a seperate directory for the video to be exported to, uncomment the two
lines specified in the source file
5. save your changes and run the "runaudioremover.bat" file
6. a command prompt window will open up along with a status bar, this may take some time depending
on the length of your video and how many threads you specified.
