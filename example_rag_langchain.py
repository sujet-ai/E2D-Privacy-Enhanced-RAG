# Import the necessary modules
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from E2D import EntityEncoderDecoder

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "Insert Your API Key Here..."


# Define the main function
def main():
    # Open the example text file and read its contents
    with open("example.txt", "r") as file:
        context = file.read()

    # Define the question to be answered
    question = ("What were the total operating expenses for Universal Holdings Ltd. in 2023 and how did they compare "
                "to the previous year?")

    # Create an instance of the EntityEncoderDecoder class
    e2d = EntityEncoderDecoder()

    # Encode the entities in the context and question using the EntityEncoderDecoder instance
    encoded_context = e2d.encode_entities(context)
    encoded_question = e2d.encode_entities(question)

    # Define the prompt template to be used by the language model
    prompt = PromptTemplate(
        template="Answer the question using the given context.\nQuestion: {question}\nContext: {context}\nAnswer:",
        input_variables=["question", "context"])

    # Create an instance of the OpenAI language model
    llm = OpenAI()

    # Create an instance of the LLMChain class using the language model and prompt template
    chain = LLMChain(llm=llm, prompt=prompt)

    # Use the LLMChain instance to generate a response to the encoded question and context
    encoded_response = chain.run({"question": encoded_question, "context": encoded_context})

    # Decode the entities in the encoded response using the EntityEncoderDecoder instance
    decoded_response = e2d.decode_entities(encoded_response)

    # Use the LLMChain instance to generate a response to the original question and context
    response = chain.run({"question": question, "context": context})

    # Print the decoded response and the original response
    print("The E2C response is: ", decoded_response)
    print("The normal response is: ", response)


# Call the main function if the script is run directly
if __name__ == "__main__":
    main()
