# mpv --input-ipc-server=\\pipe\mpv_transcript_socket video.mp4
# Shows all open pipes that contain 'mpv' in their name
#[System.IO.Directory]::GetFiles("\\.\\pipe\\") | findstr "mpv"

from python_mpv_jsonipc import MPV
import os
import pickle
import srt
from datetime import timedelta
from bisect import bisect
from colorama import init
from colored import stylize, fore, back
#TODO: insert try-catch here
mpv = MPV(start_mpv=False, ipc_socket=r"\\pipe\mpv_transcript_socket")
print("Connection successful.")
CACHE_DIR = r"C:\Programs\mpv\portable_config\transcript\cache"

FILE_DIR = mpv.path #os.path.join(mpv.working_directory, mpv.path)
FILENAME = os.path.basename(FILE_DIR)

 
def generateSRT(mp4_dir, srt_dir):
    extract_subtitles = f"ffmpeg -i \"{mp4_dir}\" \"{srt_dir}\""
    os.system(extract_subtitles) #TODO: error detection by taking the exit code here

def generatePKL(srt_dir, pkl_dir):
    reformat_sub = lambda sub : (sub.start, sub.content)
    subtitles = srt.parse(open(srt_dir, "r").read())
    subtitle_list = list(map(reformat_sub, subtitles))
    with open(pkl_dir, 'wb') as file:
        pickle.dump(subtitle_list, file)

SRT_DIR = os.path.join(CACHE_DIR, os.path.splitext(FILENAME)[0]+'.srt')
PKL_DIR = os.path.join(CACHE_DIR, os.path.splitext(FILENAME)[0]+'.pkl')
if not os.path.isfile(SRT_DIR): 
    generateSRT(FILE_DIR, SRT_DIR)
if not os.path.isfile(PKL_DIR):
    generatePKL(SRT_DIR, PKL_DIR)
with open(PKL_DIR, 'rb') as f: #Consider doing try {f = open)} catch {} else{with f:}
  subtitle_list = pickle.load(f)

print("Loading complete")

WIDTH = 110
HEIGHT = 25
HALF = int((HEIGHT-1)/2)
# CENTRE_POS = (HEIGHT+1)/2
os.system(f'MODE {WIDTH},{HEIGHT}')
os.system("COLOR F0")
init()

os.system(f'MODE {WIDTH},{HEIGHT}')
import time
while True:
    time.sleep(0.3)
    n_subs = len(subtitle_list)
    #TODO There could be a bug where the highlighted subtitle is a bit later than the current sub in the video
    now = timedelta(seconds=mpv.time_pos) 
    i = bisect(subtitle_list, (now, "")) - 1
    n_subs_before = i
    n_subs_after = n_subs - i - 1
    output = ""
    if(n_subs_before < HALF):
        start = 0;
        end = HEIGHT;
    elif(n_subs_after < HALF):
        start = n_subs-HEIGHT;
        end = n_subs;
    else:
        start = i - HALF;
        end = i + HALF + 1;
    output = ""
    for j in range(start, end):
        timestamp = str(subtitle_list[j][0]).split('.')[0]
        sub_text = subtitle_list[j][1]
        line = f"{timestamp}| {sub_text}"
        format_current = lambda text : stylize(text.ljust(WIDTH, " "), fore('grey_3')+back(254))
        format_other = lambda text : stylize(text.ljust(WIDTH, " "), fore('grey_3')+back('white'))
        format = format_current if j==i else format_other
        output += format(line) + "\n"
    print(output[:-1], end = "")