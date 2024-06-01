// Import necessary dependencies for OpenAI services
use openai::Client;

// Define a function to generate text using OpenAI's chat completions API
fn generate_text(api_key: &str, prompt: &str) -> Result<String, openai::Error> {
    let client = Client::new(api_key);
    let mut request = client.chat().create();

    request.messages(&[openai::Message::system("You are a helpful assistant.")]).model("gpt-3.5-turbo");

    match request.message(prompt) {
        Ok(_) => (),
        Err(e) => return Err(e),
    };

    let response = request.send()?;
    Ok(response.choices[0].message.content.to_string())
}

// Define a function to generate an image using OpenAI's image generation API
fn generate_image(api_key: &str, prompt: &str) -> Result<String, openai::Error> {
    let client = Client::new(api_key);
    let mut request = client.images().generate();

    request.n(1).size("1024x1024").prompt(prompt);

    let response = request.send()?;
    Ok(response.data[0].url.to_string())
}

// Define a function to convert text to speech using OpenAI's text-to-speech API
fn text_to_speech(api_key: &str, text: &str) -> Result<String, openai::Error> {
    let client = Client::new(api_key);
    let mut request = client.audio().speech();

    request.text(text).model("eleven-tts");

    let response = request.send()?;
    Ok(response.url.to_string())
}

// Define a function to convert speech to text using OpenAI's speech-to-text API
fn speech_to_text(api_key: &str, url: &str) -> Result<String, openai::Error> {
    let client = Client::new(api_key);
    let mut request = client.audio().transcribe();

    request.model("whisper-1").file_url(url);

    let response = request.send()?;
    Ok(response.text.to_string())
}


