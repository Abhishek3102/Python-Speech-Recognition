import wave

obj = wave.open("Triple-H-The-Game.wav","rb")

print("Number of channels :", obj.getnchannels())
print("Sample width :", obj.getsampwidth())
print("Frame Rate :", obj.getframerate())
print("Nnumber of frames :", obj.getnframes())
print("Parameters :", obj.getparams())