import collections

test_list = ['isaaa', 'bests', 'forss', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# Initializing substring
sub_str = '_e_ks'
letter_index = []
indices = [i for i, letter in enumerate(sub_str) if letter != '_']
print(indices)


def get_eligible_word_list(word_list, indexes_of_guessed_letter, pattern):
    for i in word_list:
        for j in indexes_of_guessed_letter:
            if i[j] != pattern[j]:
                word_list.remove(i)
                break
    return list(word_list)


# test_list = ['isaaa', 'bests', 'forss', 'geeks']

print(get_eligible_word_list(test_list, indices, sub_str))

used_letters = ['e', 'b']
rank_of_letters = collections.Counter("".join(test_list)).most_common()
# data structure rank_of_letters = [('e', 3), ('s', 1)]
print(rank_of_letters)
for x in rank_of_letters:
    if x[0] in used_letters:
        rank_of_letters.remove(x)

print(rank_of_letters[0][0])