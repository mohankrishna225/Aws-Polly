import boto3
from pygame import mixer
import os
polly = boto3.client('polly')
matter = input("Enter the text you want to synthesize_speech= ")
spoken_text = polly.synthesize_speech(Text=matter,
                                      OutputFormat='mp3',VoiceId='Emma')



with open('output.mp3', 'wb') as f:
	f.write(spoken_text['AudioStream'].read())
	f.close

mixer.init()
mixer.music.load('output.mp3')
mixer.music.play()

while mixer.music.get_busy() == True:
     pass

mixer.quit()
os.remove('output.mp3')
