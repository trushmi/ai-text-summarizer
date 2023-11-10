# Text Summarizer

## Overview

Text Summarizer is a web application designed to provide quick and efficient summaries of large texts. It uses an advanced NLP model to extract the essence of the input text, providing users with concise summaries.

## Features

- User-friendly interface for easy text input and summary display.
- Supports text length from 200 to 100,000 characters.
- Real-time validation of input text.
- Loader animation to indicate processing.
- Responsive design for various devices.

## How to Use

1. Open the application.
2. Paste the text you want to summarize into the input text area.
3. Click the 'Summarize' button to receive a summary.
4. Use the 'Reset' button to clear all fields and start over.

## Requirements

- Flask
- Python 3
- A Hugging Face account for API access (to use the text summarization service)

## Installation

To set up the project locally:

1. Clone the repository:
   ```
   git clone [repository URL]
   ```
2. Navigate to the project directory:

   ```
   cd [project name]
   ```

3. Set up a virtual environment:
   ```
   python3 -m venv venv
   ```
4. Activate virtual environment

   ```
   source venv/bin/activate
   ```

5. Install the required Python packages:

   ```
    pip install -r requirements.txt
   ```

6. Create a secrets.sh file to store your Hugging Face API token:

   ```
   echo "export ACCESS_TOKEN='your_huggingface_api_token'" > secrets.sh
   ```

7. Source the secrets.sh file to set the environment variable:

   ```
   source secrets.sh
   ```

8. Run the Flask application:

   ```
   python server.py
   ```

9. Open your web browser and navigate to localhost:5000 to use the application.

## Author

Iryna Trush, Software engineer with a strong background in the media industry and leadership.
[LinkedIn](https://www.linkedin.com/in/trushmi/), [email](trushmi415@gmail.com);
