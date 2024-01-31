import speech_recognition as sr
from googletrans import Translator

recognizer = sr.Recognizer()
translator = Translator()

def record_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio, language):
    try:
        text = recognizer.recognize_google(audio, language=language)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")
        return None

def translate_text(text, target_language='en'):
    translation = translator.translate(text, dest=target_language)
    return translation.text

if __name__ == "__main__":
    language_choice = input("Enter the language (hi for Hindi, bn for Bengali): ")

    if language_choice.lower() == 'hi':
        language_code = 'hi-IN'
    elif language_choice.lower() == 'bn':
        language_code = 'bn-IN'
    else:
        print("Invalid language choice. Exiting.")
        exit()

    audio = record_audio()
    spoken_text = recognize_speech(audio, language=language_code)

    if spoken_text:
        english_translation = translate_text(spoken_text)
        print(f"Translation (to English): {english_translation}")
