# AI Text Completion App

An interactive command-line chatbot interface allowing users to prompt via the Cohere API.

## Setup

- I initialized a Cohere client using my API key to make requests to LLMs running in the background.
- The chatbot consists of two crucial functions:
  - `generate_response()`: Handles text generation using Cohere, allowing me to fine-tune the parameters to generate better responses.
  - `run__session()`: Manages the interactive user session to interact with the chatbot.

## Usage

Command to run the application:

python3 text_completion_app.py

## Fine-tuning Parameters

Adjust these parameters in `generate_response()` to control the output:

- `temperature` (0.0-2.0): Controls randomness

  - Lower (0.1): More focused, deterministic responses
  - Higher (0.9): More creative, varied responses

- `max_tokens` (1-2048): Controls response length

  - Lower (100): Shorter, concise responses
  - Higher (600): Longer, detailed responses

- `k` (0-500): Number of tokens to consider for each step

  - Lower: More focused on likely tokens
  - Higher: More diverse vocabulary

- `p` (0.0-1.0): Nucleus sampling

  - Lower (0.1): More conservative choices
  - Higher (0.9): More diverse choices

- `frequency_penalty` (0.0-1.0): Reduces repetition

  - Higher values discourage repeated words/phrases

- `presence_penalty` (0.0-1.0): Encourages new topics
  - Higher values encourage covering new topics

## Dependencies

- `cohere`: Powers the text generation using Cohere's language models
