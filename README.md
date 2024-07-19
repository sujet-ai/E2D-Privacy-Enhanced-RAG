[![PyPI - PyPi](https://img.shields.io/pypi/v/antm)](https://pypi.org/project/antm/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://hamedrahimi.fr)
[![arXiv](https://img.shields.io/badge/arXiv-2302.01501-<COLOR>.svg)](https://arxiv.org/abs/2302.01501)


![alt text](https://github.com/sujet-ai/E2D-Privacy-Enhanced-RAG/diagram.png?raw=true)

 Dynamic topic models are effective methods that primarily focus on studying the evolution of topics present in a collection of documents. These models are widely used for understanding trends, exploring public opinion in social networks, or tracking research progress and discoveries in scientific archives. Since topics are defined as clusters of semantically similar documents, it is necessary to observe the changes in the content or themes of these clusters in order to understand how topics evolve as new knowledge is discovered over time. Here, we introduce a dynamic neural topic model called ANTM, which uses document embeddings (data2vec) to compute clusters of semantically similar documents at different periods, and aligns document clusters to represent their evolution. This alignment procedure preserves the temporal similarity of document clusters over time and captures the semantic change of words characterized by their context within different periods. Experiments on four different datasets show that ANTM outperforms probabilistic dynamic topic models (e.g. DTM, DETM) and significantly improves topic coherence and diversity over other existing dynamic neural topic models (e.g. BERTopic).


[![PyPI - PyPi](https://img.shields.io/pypi/v/antm)](https://pypi.org/project/antm/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://hamedrahimi.fr)
[![arXiv](https://img.shields.io/badge/arXiv-2302.01501-<COLOR>.svg)](https://arxiv.org/abs/2302.01501)

# E2D
 Entity Encoder Decoder: A Privacy-Enhanced Framework for LLMs and RAG Agents

## Overview

With the implementation of the AI EU Act, privacy has become a paramount concern in the development and deployment of AI technologies. The E2D (Entity Encoder Decoder) framework emerges as a robust solution to address these privacy concerns. E2D is a privacy-enhanced framework designed for Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) agents, offering a reliable way to handle sensitive information while mitigating privacy risks.

## Description

The E2D framework focuses on enhancing the privacy of AI models by encoding and decoding entities in a secure manner. This ensures that delicate information is protected during both the training and inference phases of AI model operations. E2D is particularly beneficial when dealing with closed-source LLMs, providing an extra layer of security to prevent unauthorized access or misuse of sensitive data.

## Details

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
