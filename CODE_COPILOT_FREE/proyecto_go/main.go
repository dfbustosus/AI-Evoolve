package main

import (
	"fmt"
	"net/http"
)

// Define your handler for handling GET requests
func getHandler(w http.ResponseWriter, r *http.Request) {
	// Write response to the client
	fmt.Fprint(w, "This is a GET request")
}

// Define another handler for handling POST requests
func postHandler(w http.ResponseWriter, r *http.Request) {
	// Read request body and handle it
	var data string
	r.ParseForm()
	data = r.FormValue("some_key")
	fmt.Fprintf(w, "This is a POST request with data: %s", data)
}

func main() {
	// Register your handlers with the appropriate HTTP methods and paths
	http.HandleFunc("/get", getHandler)
	http.HandleFunc("/post", postHandler)

	// Start the server on port 8080
	fmt.Println("Server started on port 8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		panic(err)
	}
}
