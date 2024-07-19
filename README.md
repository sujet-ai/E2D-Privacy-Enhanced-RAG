[![PyPI - PyPi](https://img.shields.io/pypi/v/sujet-ai)](https://pypi.org/project/sujet-ai/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://sujet.ai)


# E2D
 Entity Encoder Decoder: A Privacy-Enhanced Framework for LLMs and RAG Agents

<img src="https://github.com/sujet-ai/E2D-Privacy-Enhanced-RAG/blob/main/diagram.png" alt="drawing" width="500"/>

## Description

With the implementation of the AI EU Act, privacy has become a paramount concern in the development and deployment of AI technologies. In response to these heightened privacy requirements, the E2D (Entity Encoder Decoder) framework emerges as a robust solution specifically designed to address these concerns. E2D is a privacy-enhanced framework tailored for Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) agents, offering a reliable mechanism for managing sensitive information and mitigating privacy risks. By securely encoding and decoding entities, the E2D framework ensures that delicate information is safeguarded during both the training and inference phases of AI model operations. This approach is especially beneficial for closed-source LLMs, providing an additional layer of security to prevent unauthorized access or misuse of sensitive data.

### Key Features

- **Privacy Preservation**: E2D ensures that sensitive entities are encoded securely, reducing the risk of data breaches.
- **Compatibility**: The framework can be integrated with various LLMs and RAG agents, making it versatile and adaptable.
- **Ease of Use**: Designed with usability in mind, E2D can be easily incorporated into existing AI workflows.
- **Regulatory Compliance**: By adopting E2D, organizations can align with the privacy requirements stipulated by the AI EU Act and other regulations.

### Components

1. **Entity Encoder**: This component encodes sensitive entities using advanced cryptographic techniques, ensuring that the original data cannot be easily reconstructed without authorization.
2. **Entity Decoder**: The decoder component allows for the secure retrieval of the original entities when necessary, ensuring that only authorized users can access the sensitive information.
3. **Integration Modules**: E2D provides modules for seamless integration with popular LLM frameworks and RAG agents.

## Examples

Below are examples of how to use the E2D framework with different applications.

### Example 1: Process of E2D

```python
from E2D import EntityEncoderDecoder

e2d = EntityEncoderDecoder()

text = "Apple Inc. was founded by Steve Jobs and Steve Wozniak on April 1, 1976."

# Encode the entities in the text using E2D
encoded_text = e2d.encode_entities(text)

print("The encoded text is: ", encoded_text)
# Output: "ORG_0 was founded by PERSON_0 and PERSON_1 on DATE_0."

# Decode the entities in the encoded text using E2D
decoded_text = e2d.decode_entities(encoded_text)

print("The decoded text is: ", decoded_text)
# Output: "Apple Inc. was founded by Steve Jobs and Steve Wozniak on April 1, 1976."
```

### Example 2: Integration of E2D with LangChain
```python
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from E2D import EntityEncoderDecoder

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "Insert Your API Key Here..."


# Define the question to be answered
question = ("What were the total operating expenses for Universal Holdings Ltd. in 2023 and how did they compare "
"to the previous year?")

# we assume the context is already retrieved.
# Open the example text file as a context containing "fake" sensetive information and read its contents
with open("example.txt", "r") as file:
    context = file.read()

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
print("The regular response is: ", response)
```

### Bibliography

To cite the E2D framework in your research or project, please use the following BibTeX reference:

```bibtex
@software{e2d2024,
  title={Entity Encoder Decoder: A Privacy-Enhanced Framework for LLMs and RAG Agents},
  author={Sujet AI, Hamed, Allaa, Aleks},
  year={2024},
  url = {https://github.com/sujet-ai/E2D-Privacy-Enhanced-RAG}
}
```
