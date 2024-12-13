import vlc
import time

stream_url = "https://thfradio2.out.airtime.pro/thfradio2_a"

player = vlc.MediaPlayer(stream_url)

print("Starte den Stream...")
player.play()

time.sleep(1800)

print("Beende den Stream...")
player.stop()
