import mpv
# plugins=['file-browser','uosc']   
# player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True, ytdl=True)
player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True)
player['scripts'] = [r'C:\Programs\mpv\portable_config\scripts\file-browser.lua']
player.play(r'D:\Downloads\1_delete\filian.mp4')
player.wait_for_playback()
# mp.get_property("path")