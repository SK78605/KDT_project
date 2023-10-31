# 모듈 로딩
from flask import Flask,render_template,request,redirect
from .cosine_count import cosine_count,review_bring
import mariadb
import datetime

app = Flask(__name__)

# 홈 페이지
@app.route("/")
def start():
    return render_template("start.html")

# 서브 페이지
@app.route("/sub_page")
def sub_page():
    return render_template("sub_page.html")

# 메인 페이지
@app.route("/search", methods=["POST"])
def search():
    search_query = request.form.get("search_query")
    search_results = cosine_count(search_query)
    search_review=review_bring(search_query)
  
    return render_template("playlist.html", search_query=search_query, search_results=search_results,search_review=search_review)


# 서브컨텐츠(영상이미지)
@app.route("/link_page", methods=["GET","POST"])
def link_page():
    search_query=""
    search_results=""
    search_review=''
    a = request.args.get("type")
    if(a=="1"):
        search_query = '살짝 쌀쌀한 가을 아니면 언제 들을래'
    if(a=="2"):
        search_query = '짝사랑 상대를 돌아보게 만드는 플레이리스트'
    if(a=="3"):
        search_query = '내 마음에 들어온 감성 플레이리스트'

    search_results = cosine_count(search_query) 
    search_review=review_bring(search_query) 
    return render_template("playlist.html",search_results=search_results,search_query=search_query,search_review=search_review)

# 댓글 등록 후 페이지
@app.route("/test", methods=["POST"])
def test():
    if request.method == "POST":
        test_data = request.form.get("test")
        search_query = request.form.get('search_query')  # search_query 값을 가져오기

        # 데이터베이스에 연결 및 데이터 삽입
        conn_params = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'database': "playlistdb",
            'autocommit': True
        }
        conn = mariadb.connect(**conn_params)
        cur = conn.cursor()

        try:
            current_time = datetime.datetime.now()
            cur.execute("INSERT INTO playtb (playlist, review, datetime) VALUES (%s, %s, %s);", (search_query, test_data, current_time))
        except Exception as e:
            pass

        cur.close()
        conn.close()

        search_results = cosine_count(search_query) 
        search_review=review_bring(search_query) 
    return render_template("playlist.html",search_results=search_results,search_query=search_query,search_review=search_review)
