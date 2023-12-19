# mpv --input-ipc-server=\\pipe\mpv_transcript_socket filian.mp4
# Shows all open pipes that contain 'mpv' in their name
#[System.IO.Directory]::GetFiles("\\.\\pipe\\") | findstr "mpv"

from python_mpv_jsonipc import MPV
import os
mpv = MPV(start_mpv=False, ipc_socket=r"\\pipe\mpv_transcript_socket")
print("Connection successful.")
CACHE_DIR = r"C:\Programs\mpv\portable_config\transcript\cache"

FILE_DIR = os.path.join(mpv.working_directory,mpv.path)
FILENAME = os.path.basename(FILE_DIR)

print(CACHE_DIR, FILE_DIR, FILENAME)
# os.system()

# @mpv.on_key_press("R")
# def init_transcript():
#     pass


