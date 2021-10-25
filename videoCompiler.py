import os
os.system('ffmpeg -f concat -safe 0 -i video_list.txt -c copy chill2_15m.mp4')
#os.system('ffmpeg -i output1.mp4 -i audio_output.mp3 -map 0:v -map 1:a -c:v copy -shortest FINALE.mp4')
