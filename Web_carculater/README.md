# 🧮 웹 계산기 (Python Flask)

Python Flask 프레임워크로 구현한 현대적이고 아름다운 웹 계산기입니다.

## 📋 목차
- [주요 기능](#주요-기능)
- [기술 스택](#기술-스택)
- [프로젝트 구조](#프로젝트-구조)
- [설치 방법](#설치-방법)
- [사용 방법](#사용-방법)
- [주요 개념 설명](#주요-개념-설명)
- [개선 제안](#개선-제안)

## ✨ 주요 기능

### 기본 계산 기능
- ✅ 사칙연산 (덧셈, 뺄셈, 곱셈, 나눗셈)
- ✅ 괄호를 이용한 복잡한 수식 계산
- ✅ 소수점 계산 지원
- ✅ 실시간 계산 결과 미리보기

### 사용자 인터페이스
- 🎨 현대적인 글래스모피즘(Glassmorphism) 디자인
- 🌈 그라데이션 배경과 부드러운 애니메이션
- 📱 반응형 디자인 (모바일, 태블릿, 데스크톱 지원)
- ⌨️ 키보드 입력 지원

### 보안 기능
- 🔒 안전한 수식 계산 (허용된 문자만 사용)
- 🛡️ 0으로 나누기 방지
- ✅ 입력 유효성 검사

## 🛠 기술 스택

### 백엔드
- **Python 3.x**: 프로그래밍 언어
- **Flask 3.0.0**: 웹 프레임워크
  - 경량화된 Python 웹 프레임워크
  - RESTful API 구축에 최적화
  - 간단한 라우팅 시스템

### 프론트엔드
- **HTML5**: 웹 페이지 구조
- **CSS3**: 스타일링 및 애니메이션
  - Flexbox & Grid 레이아웃
  - CSS 애니메이션
  - 반응형 디자인 (Media Queries)
- **Vanilla JavaScript**: 클라이언트 사이드 로직
  - Fetch API를 통한 서버 통신
  - DOM 조작
  - 이벤트 처리

## 📁 프로젝트 구조

```
Web_calculator/
│
├── app.py                 # Flask 메인 애플리케이션
│   ├── 라우트 정의 (/, /calculate)
│   ├── 계산 로직 (safe_eval 함수)
│   └── 서버 설정
│
├── templates/
│   └── index.html        # 메인 HTML 템플릿
│       ├── 계산기 UI 구조
│       ├── JavaScript 클라이언트 로직
│       └── 키보드 이벤트 처리
│
├── static/
│   └── style.css         # CSS 스타일시트
│       ├── 글래스모피즘 디자인
│       ├── 애니메이션 효과
│       └── 반응형 스타일
│
├── requirements.txt      # Python 의존성 패키지
└── README.md            # 프로젝트 문서 (이 파일)
```

## 🚀 설치 방법

### 1. Python 설치 확인
```bash
python --version
# 또는
python3 --version
```
Python 3.7 이상이 필요합니다.

### 2. 가상환경 생성 (권장)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

## 💻 사용 방법

### 1. 서버 실행
```bash
python app.py
```

### 2. 브라우저에서 접속
```
http://localhost:5000
```

### 3. 계산기 사용
- **마우스**: 화면의 버튼 클릭
- **키보드**: 
  - 숫자 키: 0-9
  - 연산자: +, -, *, /
  - Enter: 계산 실행
  - Backspace: 마지막 문자 삭제
  - Escape: 전체 지우기

## 📚 주요 개념 설명

### 1. Flask 프레임워크

#### Flask란?
Flask는 Python으로 작성된 마이크로 웹 프레임워크입니다. "마이크로"라는 말은 최소한의 핵심 기능만 제공하며, 필요에 따라 확장할 수 있다는 의미입니다.

#### 주요 특징
- **경량화**: 핵심 기능만 포함하여 빠르고 가벼움
- **유연성**: 필요한 기능을 자유롭게 추가 가능
- **간단한 라우팅**: URL과 함수를 쉽게 연결
- **Jinja2 템플릿**: 동적 HTML 생성

#### 기본 사용법
```python
from flask import Flask
app = Flask(__name__)

# 라우트 정의: URL과 함수 연결
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
```

### 2. 라우팅(Routing)

라우팅은 URL 경로를 특정 함수와 연결하는 과정입니다.

```python
@app.route('/')              # GET 요청 (페이지 조회)
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])  # POST 요청 (데이터 전송)
def calculate():
    # 계산 로직
    return jsonify({'result': result})
```

### 3. RESTful API

REST(Representational State Transfer)는 웹 서비스 설계 방식입니다.

- **GET**: 데이터 조회 (예: 페이지 불러오기)
- **POST**: 데이터 생성/전송 (예: 계산 요청)
- **PUT**: 데이터 수정
- **DELETE**: 데이터 삭제

이 프로젝트에서는 POST 방식으로 계산 요청을 보냅니다:
```javascript
fetch('/calculate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ expression: '1+2' })
})
```

### 4. Jinja2 템플릿 엔진

Jinja2는 Flask의 기본 템플릿 엔진으로, HTML에 Python 변수나 로직을 삽입할 수 있습니다.

```html
<!-- 정적 파일 경로 생성 -->
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

<!-- 변수 출력 -->
<h1>{{ title }}</h1>

<!-- 조건문 -->
{% if user %}
    <p>Hello, {{ user }}!</p>
{% endif %}

<!-- 반복문 -->
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
```

### 5. Fetch API

Fetch API는 JavaScript에서 HTTP 요청을 보내는 현대적인 방법입니다.

```javascript
// 기본 사용법
async function calculate() {
    const response = await fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: '1+2' })
    });
    
    const data = await response.json();
    console.log(data.result);  // 3
}
```

#### async/await
- `async`: 함수를 비동기 함수로 선언
- `await`: Promise가 완료될 때까지 대기

### 6. JSON (JavaScript Object Notation)

JSON은 데이터를 교환하는 표준 형식입니다.

```javascript
// JavaScript 객체를 JSON 문자열로 변환
const data = { expression: '1+2' };
const jsonString = JSON.stringify(data);

// JSON 문자열을 JavaScript 객체로 변환
const obj = JSON.parse(jsonString);
```

Python에서는:
```python
from flask import jsonify

# 딕셔너리를 JSON으로 자동 변환
return jsonify({'result': 3})
```

### 7. DOM (Document Object Model)

DOM은 HTML 문서의 구조를 프로그래밍으로 제어할 수 있게 해줍니다.

```javascript
// 요소 선택
const element = document.getElementById('result');

// 내용 변경
element.textContent = '123';

// 스타일 변경
element.style.color = 'red';

// 이벤트 리스너 추가
element.addEventListener('click', function() {
    console.log('클릭됨!');
});
```

### 8. 이벤트 처리

사용자 상호작용을 감지하고 처리합니다.

```javascript
// 키보드 이벤트
document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        calculate();
    }
});

// 클릭 이벤트 (HTML에서 직접 연결)
<button onclick="calculate()">계산</button>
```

### 9. CSS 애니메이션

부드러운 시각 효과를 제공합니다.

```css
/* 트랜지션: 속성 변화를 부드럽게 */
.button {
    transition: transform 0.3s ease;
}

.button:hover {
    transform: translateY(-2px);
}

/* 키프레임 애니메이션: 복잡한 애니메이션 */
@keyframes float {
    0% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0); }
}

.element {
    animation: float 3s infinite;
}
```

### 10. 반응형 디자인

다양한 화면 크기에 대응합니다.

```css
/* 기본 스타일 (데스크톱) */
.container {
    width: 450px;
}

/* 태블릿 */
@media (max-width: 768px) {
    .container {
        width: 380px;
    }
}

/* 모바일 */
@media (max-width: 480px) {
    .container {
        width: 100%;
    }
}
```

### 11. 보안 고려사항

#### eval() 함수의 위험성
`eval()` 함수는 문자열을 코드로 실행하므로 보안 위험이 있습니다.

```python
# 위험한 코드
result = eval(user_input)  # 악의적인 코드 실행 가능

# 안전한 코드
def safe_eval(expression):
    # 허용된 문자만 확인
    if not re.match(r'^[\d\+\-\*\/\(\)\.\s]+$', expression):
        return "오류: 허용되지 않은 문자"
    return eval(expression)
```

## 🎯 개선 제안

### 1. 기능 확장
- [ ] **계산 기록 저장**: 데이터베이스(SQLite, PostgreSQL) 연동
- [ ] **과학 계산기 모드**: 삼각함수, 로그, 지수 등
- [ ] **단위 변환기**: 길이, 무게, 온도 변환
- [ ] **통화 계산기**: 실시간 환율 API 연동
- [ ] **테마 선택**: 다크모드, 라이트모드, 커스텀 테마

### 2. 사용자 경험 개선
- [ ] **계산 기록 보기**: 이전 계산 결과 확인
- [ ] **결과 복사 버튼**: 클립보드에 복사
- [ ] **음성 입력**: Web Speech API 활용
- [ ] **키보드 단축키 안내**: 도움말 팝업
- [ ] **오류 메시지 개선**: 더 친절한 안내

### 3. 성능 최적화
- [ ] **캐싱**: 반복된 계산 결과 저장
- [ ] **웹 워커**: 복잡한 계산을 백그라운드에서 처리
- [ ] **PWA 변환**: 오프라인 사용 가능

### 4. 보안 강화
- [ ] **입력 제한**: 수식 길이 제한
- [ ] **Rate Limiting**: API 요청 횟수 제한
- [ ] **HTTPS**: SSL/TLS 인증서 적용
- [ ] **CSRF 보호**: Flask-WTF 사용

### 5. 테스트 및 문서화
- [ ] **단위 테스트**: pytest로 함수 테스트
- [ ] **통합 테스트**: Selenium으로 UI 테스트
- [ ] **API 문서화**: Swagger/OpenAPI
- [ ] **사용자 매뉴얼**: 상세 사용 가이드

### 6. UI/UX 개선
- [ ] **로딩 애니메이션**: 계산 중 표시
- [ ] **진동 피드백**: 모바일에서 버튼 클릭 시
- [ ] **소리 효과**: 버튼 클릭음 (선택사항)
- [ ] **접근성 향상**: 
  - 스크린 리더 지원 (ARIA 속성)
  - 고대비 모드
  - 키보드 네비게이션 개선

### 7. 배포 옵션
- [ ] **Docker**: 컨테이너화하여 쉬운 배포
- [ ] **Heroku**: 무료 클라우드 호스팅
- [ ] **AWS/GCP**: 프로덕션 환경 구축
- [ ] **Vercel/Netlify**: 정적 호스팅 (API는 서버리스 함수로)

## 🔧 추가 라이브러리 활용 예시

### 1. Flask-CORS (다른 도메인에서 접근 허용)
```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 도메인 허용
```

### 2. python-dotenv (환경 변수 관리)
```python
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv('SECRET_KEY')
```

### 3. Flask-SQLAlchemy (데이터베이스)
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculator.db'
db = SQLAlchemy(app)

class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expression = db.Column(db.String(200))
    result = db.Column(db.String(200))
```

## 📝 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.

## 👨‍💻 개발자

Python Flask 웹 계산기 프로젝트

---

**즐거운 계산 되세요! 🎉**

