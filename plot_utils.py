import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.pyplot import gca

prop = fm.FontProperties(fname='kalpurush.ttf')
ticks_font = fm.FontProperties(family='Helvetica', style='normal',
    size=12, weight='normal', stretch='normal')

def get_plot(word_association_dict, WORDS_ENGLISH):
    x = list(word_association_dict.keys())
    print(type(x))
    y = list(word_association_dict.values())
    plt.plot(WORDS_ENGLISH,y)
    # plt.legend(x, prop=prop)
    
    # plt.xticks(fontname='Kalpurush.ttf')
    plt.show()

def test_bangla_font():
    x = ['কাফির', 'নাস্তিক', 'ব্লগার', 'ধর্মদ্রোহী']
    y = [1, 2, 1.5, 3]
    a = gca()
    a.set_xticklabels(a.get_xticks(), ticks_font)

    plt.plot(x, y)
    # plt.xticks(fontname = 'Kalpurush.ttf')
    plt.show()

# test_bangla_font()
def get_subplot(target_wise_association_for_this_paper, b2e_dict, title):
    


    fig, ax = plt.subplots(nrows=1, ncols=2, squeeze=False)

    association_keys = []
    association_keys.append([b2e_dict[word] for word in target_wise_association_for_this_paper['progressive_occupation']['islamic'].keys()])
    association_keys.append([b2e_dict[word] for word in target_wise_association_for_this_paper['general_occupation']['radical'].keys()])

    y_values = []
    y_values.append([list(target_wise_association_for_this_paper['progressive_occupation']['islamic'].values()),
                    list(target_wise_association_for_this_paper['progressive_occupation']['radical'].values())])
    y_values.append([list(target_wise_association_for_this_paper['general_occupation']['islamic'].values()),
                    list(target_wise_association_for_this_paper['general_occupation']['radical'].values())])


    colors = ['skyblue', 'forestgreen', 'purple', 'lightcoral', 'red', 'yellow']
    markers = ['o', 's', 'p', 'd', '>', '<']

    # print(association_keys[0], y_values[0])

    for row_idx, row in enumerate(ax):
        # print(row)
        for col_idx, col in enumerate(row):
            col.plot(association_keys[col_idx],y_values[col_idx][0], marker=markers[0], markerfacecolor=colors[0], markersize=4, 
            color=colors[0], linewidth=2)
            col.plot(association_keys[col_idx],y_values[col_idx][1], marker=markers[1], markerfacecolor=colors[1], markersize=4, 
            color=colors[1], linewidth=2)
            plt.setp(col.get_xticklabels(), rotation=45, horizontalalignment='right')
    fig.legend(['islamic', 'radical'], loc='upper right')
    plt.title(title)
    plt.show()
