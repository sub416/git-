from flask import Flask, render_template
from flask.wrappers import Request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
<body>
<h1>웹앱프로그래밍</h1>

<p><a href="https://www.w3schools.com/">헬로 페이지</a></p>
<p><a href="https://www.naver.com/">네이버 페이지</a></p>

</body>
</html>

    '''
@app.route('/naver')
def naverhtml():
    return render_template("naver.html")

@app.route('/gonaver', methods=['GET','POST'])
def gonaver():
    if Request.method == 'GET': 
            return "데이터를 받아주는 페이지" 
        else:
            # 여기 POST로 들어오는 데이터를 받아보자
            search = Request.form['lname']
            print("전달된값:", search)
            return "당신이 검색한 키워드(POST)<br>{}".format(search)


    

    
if __name__ == '__main__':
    app.run()

