# 🚀 FastAPI + Render 배포 가이드

이 프로젝트는 FastAPI를 사용한 간단한 Python 웹 애플리케이션을 Render 플랫폼에 배포하는 방법을 보여줍니다.

## 📋 프로젝트 구조

```
fast-api-render/
├── main.py              # FastAPI 애플리케이션 메인 파일
├── requirements.txt     # Python 의존성 패키지 목록
├── render.yaml         # Render 배포 설정 파일
└── README.md           # 이 파일
```

## 🛠️ 로컬에서 실행하기

### 1. 가상환경 설정 (권장)
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (Mac/Linux)
source venv/bin/activate
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 애플리케이션 실행
```bash
python main.py
```

### 4. 브라우저에서 확인
- http://localhost:8000 - 메인 페이지
- http://localhost:8000/docs - 자동 생성된 API 문서
- http://localhost:8000/health - 헬스 체크

## 🌐 Render에 배포하기

### 1. GitHub에 코드 업로드
1. GitHub에서 새 저장소 생성
2. 로컬 코드를 GitHub에 푸시:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/your-repo-name.git
git push -u origin main
```

### 2. Render 계정 생성 및 연결
1. [Render.com](https://render.com)에 가입
2. GitHub 계정과 연결
3. "New +" 버튼 클릭 → "Web Service" 선택

### 3. 배포 설정
1. **Repository**: GitHub 저장소 선택
2. **Name**: `fastapi-app` (원하는 이름으로 변경 가능)
3. **Environment**: `Python 3`
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. **Plan**: Free (무료 플랜 선택)

### 4. 환경 변수 설정 (선택사항)
- Render 대시보드에서 "Environment" 탭으로 이동
- 필요한 환경 변수 추가 (현재는 불필요)

### 5. 배포 시작
- "Create Web Service" 버튼 클릭
- 배포 과정이 자동으로 시작됩니다 (약 2-3분 소요)

## ✅ 배포 확인

배포가 완료되면:
1. Render에서 제공하는 URL로 접속 (예: `https://your-app-name.onrender.com`)
2. 다음 엔드포인트들이 정상 작동하는지 확인:
   - `/` - 메인 페이지
   - `/health` - 헬스 체크
   - `/docs` - API 문서
   - `/users/1` - 사용자 정보 조회

## 🔧 API 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/` | 메인 페이지 |
| GET | `/health` | 서버 상태 확인 |
| GET | `/users/{user_id}` | 사용자 정보 조회 |
| POST | `/users` | 새 사용자 생성 |
| GET | `/docs` | 자동 생성된 API 문서 |

## 🚨 문제 해결

### 배포 실패 시
1. **Build Command 오류**: `requirements.txt` 파일이 올바른지 확인
2. **Start Command 오류**: `uvicorn`이 설치되었는지 확인
3. **포트 오류**: `$PORT` 환경 변수를 사용했는지 확인

### 로그 확인
- Render 대시보드에서 "Logs" 탭으로 이동하여 오류 메시지 확인

## 📚 추가 학습 자료

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Render 공식 문서](https://render.com/docs)
- [Python 가상환경 가이드](https://docs.python.org/3/tutorial/venv.html)

## 🎉 성공!

배포가 완료되면 전 세계 어디서든 여러분의 FastAPI 애플리케이션에 접근할 수 있습니다!

---

**💡 팁**: 무료 플랜에서는 15분간 비활성화 시 자동으로 슬립 모드로 전환됩니다. 첫 요청 시 약간의 지연이 있을 수 있습니다.
