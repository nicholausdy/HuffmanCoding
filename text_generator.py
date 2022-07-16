import random

class RandomText():
    def __init__(self, text_model):
        self.text_model = text_model
        # Text model = probability distribution of a set of characters
        # Ex of text model:
        # {"a":10, "b":30, "c":20, "d":15, "e":25}
        # Total of probability (weights) = 100
        self.seq_of_chars = []
        self.seq_of_cum_prob = []
        self.text = ""

    def extract_sequences(self): 
        cum_prob = 0
        for char, probability in self.text_model.items():
            self.seq_of_chars.append(char)
            cum_prob = cum_prob + probability
            self.seq_of_cum_prob.append(cum_prob)

    def randomly_generate_text(self, length):
        seq_of_random_chars = random.choices(
            population = self.seq_of_chars, 
            cum_weights = self.seq_of_cum_prob, 
            k = length
        )
        self.text = ''.join(seq_of_random_chars)

    @staticmethod
    def generate_text(text_model, length):
        text_generator = RandomText(text_model)
        text_generator.extract_sequences()
        text_generator.randomly_generate_text(length)
        return text_generator.text
        



