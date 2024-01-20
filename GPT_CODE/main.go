package main

import (
	"encoding/json"
	"fmt"
	"github.com/go-resty/resty/v2"
	"log"
	"os"
	"github.com/joho/godotenv"
)

// Function to retrieve environment variable
func goDotEnvVariable(key string) string {
	err := godotenv.Load(".env")
	if err != nil {
		log.Fatalf("Error loading .env file")
	}
	return os.Getenv(key)
}

var openaiApiKey string

func main() {
	openaiApiKey = goDotEnvVariable("OPENAI_API_KEY") 
	//fmt.Println("OpenAI API Key:", openaiApiKey)

	client := resty.New()

	query := getUserInput("Ask me something: ")

	response, err := queryOpenAI(client, query)
	if err != nil {
		fmt.Println("Error querying OpenAI:", err)
		os.Exit(1)
	}

	var jsonResponse map[string]interface{}
	err = json.Unmarshal([]byte(response), &jsonResponse)
	if err != nil {
		fmt.Println("Error parsing JSON response:", err)
		os.Exit(1)
	}

	// Access the 'choices' field
	choices, ok := jsonResponse["choices"].([]interface{})
	if !ok || len(choices) == 0 {
		fmt.Println("Invalid response format")
		os.Exit(1)
	}

	answer := choices[0].(map[string]interface{})["message"].(map[string]interface{})["content"].(string)
	fmt.Println("ChatGPT's response:", answer)
}


func getUserInput(prompt string) string {
	fmt.Print(prompt)
	var input string
	fmt.Scanln(&input)
	return input
}

func queryOpenAI(client *resty.Client, query string) (string, error) {
	url := "https://api.openai.com/v1/chat/completions"
	headers := map[string]string{
		"Content-Type":  "application/json",
		"Authorization": "Bearer " + openaiApiKey,
	}

	payload := map[string]interface{}{
		"model": "gpt-3.5-turbo",
		"messages": []map[string]interface{}{
			{
				"role": "system",
				"content": "You are a helpful assistant.",
			},
			{
				"role": "user",
				"content": query,
			},
		},
	}

	response, err := client.R().
		SetHeaders(headers).
		SetBody(payload).
		Post(url)

	if err != nil {
		return "", err
	}

	return response.String(), nil
}
