
def number_of_words(sentence):
    number_of_spaces = 0
    for char_ in sentence:
        if char_ == ' ':
            number_of_spaces += 1
    return number_of_spaces + 1

def to_pig_latin(sentence):
    pig_latin_sentence = ''
    list_of_words_in_sentance = list()
    pig_latin_word = ''
    Num_of_words = number_of_words(sentence)
    for index in range(Num_of_words):
        english_word = sentence[:sentence.find(' ')]
        if not (' ' in sentence):
            english_word = sentence
        if english_word[0] in ['a', 'e', 'i', 'o', 'u']:
            pig_latin_word = english_word + 'way'
        else:
            is_one_of_first_consonants = True
            first_consonants = ''
            number_of_first_consonants = 0
            for char_ in english_word:
                if not(char_ in ['a', 'e', 'i', 'o', 'u']) and is_one_of_first_consonants:
                    first_consonants += char_
                    number_of_first_consonants += 1
                else:
                    is_one_of_first_consonants = False
            pig_latin_word = english_word[number_of_first_consonants:] + 'a' + first_consonants + 'ay'

        list_of_words_in_sentance.append(pig_latin_word)
        sentence = sentence[sentence.find(' ') + 1:]

    for word in list_of_words_in_sentance:

        pig_latin_sentence += word + ' '



    return pig_latin_sentence.strip()


def to_english(sentence):
    Numbe_of_words_in_sentence = number_of_words(sentence)
    english_sentence = ''
    english_word = ''
    word = ''
    for index in range(Numbe_of_words_in_sentence):
        word = sentence[:sentence.find(' ')]
        if not (' ' in sentence):
            word = sentence
        if word[-3:] == 'way':
            english_word = word[:-3]
        else:
            last_consonants = ''
            is_last_consonant = True
            number_of_consonats = 0
            """the for loop is for getting the displaced consonants"""
            for index in range(len(word)-3, -1, -1):

                if not (word[index] in ['a', 'e', 'i', 'o', 'u']) and is_last_consonant:
                    last_consonants = word[index] + last_consonants
                    number_of_consonats += 1
                else:
                    is_last_consonant = False
            english_word = last_consonants + word[:len(word) - (3+number_of_consonats)]
        english_sentence += english_word + ' '
        sentence = sentence[sentence.find(' ') + 1:]
    return english_sentence.strip()
