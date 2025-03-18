# CS 463 Final Project 

## About the Project
The purpose of this project is to create a personal portfolio to highlight
me and my CS career. It also has a backend that is used for using the users input
to send a message to the LLM (google gemini) and get a response back.
It is a python flash server that is deployed to heroku. 

Link here: https://cfarhan-f9900dc398ab.herokuapp.com/

## Sources used
The majority of my sources for this project were the course slides and
previous assignments. For the LLM portion of the project, I used previou
assignments from CS410P: Generative Security AI with professor Feng at PSU.

## How to run locally
1. While in the root directory first install the required libraries: pip install -r requirements.txt
2. Create a new local folder called .env and add your google gemini api key: GEMINI_KEY=<your key here>
3. cd into fullstack
4. Run via: flask --app app run
5. Terminal should give you what local port it's deployed to, for me its: http://127.0.0.1:5000