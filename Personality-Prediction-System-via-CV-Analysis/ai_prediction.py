import google.generativeai as genai
from prediction import personality_traits
import pyttsx3

genai.configure(api_key="AIzaSyBhv5kk4SIT9l1Gataf3bakVbQQ7ZB42Do")
# proceed here for api key  https://makersuite.google.com/app/apikey



    # Your prediction logic here

    # Convert the contents to speech
    #engine.say(contents)
    #engine.runAndWait()

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
)

def chat(query):
    for _ in range(3):  # Retry up to 3 times
        try:
            response = model.generate_content([query])
            return response.text
        except Exception as e:
            print(f"Error occurred: {e}. Retrying...")
    return "Sorry, I'm unable to assist at the moment."

def say(text):
    print(f"Luna: {text}")

def takeCommand():
    try:
        query = "describe a candidate's personality if his traits are: " + ', '.join(f"{k}: {v}" for k, v in personality_traits.items())
        return query
    except Exception as e:
        return "Some Error Occurred. Sorry from Luna"

if __name__ == '__main__':
    query = takeCommand()
    response = chat(query)
    print(f"Luna: {response}")
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()
