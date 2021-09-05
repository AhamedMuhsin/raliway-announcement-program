# importing module used in this program
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3("railway.mp3")

    # 1 - Generate may I have your attention please
    start = 111000
    finish = 115700
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3", format="mp3")

    # 2 - is train name and train no

    # 3 - is from-city
    start = 122800
    finish = 123400
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_english.mp3", format="mp3")

    # 5 - is to-city
    start = 124200
    finish = 124900
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_english.mp3", format="mp3")

    # 7 - is via-city
    start = 126000
    finish = 127000
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_english.mp3", format="mp3")

    # 9 - Generate is arrving shortly on platform no
    start = 128900
    finish = 132500
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_english.mp3", format="mp3")

    # 10 - is platform no

    # 11 - Generate song
    start = 133500
    finish = 134500
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_english.mp3", format="mp3")

def generateAnnocement(filepath, engine):
    df = pd.read_excel('C:\\Users\\MUHSIN\\My Projects\\raliway annocement\\announce_english.xlsx', engine='openpyxl')
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate train no and train name
        textToSpeech(item['train_no'] + " " + item['train_name'], "2_english.mp3")
        
        # 4 - Generate from-city
        textToSpeech(item['from'], "4_english.mp3")

        # 6 - Generate to-city
        textToSpeech(item['to'], "6_english.mp3")

        # 8 - Generate via-city
        textToSpeech(item['via'], "8_english.mp3")

        # 10 - Generate platform number
        textToSpeech(item['platform'], "10_english.mp3")

        audios = [f"{i}_english.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now generating Annocement...")
    generateAnnocement('C:\\Users\\MUHSIN\\My Projects\\raliway annocement\\announce_english.xlsx', engine='openpyxl')




