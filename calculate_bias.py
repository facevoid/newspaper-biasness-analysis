
def calculate_bias_for_embedding(association_dict):
    bias_dict = {}
    for key in association_dict['male'].keys():
        bias_dict[key] = association_dict['male'][key] - association_dict['female'][key]
    return bias_dict

def calculate_bias_for_all_embedding(association_dict):
    bias_dict_for_newspapers = {}
    for newspaper in association_dict.keys():
        bias_dict_for_newspapers[newspaper] = calculate_bias_for_embedding(association_dict=association_dict[newspaper]['professional_occupation'])
    return bias_dict_for_newspapers