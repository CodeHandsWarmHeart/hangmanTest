import unittest
import random

import main
class HangmanTestCase(unittest.TestCase):
    def setUp(self):
        self.original_word_bank = ['bad', 'dad', 'about', 'and', 'around', 'wares', 'soup',
                      'mount', 'extend', 'brown', 'expert', 'tired', 'humidity', 'backpack', 'crust', 'dent', 'market',
                      'knock', 'smite', 'windy', 'coin', 'throw', 'silence', 'bluff', 'downfall', 'climb', 'lying',
                      'weaver', 'snob', 'kickoff', 'match', 'quaker', 'foreman', 'excite', 'thinking', 'mend',
                      'allergen', 'pruning', 'coat', 'emerald', 'coherent', 'manic', 'multiple', 'square', 'funded',
                      'funnel', 'sailing', 'dream', 'mutation', 'strict', 'mystic', 'film', 'guide', 'strain', 'bishop',
                      'settle', 'plateau', 'emigrate', 'marching', 'optimal', 'medley', 'endanger', 'wick', 'condone',
                      'schema', 'rage', 'figure', ]
        self.word = random.choice(self.original_word_bank)
        self.word_completion = "_" * len(self.word)
        self.guessedLetters = []

    def test_returnlowerCaseLetter(self):
        self.assertTrue(main.guess_next_letter(self.word_completion, self.guessedLetters, self.original_word_bank).islower())
    def test_guessIsInTargetAnswer(self):
        self.assertIn(main.guess_next_letter(self.word_completion, self.guessedLetters, self.original_word_bank), self.original_word_bank)

    def test_guessIsInTargetAnswer(self):
        self.assertNotIn(main.guess_next_letter(self.word_completion, self.guessedLetters, self.original_word_bank), self.guessedLetters)


