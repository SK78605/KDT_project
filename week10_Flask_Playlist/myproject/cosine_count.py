# 함수 생성

# CountVectorizer 후 코사인 유사도
def cosine_count(playlist_name):
    import pandas as pd
    import mariadb
    import numpy as np
    from tqdm import tqdm
    import re
    from konlpy.tag import Okt
    import datetime

    df=pd.read_csv('myproject/static/data/not_josa.csv',encoding='utf-8',index_col=0)
    # del df['Unnamed: 0']
    df.columns=['가수','제목','앨범사진','리뷰1','리뷰2','총리뷰','token_review']

    # 벡터화
    from sklearn.feature_extraction.text import CountVectorizer

    cv=CountVectorizer(ngram_range=(1,2),min_df=3)
    test=df["token_review"].to_list()
    dtm=cv.fit_transform(test)
    dtm=pd.DataFrame(dtm.toarray(),columns=cv.get_feature_names_out())

    # 코사인 유사도 : 두 벡터 사이 각도의 코사인 값 (-1 ~ 1)
    def make_cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b)) 

    okt=Okt()

    text = okt.pos(playlist_name, norm=True,stem=True) 
    text = [word for word, pos in text if pos != 'Josa' ]
    text = " ".join(text)
    dtm_2=cv.transform([text])
    target=dtm_2.toarray()[0]

    box=[]
    for i in range(len(dtm)):
        sample=dtm.iloc[i].to_numpy()
        cosine=make_cosine(target,sample)
        box.append(cosine)

    # 데이터프레임에 유사도 열 추가
    df['유사도분석']=box

    # 유사도에 따라 데이터프레임 정렬
    df.sort_values('유사도분석',ascending=False,inplace=True)

    # 유사한 상위 4개 확인
    top_4_similar = df.head(4)
    # return (top_4_similar[['가수', '제목', '앨범사진', '유사도분석']].values.tolist())
    
    # MariaDB 불러오기
    conn_params = {'host':'localhost',
               'port':3306,
               'user':'root',
               'password':'root',
               'database':"playlistdb",
               'autocommit':True}
    conn = mariadb.connect(**conn_params)
    cur = conn.cursor()

    result=top_4_similar[['가수', '제목', '앨범사진', '유사도분석','리뷰1']].values.tolist()
    result_list=[]
    for singer,song,album,yusa,review in result:
        result_list.append([singer,song,album])
        review=review.split("|")[:10]
        for r in review:
            try:
                # DB 로 보내기
                current_time = datetime.datetime.now()

                # 플리제목, 리뷰 40개, current_time을 SQL에 삽입
                cur.execute("INSERT INTO playtb (playlist, review, datetime) VALUES (%s, %s, %s);", (playlist_name, r, current_time))
                
            except Exception as e:
                pass

    cur.close()
    conn.close()


    return result_list


# 플리에 맞는 리뷰 데이터 가져오기
def review_bring(playlist_name):
    import mariadb

    conn_params = {'host':'localhost',
               'port':3306,
               'user':'root',
               'password':'root',
               'database':"playlistdb",
               'autocommit':True}
    conn = mariadb.connect(**conn_params)
    cursor = conn.cursor()

    # DB 에서 playtb  데이터 조회하는  sql 실행

    cursor.execute('SELECT review, datetime FROM playtb WHERE playlist = %s ORDER BY datetime DESC;', (playlist_name,))
    # 조회결과 가져오기
    queryDatas=cursor.fetchall()

    cursor.close()
    conn.close()

    return queryDatas



