import speech_recognition as sr  # For speech-to-text functionality
import pyttsx3  # For text-to-speech functionality

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Process and execute the speech

# Function to listen to audio input from the user and convert it to text
def listen():
    recognizer = sr.Recognizer()  # Initialize the speech recognizer

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")  # Notify the user that listening has started
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        audio = recognizer.listen(source)  # Capture the audio input

    try:
        print("Recognizing...")  # Notify the user that recognition is in progress
        query = recognizer.recognize_google(audio)  # Use Google Speech Recognition to convert audio to text
        print(f"User said: {query}")  # Output the recognized text
        return query.lower()  # Return the text in lowercase
    except sr.UnknownValueError:
        # Handle case where speech is not understood
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        # Handle errors with the recognition service
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Function to process the user's query and respond accordingly
def assistant(query):
    if "hello" in query:
        speak("Hello! How can I help you?")  # Respond to greeting
    elif "how are you" in query:
        speak("I'm doing well, thank you!")  # Respond to inquiry about bot's well-being
    elif "what is your name" in query:
        speak("I am a voice assistant. You can call me Assistant.")  # Respond with the bot's name
    elif "exit" in query:
        speak("Goodbye!")  # Exit the program
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")  # Handle unknown commands

# Main program execution
if __name__ == "__main__":
    # Initial greeting from the assistant
    speak("Hello! I am your voice assistant.")

    # Continuously listen for commands in a loop
    while True:
        query = listen()  # Capture the user's voice input
        assistant(query)  # Process the input and respond
