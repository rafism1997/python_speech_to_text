import wave 
import matplotlib.pyplot as plt
import numpy as np 

obj = wave.open("Fanfare60.wav","rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1) # bytes object , need to call a numpy array for this 

t_audio = n_samples / sample_freq

print(t_audio)


signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times =np.linspace(0,t_audio, num=n_samples) # x axis 

plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0,t_audio)
plt.show()
