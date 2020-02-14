

def get_sorted_dict(word_association_dict):
    word_association_dict = {k: v for k, v in sorted(word_association_dict.items(), key=lambda item: item[1], reverse = True)}
    return word_association_dict

def populate_b2e_dict_for_words(BANGLA_WORDS, ENGLISH_WORDS):
    word_to_eng = {}
    for bangla_word, english_word in zip(BANGLA_WORDS, ENGLISH_WORDS):
        word_to_eng[bangla_word] = english_word
    return word_to_eng