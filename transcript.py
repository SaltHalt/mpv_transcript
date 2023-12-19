import mpv
player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True, ytdl=True)
player.play('https://youtu.be/DOmdB7D-pUU')
player.wait_for_playback()

# mp.get_property("path")