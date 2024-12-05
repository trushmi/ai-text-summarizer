# Text Summarizer
# In this ReadMe:
- [About this project](#about-this-project)
- [Features](#features)
- [Tech stack](#tech-stack)
- [How to use the app](#how-to-use-the-app)
- [How to run the app](#how-to-run-the-app)

## About this project

Text Summarizer is a web application designed to provide quick and efficient summaries of large texts. It uses an advanced NLP model to extract the essence of the input text, providing users with concise summaries.

## Features

- User-friendly interface for easy text input and summary display.
- Supports text length from 200 to 100,000 characters.
- Real-time validation of input text.
- Loader animation to indicate processing.
- Responsive design for various devices.

## Tech stack
 - Python
 - Flask
 - API:
     [Hugging Face](https://huggingface.co/)

## How to use the app
1. Open the application.
2. Paste the text you want to summarize into the input text area.
3. Click the 'Summarize' button to receive a summary.
4. Use the 'Reset' button to clear all fields and start over.


## How to run the app

 > [!NOTE]
> You need a Hugging Face account for API access (to use the text summarization service)
 

1.  ### Clone the repository:
```
git clone [repository URL]
```   
2.  ### Navigate to the project directory:
```
cd [project name]
```
3. ### Set up a virtual environment:
```
python3 -m venv venv
```
4. ### Activate virtual environment
```
source venv/bin/activate
```
5. ### Install the required Python packages:
```
pip install -r requirements.txt
```
6. ###  Create a secrets.sh file in your project directory to store  Hugging Face API token
```
touch secrets.sh
```

7. ### Include the following environment variables into secrets.sh file:
```
export ACCESS_TOKEN='your_huggingface_api_token'
```
8. ### Source the secrets.sh file to set the environment variable:
```
source secrets.sh
```
 9. ### Run the Application
```
python3 server.py
```
10. ### Open your web browser and navigate to the following address:
```
http://localhost:5000/
```
You should now see the application running. If you encounter any issues, please check that all previous steps have been followed correctly.

________________________
See my other project, [Text Summarizer](https://github.com/trushmi/ai-text-summarizer), a web application designed to provide quick and efficient summaries of large texts.
