import pandas as pd
import matplotlib.pyplot as plt
import	platform
import	matplotlib.font_manager as	fm
import seaborn as sns
import numpy as np

def draw_bar_one_graph(name,x_list,y_list,_labels,_color):
    '''
    -name
    -x_list 
    -y_list
    -color :바 그래프 색상

    '''

    # if	platform.system()	==	'Windows':
    #     font_name =	fm.FontProperties(fname='week05_공공데이터_SSF\H2HDRM.TTF').get_name()
    #     plt.rc('font',	family=font_name)
    # else:
    #     plt.rc('font',	family='AppleGothic')

    some_color = sns.color_palette(_color)
    fig=plt.figure(figsize=(10,10))

    
    sns.barplot(x=x_list,y=y_list,label=_labels,palette=some_color)
    plt.xticks(rotation=90)
    # plt.yticks([2500,3000,3500,4000,4500,5000,5500])

    plt.legend()


    # 제목
    # plt.title(name,size=25)

    plt.xlabel('년도')

    # 이미지 저장
    plt.savefig('../img/'+name+_labels+'.png',dpi=100)
    plt.show()
    