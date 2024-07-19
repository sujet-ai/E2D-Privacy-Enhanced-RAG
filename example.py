# Import the EntityEncoderDecoder class from the E2D module
from sujet_ai import EntityEncoderDecoder


# Define the main function
def main():
    # Create an instance of the EntityEncoderDecoder class
    e2d = EntityEncoderDecoder()

    # Define a text containing named entities
    text = "Apple Inc. was founded by Steve Jobs and Steve Wozniak on April 1, 1976."

    # Encode the entities in the text using the EntityEncoderDecoder instance
    encoded_text = e2d.encode_entities(text)

    # Print the encoded text
    print("The encoded text is: ", encoded_text)
    # Output: "ORG_0 was founded by PERSON_0 and PERSON_1 on DATE_0."

    # Decode the entities in the encoded text using the EntityEncoderDecoder instance
    decoded_text = e2d.decode_entities(encoded_text)

    # Print the decoded text
    print("The decoded text is: ", decoded_text)
    # Output: "Apple Inc. was founded by Steve Jobs and Steve Wozniak on April 1, 1976."


# Call the main function if the script is run directly
if __name__ == "__main__":
    main()
