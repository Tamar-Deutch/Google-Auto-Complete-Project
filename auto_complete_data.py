

class AutoCompleteData:
   # root = "technology_texts\\"
    root = 'technology_texts\collection'

    def __init__(self, sentence, source, offset, score_):
        self.completed_sentence = sentence
        self.source_text = source
        self.offset = offset
        self.score = score_

    def __str__(self):
        return f'{self.completed_sentence} ({self.source_text} {self.offset}) score {self.score}'

    def set_score(self, points_to_decrement):
        self.score -= points_to_decrement

    @staticmethod
    def get_score(word, sentence):
        return len(word) * 2