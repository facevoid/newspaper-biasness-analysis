
def calculate_bias_for_embedding(association_dict, reference_labels):
    bias_dict = {}
    for key in association_dict[reference_labels[0]].keys():
        bias_dict[key] = association_dict[reference_labels[0]][key] - association_dict[reference_labels[1]][key]
    return bias_dict

def calculate_bias_for_all_embedding(association_dict, target_label, reference_labels):
    bias_dict_for_newspapers = {}
    for newspaper in association_dict.keys():
        bias_dict_for_newspapers[newspaper] = calculate_bias_for_embedding(association_dict=association_dict[newspaper][target_label], reference_labels = reference_labels)
    return bias_dict_for_newspapers