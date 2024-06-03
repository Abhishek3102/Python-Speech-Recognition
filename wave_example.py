import wave

obj = wave.open("Triple-H-The-Game.wav","rb")

print("Number of channels :", obj.getnchannels())
print("Sample width :", obj.getsampwidth())
print("Frame Rate :", obj.getframerate())
print("Nnumber of frames :", obj.getnframes())
print("Parameters :", obj.getparams())

time_of_audio = obj.getnframes() / obj.getframerate()
print("The time of audio in seconds is :", time_of_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))