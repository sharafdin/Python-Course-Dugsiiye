from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer


class SomaliTranslator:
    def __init__(self, model_name="facebook/m2m100_418M"):
        # Load pre-trained model and tokenizer
        self.model_name = model_name
        self.tokenizer = M2M100Tokenizer.from_pretrained(self.model_name)
        self.model = M2M100ForConditionalGeneration.from_pretrained(
            self.model_name)
        print("Somali-English Translator Model Loaded Successfully")

    def translate(self, somali_text: str) -> str:
        try:
            # Set source and target languages
            self.tokenizer.src_lang = "so"  # Somali
            encoded_input = self.tokenizer(somali_text, return_tensors="pt")

            # Generate translation
            generated_tokens = self.model.generate(
                **encoded_input,
                forced_bos_token_id=self.tokenizer.get_lang_id("en")  # English
            )
            english_translation = self.tokenizer.decode(
                generated_tokens[0],
                skip_special_tokens=True
            )

            return english_translation
        except Exception as e:
            return f"Error during translation: {e}"
