import pandas as pd
import matplotlib.pyplot as plt
import	platform
import	matplotlib.font_manager as	fm
import seaborn as sns
import numpy as np

def draw_line_one_graph(name,x_list,y_list,_color,_labels):
    '''
    -name
    -x_list 
    -y_list
    -color :선 그래프 색상

    '''

    if	platform.system()	==	'Windows':
        font_name =	fm.FontProperties(fname='../data/H2HDRM.TTF').get_name()
        plt.rc('font',	family=font_name)
    else:
        plt.rc('font',	family='AppleGothic')


    fig=plt.figure(figsize=(5,5))
    plt.style.use('ggplot')

    sns.lineplot(x=x_list,y=y_list,label=_labels,color=_color)
    plt.legend()
    plt.xlabel('년도')

    # 이미지 저장
    plt.savefig('../img/'+name+_labels+'.png',dpi=100)
    plt.show()
    