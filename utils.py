

def get_sorted_dict(word_association_dict):
    word_association_dict = {k: v for k, v in sorted(word_association_dict.items(), key=lambda item: item[1], reverse = True)}
    return word_association_dict

def populate_b2e_dict_for_words(BANGLA_WORDS, ENGLISH_WORDS):
    word_to_eng = {}
    for bangla_word, english_word in zip(BANGLA_WORDS, ENGLISH_WORDS):
        word_to_eng[bangla_word] = english_word
    return word_to_eng

def change_word_to_english(bias_for_this_embedding, b2e_dict):
    bias_for_this_embedding_label_changed = {}
    for word in bias_for_this_embedding.keys():
        bias_for_this_embedding_label_changed[b2e_dict[word]] = bias_for_this_embedding[word]
    return bias_for_this_embedding


def change_dict_label_to_english(female_bias_for_all_embedding, b2e_dict):
    female_bias_for_all_embedding_label_changed = {}
    for embedding in female_bias_for_all_embedding.keys():
        bias_for_this_embedding = female_bias_for_all_embedding[embedding]
        female_bias_for_all_embedding_label_changed[embedding] = change_word_to_english(bias_for_this_embedding, b2e_dict)
        
def change_label_to_english_at_association(association_dict_for_this_paper, b2e_dict):
    for key in association_dict_for_this_paper['professional_occupation'].keys():
        updated_dict_for_this_key = {}
        for word, val in association_dict_for_this_paper['professional_occupation'][key].items():
            updated_dict_for_this_key[b2e_dict[word]] = association_dict_for_this_paper['professional_occupation'][key][word]
        association_dict_for_this_paper['professional_occupation'][key] = updated_dict_for_this_key
    return association_dict_for_this_paper