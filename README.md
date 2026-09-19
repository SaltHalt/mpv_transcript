# MPV Transcript Viewer

Shows the live transcript of the current video in mpv, within a separate terminal window.

To use, run your mpv window with the IPC flag: `mpv --input-ipc-server=\\pipe\mpv_transcript_socket video.mp4`. Or stick: `input-ipc-server=\\pipe\mpv_transcript_socket` into your config file. 
You may find the ability to add flags on Windows shortcuts helpful.
 
Then execute `transcript.py`. (Alternatively use the exe generated from the makefile)

Note that the terminal dimensions are hardcoded.
Also I think this will only work with video files that have .srt subtitles.
