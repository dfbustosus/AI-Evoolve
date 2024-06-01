# Import necessary libraries
import openai

class OpenAIClient:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_text(self, prompt, max_tokens=50):
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=max_tokens)
        return response.choices[0].text.strip()

    def chat_completions(self, messages):
        response = openai.ChatCompletion.create(engine="gpt-3.5-turbo", messages=messages)
        return response.choices[0].message.content

    def image_generation(self, prompt):
        response = openai.Image.generate(prompt)
        return response['data'][0]['url']

    def text_to_speech(self, text):
        response = openai.Audio.create(engine="text-to-speech", text=text)
        return response['url']

    def speech_to_text(self, audio_file_path):
        with open(audio_file_path, 'rb') as f:
            response = openai.Audio.recognize(engine="speech-to-text", file=f)
        return response['result'][0]['alternatives'][0]['transcript']

if __name__ == "__main__":
    api_key = "your-openai-api-key"
    client = OpenAIClient(api_key)

    prompt = "What is the capital of France?"
    print("Generated text:", client.generate_text(prompt))

    messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}]
    print("Chat completions:", client.chat_completions(messages))

    prompt = "A cat in a hat"
    print("Image generation URL:", client.image_generation(prompt))

    text = "Hello, World!"
    print("Text-to-speech URL:", client.text_to_speech(text))

    audio_file_path = "path/to/your/audio/file"
    print("Speech-to-text transcript:", client.speech_to_text(audio_file_path))