from python_mpv_jsonipc import MPV
mpv = MPV(start_mpv=False, ipc_socket=r"\\pipe\mpv_transcript_socket")
@mpv.on_key_press("g")
def space_handler():
    print("Test")

#mpv --input-ipc-server=\\pipe\mpv_transcript_socket filian.mp4
#[System.IO.Directory]::GetFiles("\\.\\pipe\\") | findstr "mpv"
