import spacy


class EntityEncoderDecoder:
    def __init__(self, model="en_core_web_lg"):
        # Load the English language model in spaCy
        self.nlp = spacy.load(model)
        self.entities = {}

    def encode_entities(self, text):
        """
        Extract named entities from a given text and replace them with placeholders.

        Args:
            text (str): The input text.
            dictionary (dict, optional): A dictionary of entities to use as a starting point.

        Returns:
            tuple: A tuple containing the output text and the dictionary of entities.
            :param text:
            :param entities:
        """
        # Process the text with spaCy
        doc = self.nlp(text)

        # Initialize the output text with the input text
        output_text = text

        # Iterate over the named entities in the document
        for ent in doc.ents:
            # Get the entity type and name as strings
            entity_type = str(ent.label_)
            entity_name = str(ent)

            # If the entity type is already in the dictionary, add the entity name to the list of entities of that type
            # Only add the entity name if it's not already in the list
            if entity_type in self.entities:
                if entity_name not in self.entities[entity_type]:
                    self.entities[entity_type].append(entity_name)
            # If the entity type is not in the dictionary, add it with the entity name as the first element of the list
            else:
                self.entities[entity_type] = [entity_name]

            # Replace the entity name in the output text with a placeholder that includes the entity type and index
            output_text = output_text.replace(entity_name,
                                              entity_type + "_" + str(self.entities[entity_type].index(entity_name)))

        # Return the output text and the dictionary of entities
        return output_text

    def decode_entities(self, string):
        """
        Decode placeholders in a given string with the actual entity names.
        Args:
            string (str): The input string.
        Returns:
            str: The decoded string.
        """
        # Iterate over the entity types in the dictionary
        for entity_type, entity_list in self.entities.items():
            # Iterate over the entities of the current type
            for i in range(len(entity_list)):
                # Replace the placeholder with the actual entity name
                placeholder = f"{entity_type}_{len(entity_list) - i - 1}"
                string = string.replace(placeholder, entity_list[len(entity_list) - i - 1])
        return string
