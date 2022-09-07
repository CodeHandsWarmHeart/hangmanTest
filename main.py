import collections
import random
from typing import List


def guess_next_letter(pattern, used_letters, word_list):
    """my overall strategy is
       making guesses following the rank of most popular letters among all the word among the eligible words (filter out ineligible words in time)
    """
    """because when game start the word has been choosen 
        which means the length of the word has informed to the player 
        so we should narrow down the original world_list using all given hint 
        such as word length 
        and already reviewed letter in the pattern
    """

    # filter eligible words with correct length
    updated_eligible_wordlist = list(filter(lambda word_to_check_length: len(word_to_check_length) == len(pattern), word_list))

    indexes_of_guessed_letter: list[int] = [i for i, letter in enumerate(pattern) if letter != '_']

    updated_eligible_wordlist = get_eligible_word_list(updated_eligible_wordlist, indexes_of_guessed_letter, pattern, used_letters)

    rank_of_letters = collections.Counter("".join(updated_eligible_wordlist)).most_common()
    # data structure example rank_of_letters = [('e', 3), ('s', 1)]

    rank_of_letters = list(filter(lambda rank_tuple: rank_tuple[0].upper() not in used_letters, rank_of_letters))
    # remove the letters which have been tried
    # rank_of_letters = list(filter(lambda rank_tuple: rank_tuple[0].upper() not in used_letters, rank_of_letters))
    """for x in rank_of_letters:
        if x[0].upper() in used_letters:
            rank_of_letters.remove(x)"""
    try:
        return rank_of_letters[0][0]
    except IndexError:
        return 'no eligible words'



def get_eligible_word_list(word_list, indexes_of_guessed_letter, pattern, used_letters):

    # remove words contains incorrect guesses
    for i in word_list:
        for j in used_letters:
            if j in i:
                word_list.remove()

    word_list = list(filter(lambda w: w.find, used_letters))

    # remove words not match with pattern
    for i in word_list:
        for j in indexes_of_guessed_letter:
            if i[j].upper() != pattern[j]:
                word_list.remove(i)
                break

    return list(word_list)


def play(word, triesRemain):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []

    word_list = list(filter(lambda x: len(x) == len(word), original_word_bank))

    print("Let's play Hangman!")
    print(" ".join(word_completion))
    print("\n")
    while not guessed and triesRemain > 0:
        print("my function give this guess:")
        print(guess_next_letter(word_completion, guessed_letters, word_list))

        guess = input("Please guess a letter or word: ").upper()
        """
        world_list = list(filter(lambda x: len(x)==len(word), words))
        guess_next_letter(word_completion, gussed_letters, word_list):
        """
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                triesRemain -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                triesRemain -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(" ".join(word_completion))
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def get_word():
    word = random.choice(original_word_bank)
    return word.upper()


def main():
    word = get_word()
    play(word, 16)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word, 16)


original_word_bank = ['bad', 'dad', 'about', 'and', 'around', 'wares', 'soup',
                      'mount', 'extend', 'brown', 'expert', 'tired', 'humidity', 'backpack', 'crust', 'dent', 'market',
                      'knock', 'smite', 'windy', 'coin', 'throw', 'silence', 'bluff', 'downfall', 'climb', 'lying',
                      'weaver', 'snob', 'kickoff', 'match', 'quaker', 'foreman', 'excite', 'thinking', 'mend',
                      'allergen', 'pruning', 'coat', 'emerald', 'coherent', 'manic', 'multiple', 'square', 'funded',
                      'funnel', 'sailing', 'dream', 'mutation', 'strict', 'mystic', 'film', 'guide', 'strain', 'bishop',
                      'settle', 'plateau', 'emigrate', 'marching', 'optimal', 'medley', 'endanger', 'wick', 'condone',
                      'schema', 'rage', 'figure', ]
if __name__ == "__main__":
    main()
