#!/usr/bin/env python
# coding: utf-8

# # Python Lab Project
# ### Speech Recognition - Speech to Text

# submitted by (Group members) -<br><br> 
#      &emsp; 1. Saumel Verma<br>
#      &emsp; &emsp; &emsp; Scholar number: 191112013 (CSE-1) <br><br>
#      &emsp; 2. Prashant Kaushal<br>
#      &emsp; &emsp; &emsp; Scholar number: 191112473 (CSE-3) <br><br>
#      &emsp; 3. Nikhil Singh Parihar<br>
#      &emsp; &emsp; &emsp; Scholar number: 191112409 (CSE-3) <br><br>

# ### Lets have an adea of what is actually Speech Recognition ?

# ![8f43f25c53c3-4.png](attachment:8f43f25c53c3-4.png)

# Speech recognition, or speech-to-text, is the ability for a machine or program to identify words spoken aloud and convert them into readable text. An elementary speech recognition software has a limited vocabulary of words and phrases, and it may only identify these if they are spoken very clearly.

# ![using-googles-speech-api-for-language-instruction-1-638.png](attachment:using-googles-speech-api-for-language-instruction-1-638.png)
# The Web Speech API aims to enable web developers to provide, in a web browser, speech-input and text-to-speech output features that are typically not available when using standard speech-recognition or screen-reader software. <br>
# The API itself is agnostic of the underlying speech recognition and synthesis implementation and can support both server-based and client-based/embedded recognition and synthesis. The API is designed to enable both brief (one-shot) speech input and continuous speech input.

# ## Here is the code for Speech-to-text conversion by Speech Recognition

# In[9]:


import speech_recognition as sr
SampleRate = 46000
ChunkSize = 4096
# Initialize the recognizer
r = sr.Recognizer()

print('''Ways to supply input audio : \npress 1 to give input by microphone
press 2 to give input by audio file *(file must be in .wav format)''')

choice = int(input())
if choice == 1:
    with sr.Microphone(device_index=None, sample_rate=SampleRate, chunk_size=ChunkSize) as source:
        # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("start speaking ")
        # listens for the user's input
        audio = r.listen(source)
if choice == 2:
    src = input("enter the name of audio file present at location where notebook file is present : ")
    try:
        input_audio_file = sr.AudioFile(src)
        with input_audio_file as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
    except:
        input_audio_file = sr.AudioFile(src + ".wav")
        with input_audio_file as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
    
    print("please wait: audio file is runnning to extract text....", end="" )

try:
    text = r.recognize_google(audio)
    if choice == 1:
        print("you said: " + text)
    else:
        print("...done")

# error occurs when google could not understand what was said

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


# In[10]:


# code to save text file 

output = "{}".format(text)
with open("outputs.txt","a") as f:
    f.write(output + "\n")
print("please check! text file has been saved.")
    


# In[ ]:




