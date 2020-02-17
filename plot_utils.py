import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.pyplot import gca
from utils import get_sorted_dict
import seaborn as sns

def get_association_subplot(target_wise_association_for_this_paper, b2e_dict, title):
    
    association_keys = []
    for target_key in target_wise_association_for_this_paper.keys():
        # target_wise_association_for_this_paper[target_key] = get_sorted_dict(target_wise_association_for_this_paper[target_key])
        for reference_key in target_wise_association_for_this_paper[target_key].keys(): #target_wise_association_for_this_paper['progressive_occupation']['islamic']
            association_keys.append([b2e_dict[word] for word in target_wise_association_for_this_paper[target_key][reference_key].keys()])
            
            break
    fig, ax = plt.subplots(nrows=1, ncols=len(association_keys), squeeze=False)
    y_values = []
    
    for target_key in target_wise_association_for_this_paper.keys():
        this_target_y_values = []
        for reference_key in target_wise_association_for_this_paper[target_key].keys():
            this_target_y_values.append(list(target_wise_association_for_this_paper[target_key][reference_key].values()))
            
        y_values.append(this_target_y_values)
    
    

    colors = ['skyblue', 'forestgreen', 'purple', 'lightcoral', 'red', 'yellow']
    markers = ['o', 's', 'p', 'd', '>', '<']

    
    for row_idx, row in enumerate(ax):
        
        for col_idx, col in enumerate(row):
            col.plot(association_keys[col_idx],y_values[col_idx][0], marker=markers[0], markerfacecolor=colors[0], markersize=4, 
            color=colors[0], linewidth=2)
            col.plot(association_keys[col_idx],y_values[col_idx][1], marker=markers[1], markerfacecolor=colors[1], markersize=4, 
            color=colors[1], linewidth=2)
            plt.setp(col.get_xticklabels(), rotation=45, horizontalalignment='right')
    fig.legend(list(target_wise_association_for_this_paper[target_key].keys()), loc='upper right')
    plt.title(title)
    plt.show()


def get_bias_plot(bias_dict, b2e_dict):
    for key in bias_dict.keys():
        plt.close()
        sorted_dict = get_sorted_dict(bias_dict[key])
        x_labels = [b2e_dict[word] for word in sorted_dict.keys()]
        y_labels = list(sorted_dict.values())
        plt.xticks(rotation=60)
        plt.plot(x_labels, y_labels, marker='o', markersize = 4, linewidth = 2)
        plt.legend(['male_bias'])
        plt.title(key)
        plt.show()

def get_all_bias_in_single_plot_label_vs_year(bias_dict, words,labels):
    colors = ['skyblue', 'forestgreen', 'purple', 'lightcoral']
    markers = ['o', 's', 'p', 'd']
    years = list(bias_dict.keys())

    year_wise_bias = []
    for key in years:
        bias_for_this_year = []
        for word in words:
            bias_for_this_year.append(bias_dict[key].get(word, 0))
        year_wise_bias.append(bias_for_this_year)
        plt.plot(labels, bias_for_this_year, label = key)
    plt.xticks(rotation=60)
    plt.legend(loc="upper left")
    plt.show()



def get_all_bias_in_single_plot_year_vs_label(bias_dict, b2e, limit = None):


    years = ['2005', '2008', '2011', '2014', '2017']
    labels = list(get_sorted_dict(bias_dict['2017']).keys())
    

    if limit is not None:
        minimized_labels = labels[:limit] + labels[-limit:]
    else:
        minimized_labels = labels

    # print(minimized_labels)
    minimized_labels_english = [b2e[label] for label in minimized_labels]

    for label in minimized_labels:
        bias_for_this_label = []
        for year in years:
            bias_for_this_label.append(bias_dict[year].get(label, None))
        plt.plot(years, bias_for_this_label)
        plt.legend(minimized_labels_english, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()


def get_correlation_heatmap(df):
    # print('change ')
    sns.heatmap(df.corr(), annot=True,  vmin=-.0001, vmax=1,
            cmap='coolwarm')
    plt.show()