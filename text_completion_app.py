import cohere

# Method used to generate a completion for a prompt
def generate_response(prompt, co):
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty")

    try:
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=600,
            temperature=0.8,
            k=0,
            stop_sequences=[],
            return_likelihoods='NONE'
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error generating completion: {str(e)}"

# Purpose: To run a user session for continuous text completion.
def run__session(co):
    print("Welcome to my Text Completion App!")
    print("Type 'quit' or 'exit' to end the session")
    print("*" * 55)

    while True:
        try:
            # Get user input
            user_input = input("\nEnter your prompt: ").strip(" \t\n\r,")

            # Validate for for quit or exit commands
            if user_input.lower() in ['quit', 'exit']:
                print("Thank you for using the Text Completion App!")
                break

            # Validate input for empty prompt
            if not user_input:
                print("Error: Prompt cannot be empty. Please try again.")
                continue

            # Generate and display completion
            print("\nGenerating response...\n")
            completion = generate_response(user_input, co)
            print("Response:")
            print("*" * 50)
            print(completion)
            print("*" * 50)
        # For performing Control-C to terminate the user's session
        except KeyboardInterrupt:
            print("\nSession terminated by user.")
            break
        # For any other exceptions that may pop up.
        except Exception as e:
            print(f"An error occurred: {str(e)}")

try:
    # Set the API key manually
    api_key = "Rb0iaoEFiazuLXvSSuPcnqpx4pd3Z79kHAVMhhfC" #API key for Cohere, reset it for your own use.
    # Configure the cohere client with that api key
    co = cohere.Client(api_key)
    # Run an interactive session, which will generate completion per user input in the session
    run__session(co)
except Exception as e:
    print(f"Failed to initialize the app: {str(e)}")