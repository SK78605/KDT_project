#=========================================================================
# 시각화 함수 
#=========================================================================

import pandas as pd
import matplotlib.pyplot as plt
import	platform
import	matplotlib.font_manager as	fm
import seaborn as sns
import numpy as np
#-----------------------------------------------------------------------
# 막대 그래프
#-----------------------------------------------------------------------
def draw_bar_one_graph(name,x_list,y_list,_labels,_color):
    '''
    -name
    -x_list 
    -y_list
    -color :바 그래프 색상

    '''

    if	platform.system()	==	'Windows':
        font_name =	fm.FontProperties(fname='../data/H2HDRM.TTF').get_name()
        plt.rc('font',	family=font_name)
    else:
        plt.rc('font',	family='AppleGothic')

    some_color = sns.color_palette(_color)
    fig=plt.figure(figsize=(10,10))

    
    sns.barplot(x=x_list,y=y_list,label=_labels,palette=some_color)
    plt.xticks(rotation=90)
    # plt.yticks([2500,3000,3500,4000,4500,5000,5500])

    plt.legend()
    plt.xlabel('년도')

    # 이미지 저장
    plt.savefig('../img/'+name+_labels+'.png',dpi=100)
    plt.show()

#-----------------------------------------------------------------------
# 선그래프
#-----------------------------------------------------------------------
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

#-----------------------------------------------------------------------
# 보조축 그래프
#-----------------------------------------------------------------------
def draw_line_graph(city,x_list,y_list_1,y_list_2,bar_color):
    '''
    특정 지역에 대한 연봉 상승률 / 집값 상승률 그래프
    -city: 지역
    -x_list :년도 (columns)
    -y_list_1: 연봉 상승률 값 리스트
    -y_list_2: 집값 상승률 값 리스트
    - bar_color : 막대 그래프 색상

    '''

    if	platform.system()	==	'Windows':
        font_name =	fm.FontProperties(fname='../data/H2HDRM.TTF').get_name()
        plt.rc('font',	family=font_name)
    else:
        plt.rc('font',	family='AppleGothic')

    fig=plt.figure(figsize=(10,10))
    # plt.style.use('ggplot')
    cmap_name=bar_color

    #컬러 팔레트 설정
    cmap=plt.get_cmap(cmap_name)
    colors=cmap(np.linspace(0,1,len(x_list)))

    # 연봉 상승률 메인
    fig,ax1=plt.subplots()
    ax1.bar(x_list,y_list_1,label='연봉', color=colors)
 
    ax1.set_xlabel('년도')
    ax1.set_ylabel('평균 연봉')


    # 집값 보조축
    ax2=ax1.twinx()
    ax2.plot(x_list,y_list_2,color='tomato',linestyle='solid',linewidth=3,label='집값')
    ax2.set_ylabel('평당 가격')
    ax1.legend(bbox_to_anchor=[0.2,1])
    ax2.legend(bbox_to_anchor=[0.2,0.93])

 
    # plt.legend()
    plt.title('주거 지역 : '+city,size=25,weight='bold')
    plt.savefig('../img/'+city+'상승률.png',dpi=100)
    plt.show()

# bar 그래프 팔레트 색상
# Set3
# Pastel1
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
