from pydub import AudioSegment
from pydub.utils import which
import imageio_ffmpeg as ffmpeg
import os

# Explicitly set the ffmpeg path for pydub
ffmpeg_path = ffmpeg.get_ffmpeg_exe()
if not os.path.exists(ffmpeg_path):
    raise FileNotFoundError("FFmpeg executable not found at {}".format(ffmpeg_path))

AudioSegment.converter = ffmpeg_path

# Process the audio file
audio = AudioSegment.from_wav("Output.wav")

# Increase the volume by 6dB
# audio = audio + 6

audio = audio * 2

audio = audio.fade_in(2000)

audio.export("mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("mashup.mp3")
print("done")
