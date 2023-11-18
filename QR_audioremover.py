from moviepy.editor import VideoFileClip
#added by steven miller on 10/30/2023
#description: removes sound from target video to prevent errors
#source: https://thepythoncode.com/assistant/transformation-details/python-script-to-remove-audio-from-video/
###########ENTER VIDEO NAME HERE###########
videoname = "GH013693.mp4"
silentdirectory = "silentvideooutput"
threadnum = 8
#def remove_audio_from_video(videoname):

#create directory if needed

#UNCOMMENT THESE TWO LINES BELOW IF YOU WANT A SEPERATE DIRECTORY
#if not os.path.exists(silentdirectory):
 #   os.mkdir(silentdirectory)
#UNCOMMENT THESE TWO LINES ABOVE IF YOU WANT A SEPERATE DIRECTORY
        
# Load the video
video = VideoFileClip(videoname)
    
# Remove the audio
video_without_audio = video.without_audio()
# Write the result to a file
video_without_audio.write_videofile(videoname.split('.')[0] + "_no_sound"+ "." + videoname.split('.')[1] ,fps = 60,
                                    codec='libx264', audio = False, write_logfile = False,verbose = False, threads = threadnum, logger = 'bar')
