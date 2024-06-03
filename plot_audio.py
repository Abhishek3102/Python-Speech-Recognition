import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("Triple-H-The-Game.wav", "rb")

sample_frequency = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

audio_time = n_samples / sample_frequency
print("The time of audio in seconds is :", audio_time)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, audio_time, num = n_samples)

plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.title("Audio signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0, audio_time)
plt.show()
