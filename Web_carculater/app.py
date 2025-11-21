"""
웹 계산기 Flask 애플리케이션

이 파일은 Flask 웹 프레임워크를 사용하여 웹 계산기 애플리케이션을 구동합니다.
사용자는 브라우저를 통해 계산기 인터페이스에 접근하고, 
백엔드에서 계산을 처리합니다.
"""

from flask import Flask, render_template, request, jsonify
import re

# Flask 애플리케이션 인스턴스 생성
# __name__: 현재 모듈의 이름을 전달하여 Flask가 리소스 위치를 파악하도록 함
app = Flask(__name__)


def safe_eval(expression):
    """
    안전한 수식 계산 함수
    
    사용자로부터 입력받은 수식을 안전하게 계산합니다.
    eval() 함수의 보안 취약점을 방지하기 위해 허용된 문자만 사용합니다.
    
    Args:
        expression (str): 계산할 수식 문자열
        
    Returns:
        float or str: 계산 결과 또는 에러 메시지
    """
    try:
        # 허용된 문자만 포함되어 있는지 확인 (숫자, 연산자, 괄호, 소수점, 공백)
        # 정규표현식으로 안전하지 않은 문자 제거
        if not re.match(r'^[\d\+\-\*\/\(\)\.\s]+$', expression):
            return "오류: 허용되지 않은 문자가 포함되어 있습니다"
        
        # 0으로 나누기 방지를 위한 사전 검사
        if '/0' in expression.replace(' ', ''):
            return "오류: 0으로 나눌 수 없습니다"
        
        # 수식 계산
        # eval()을 사용하지만, 위에서 안전한 문자만 허용했으므로 상대적으로 안전
        result = eval(expression)
        
        # 결과가 정수인 경우 소수점 제거
        if isinstance(result, float) and result.is_integer():
            return int(result)
        
        # 소수점 10자리까지만 표시
        if isinstance(result, float):
            return round(result, 10)
            
        return result
        
    except ZeroDivisionError:
        return "오류: 0으로 나눌 수 없습니다"
    except SyntaxError:
        return "오류: 잘못된 수식입니다"
    except Exception as e:
        return f"오류: {str(e)}"


@app.route('/')
def index():
    """
    메인 페이지 라우트
    
    사용자가 웹 애플리케이션의 루트 URL(/)에 접속하면
    index.html 템플릿을 렌더링하여 반환합니다.
    
    Returns:
        HTML: 렌더링된 index.html 페이지
    """
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    """
    계산 API 엔드포인트
    
    클라이언트로부터 POST 요청으로 수식을 받아 계산한 후
    JSON 형식으로 결과를 반환합니다.
    
    Request Body:
        expression (str): 계산할 수식
        
    Returns:
        JSON: {"result": 계산결과} 형태의 응답
    """
    try:
        # 클라이언트로부터 JSON 데이터 받기
        data = request.get_json()
        expression = data.get('expression', '')
        
        # 빈 문자열 체크
        if not expression:
            return jsonify({'result': '0'})
        
        # 수식 계산
        result = safe_eval(expression)
        
        # 결과를 JSON 형식으로 반환
        return jsonify({'result': str(result)})
        
    except Exception as e:
        # 예외 발생 시 에러 메시지 반환
        return jsonify({'result': f'오류: {str(e)}'})


@app.route('/history', methods=['GET'])
def get_history():
    """
    계산 기록 조회 API (향후 확장 가능)
    
    현재는 기본 구현만 되어있으며, 
    데이터베이스를 연결하면 계산 기록을 저장하고 조회할 수 있습니다.
    
    Returns:
        JSON: 계산 기록 목록
    """
    # 향후 데이터베이스 연동 시 계산 기록을 저장하고 조회할 수 있습니다
    return jsonify({'history': []})


if __name__ == '__main__':
    """
    애플리케이션 실행 부분
    
    debug=True: 개발 모드로 실행 (코드 변경 시 자동 재시작, 에러 메시지 상세 표시)
    host='0.0.0.0': 모든 네트워크 인터페이스에서 접속 가능
    port=5000: 5000번 포트에서 서버 실행
    """
    app.run(debug=True, host='0.0.0.0', port=5000)

