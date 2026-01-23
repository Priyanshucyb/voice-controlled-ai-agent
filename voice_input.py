import speech_recognition as sr


def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5)

        text = r.recognize_google(audio)
        return text.lower()

    except sr.WaitTimeoutError:
        print("Timeout: kuch bola nahi")
        return ""

    except sr.UnknownValueError:
        print("Samajh nahi aaya, dubara bolo")
        return ""

    except sr.RequestError as e:
        print(f"Speech service error: {e}")
        return
