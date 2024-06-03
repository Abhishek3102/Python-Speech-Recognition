import wave
import matplotlib.pyplot as plt
import numpy as np

# Open the wave file
obj = wave.open("Triple-H-The-Game.wav", "rb")

# Extract basic information
sample_frequency = obj.getframerate()
n_samples = obj.getnframes()
n_channels = obj.getnchannels()
sample_width = obj.getsampwidth()

# Read frames and close the file
signal_wave = obj.readframes(-1)
obj.close()

# Calculate audio time
audio_time = n_samples / sample_frequency
print("The time of audio in seconds is :", audio_time)

# Determine the data type based on sample width
if sample_width == 1:
    dtype = np.uint8  # 8-bit PCM
elif sample_width == 2:
    dtype = np.int16  # 16-bit PCM
else:
    raise ValueError("Unsupported sample width: {}".format(sample_width))

# Ensure the buffer size is a multiple of the element size
element_size = sample_width * n_channels
buffer_size = len(signal_wave)
if buffer_size % element_size != 0:
    adjusted_size = buffer_size - (buffer_size % element_size)
    signal_wave = signal_wave[:adjusted_size]

# Convert buffer to an array with appropriate data type and shape
signal_array = np.frombuffer(signal_wave, dtype=dtype)

# Reshape the array to separate channels if stereo
if n_channels == 2:
    signal_array = np.reshape(signal_array, (-1, 2))

# Create time axis
# Ensure that the number of time points matches the number of samples in signal_array
times = np.linspace(0, audio_time, num=signal_array.shape[0])

# Plotting the audio signal
plt.figure(figsize=(15, 5))
if n_channels == 2:
    plt.plot(times, signal_array[:, 0], label='Left Channel')
    plt.plot(times, signal_array[:, 1], label='Right Channel')
else:
    plt.plot(times, signal_array, label='Mono Channel')

plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0, audio_time)
plt.legend()
plt.show()
