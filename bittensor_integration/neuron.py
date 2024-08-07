import bittensor as bt
from model.translator import SomaliTranslator


class SomaliTranslatorNeuron(bt.Neuron):
    def __init__(self):
        super().__init__()
        # Initialize Somali Translator
        self.translator = SomaliTranslator()
        print("Somali Translator Neuron Initialized")

    def forward(self, synapse: bt.Synapse):
        try:
            # Get input text from synapse
            somali_text = synapse.text
            print(f"Received Input: {somali_text}")

            # Perform translation
            english_translation = self.translator.translate(somali_text)

            # Set the output to the translation
            synapse.output = english_translation
            print(f"Translated Output: {english_translation}")
        except Exception as e:
            synapse.output = "Error processing the input"
            print(f"Error: {e}")


if __name__ == "__main__":
    neuron = SomaliTranslatorNeuron()
    neuron.run()
