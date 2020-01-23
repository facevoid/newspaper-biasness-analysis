import numpy as np 
from utils import get_sorted_dict
import traceback

class CalculateDistance:
    def __init__(self):
        super().__init__()
    
    def set_target_word_groups(self, target_word_groups, target_group_labels):
        self.target_word_groups = target_word_groups
        self.target_group_labels = target_group_labels
    
    
    def set_reference_word_groups(self, reference_word_groups, reference_group_labels):
        self.reference_word_groups = reference_word_groups
        self.reference_group_labels = reference_group_labels
    
    
    def __get_group_centroid(self, model,target_word_group):
        group_vectors = []

        for word in target_word_group:
            group_vectors.append(model.get_vector(word))

        centroid_target_word_group = np.average(group_vectors, axis=0)
        return centroid_target_word_group

    

    def __get_word_associations_for_target_group(self, model, centroid_group_word_vectors, target_group_words):
        word_associations = {}
        for word in target_group_words:
            word_vector = model.get_vector(word)
            association = np.linalg.norm(np.array(word_vector) - np.array(centroid_group_word_vectors))
            # value = np.linalg.norm(association)
            word_associations[word] = association
        return word_associations

    
    def get_association_for_provided_embedding(self, model):
        target_wise_association_for_this_paper = {}
        for target_group, target_word_list in zip(self.target_group_labels, self.target_word_groups):
        # print(word_list)
            association_dict_this_paper = {}
            
            for category, reference_words in zip(self.reference_group_labels, self.reference_word_groups):
                group_centroid = self.__get_group_centroid(model, reference_words)
                try:
                    word_associations = self.__get_word_associations_for_target_group(model, group_centroid, target_group_words= target_word_list)
                except:
                    traceback.print_exc(limit=2)
                # word_associations = get_sorted_dict(word_associations)
                # word_associations = {k: str(v) for k, v in word_associations.items()}

                association_dict_this_paper[category] = word_associations
            target_wise_association_for_this_paper[target_group] = association_dict_this_paper
        # print('from class')
        # print(target_wise_association_for_this_paper)
        return target_wise_association_for_this_paper