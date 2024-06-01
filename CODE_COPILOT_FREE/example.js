// HTML for the webpage
const html = `
  <html>
    <head>
      <title>My Web Page</title>
      <style>
        body {
          font-family: Arial, sans-serif;
        }
        h1 {
          color: #333;
        }
        p {
          line-height: 1.5;
        }
      </style>
    </head>
    <body>
      <h1>Welcome to my Web Page!</h1>
      <p>This is a simple example of a web page using HTML and JavaScript.</p>
      <script src="main.js"></script>
    </body>
  </html>
`;

// JavaScript for the webpage
const script = `
  document.addEventListener('DOMContentLoaded', () => {
    const h1 = document.querySelector('h1');
    h1.textContent = 'Hello, world!';
  });
`;

// Create a file with HTML content and save it to disk
const fs = require('fs');
fs.writeFileSync('index.html', html);

// Write JavaScript code to a new file and save it to disk
fs.writeFileSync('main.js', script);

// Open the web page in a browser window for testing
const { exec } = require('child_process');
exec(`start http://localhost:3000 && cd ${__dirname} && npx live-server`, (err, stdout, stderr) => {
  if (err) throw err;
  console.log(stdout);
});
