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
