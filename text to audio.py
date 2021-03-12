import pyttsx3
from winsound import PlaySound

def speak(text, filename):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty("voices")[0]
    engine.setProperty('voice', voices)
    engine.save_to_file(text, f"{filename}.mp3")
    engine.runAndWait()
    PlaySound(f"{filename}.mp3", True)
    print("File has been converted to {}.mp3. Now playing the file".format(filename))
    input("Hit enter to Complete!!!")

if __name__ == '__main__':
    data = []
    filename = input('Filename: ')
    print('Start Writing, We are Transcribing')
    while True:
        text = input("")
        if text == '':
            break
        else:
            data.append(text)
    print("Converting into Audio: {}.mp3\r".format(filename), end="")
    data = '\n'.join(data)
    speak(data, filename)