from flask import Flask, render_template
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
def naver():
    return '네이버 페이지' render_template("main-html")
    
if __name__ == '__main__':
    app.run()

