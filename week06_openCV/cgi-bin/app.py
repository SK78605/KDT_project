from flask import Flask, request, render_template, jsonify
import os
import joblib
import cv2

PATH = os.path.dirname(__file__)

randomforest = joblib.load(PATH+'/RandomForestClassifier(15).pkl')
characterDict = {
    'agaPing':'아자핑',
 'banglePing':'방글핑',
 'baroPing':'바로핑',
 'chachaPing':'차차핑',
 'ggraePing':'꾸래핑',
 'hachuPing':'하츄핑',
 'happyPing':'해핑',
 'joaPing':'조아핑',
 'lalaPing':'라라핑',
 'malangPing':'말랑핑',
 'nanaPing':'나나핑',
 'posilPing':'포실핑',
 'soljjiPing':'솔찌핑',
 'trustPing':'믿어핑'
}
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# # 업로드된 파일을 저장할 디렉토리 설정
# UPLOAD_FOLDER = os.path.join(os.getcwd(), './templates/uploads')
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html', result_message="아직 없음",internal_script="")

@app.route('/upload', methods=['POST','GET'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': '파일이 없습니다.'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'success': False, 'message': '파일을 선택하지 않았습니다.'})

    if file:
        filename = os.path.join(PATH+"/static/upload/uploaded_image.png")
        file.save(filename)



        #여기다가 인공지능 처리하실거 넣으시고
        imgData = cv2.imread(PATH+"/static/upload/uploaded_image.png")
        imgData = cv2.resize(imgData,(200,200))[:,:,:3].reshape((1,-1))/255.0
        predResult = characterDict[randomforest.predict(imgData)[0]]



        # 'uploaded_image' 변수를 템플릿에 전달
        return render_template('index.html',  result_message=f"{predResult}"
                               ,internal_script="showResult();")

if __name__ == '__main__':
    app.run(debug=True)