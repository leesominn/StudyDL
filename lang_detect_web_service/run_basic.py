# 서비스 메인코드 작성(엔트리(진입로) 코드)

# 1. 모듈 가져오기
from flask import Flask, request, render_template, jsonify

# 2. 플라스크 객체 생성
app = Flask(__name__)
'''
__name__을 기술한 py에서 직접 실행되면 __main__으로 리턴
but 다른 모듈에서 이 py를 호출하면 파일명으로 리턴됨
'''
print(__name__)

# 3. 라우팅 (서버측으로 요청이 들어오면 url-주소를 분석해서 어떤 함수가 대응할지 처리하는 것)
@app.route('/')
def home():
    # 응답 내용 -> 이 주소를 요청한 클라이언트가 보는 화면 창
    return 'hi'

# 4. 서버 가동
if __name__ == '__main__': # 이 코드가 엔프리 포인트가 되면 서버 가동
    app.run()