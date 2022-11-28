import wave

# Audio signal paramters 
# number of channels 
# sample width 
# framerate /sample_rate - Number of samples for each second - 44,100 Hz (Standard) 
#- number of frames 
# values of a frame
# 
obj = wave.open("Fanfare60.wav","rb")

print("Number of channels",obj.getnchannels())
print("Sample width",obj.getsampwidth())
print("frame rate",obj.getframerate())
print("Number  of frames",obj.getnframes())
print("parameters",obj.getparams())

audio_time_in_secs = obj.getnframes() / obj.getframerate()
print(audio_time_in_secs)

# to understand the number of frames in a wave file w.r.t sample width being 2
frames = obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames))
print(len(frames) / 2)