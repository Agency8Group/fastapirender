# 🚀 FastAPI + Railway 배포 가이드

이 프로젝트는 FastAPI를 사용한 간단한 Python 웹 애플리케이션을 Railway 플랫폼에 배포하는 방법을 보여줍니다.

## ✨ Railway의 장점

- **🚀 빠른 배포**: GitHub 연동으로 자동 배포
- **💤 슬립 모드 없음**: 무료 플랜에서도 24/7 실행
- **⚡ 즉시 응답**: 첫 요청도 빠른 로딩
- **🔧 간단한 설정**: 복잡한 설정 없이 바로 배포
- **📊 실시간 로그**: 배포 과정을 실시간으로 확인

## 📋 프로젝트 구조

```
fast-api-railway/
├── main.py              # FastAPI 애플리케이션 메인 파일
├── requirements.txt     # Python 의존성 패키지 목록
├── railway.json         # Railway 배포 설정 파일
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

## 🌐 Railway에 배포하기

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

### 2. Railway 계정 생성 및 연결
1. [Railway.app](https://railway.app)에 가입
2. GitHub 계정과 연결
3. "New Project" 클릭 → "Deploy from GitHub repo" 선택

### 3. 저장소 선택 및 배포
1. **Repository**: GitHub 저장소 선택
2. **Deploy**: 자동으로 배포 시작
3. **Domain**: Railway가 자동으로 도메인 생성

### 4. 환경 변수 설정 (선택사항)
- Railway 대시보드에서 "Variables" 탭으로 이동
- 필요한 환경 변수 추가 (현재는 불필요)

### 5. 배포 완료 확인
- Railway 대시보드에서 "Deployments" 탭 확인
- 배포 상태가 "SUCCESS"가 되면 완료
- 제공된 URL로 접속 테스트

## ✅ 배포 확인

배포가 완료되면:
1. Railway에서 제공하는 URL로 접속 (예: `https://your-app-name.up.railway.app`)
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
1. **Build 오류**: `requirements.txt` 파일이 올바른지 확인
2. **Start Command 오류**: `uvicorn`이 설치되었는지 확인
3. **포트 오류**: `$PORT` 환경 변수를 사용했는지 확인

### Railway 특화 문제 해결
1. **배포 시간 초과**: Railway는 일반적으로 2-3분 내에 배포 완료
2. **도메인 접속 불가**: 배포 완료 후 몇 분 더 기다려보세요
3. **로그 확인**: Railway 대시보드에서 "Logs" 탭으로 이동

### 로그 확인
- Railway 대시보드에서 "Logs" 탭으로 이동하여 오류 메시지 확인
- 실시간 로그 스트리밍 지원

## 💰 Railway 요금제

### 무료 플랜
- **월 $5 크레딧** (충분한 사용량)
- **24/7 실행** (슬립 모드 없음)
- **자동 HTTPS**
- **커스텀 도메인**

### 유료 플랜
- **Pro Plan**: $20/월
- **더 많은 리소스**
- **우선 지원**

## 🆚 다른 플랫폼과 비교

| 플랫폼 | 무료 플랜 | 슬립 모드 | 배포 속도 | 설정 복잡도 |
|--------|-----------|-----------|-----------|-------------|
| **Railway** | ✅ | ❌ | ⚡ 빠름 | 🟢 간단 |
| Render | ✅ | ⚠️ 있음 | 🐌 느림 | 🟡 보통 |
| Heroku | ❌ | ❌ | ⚡ 빠름 | 🟡 보통 |
| Fly.io | ✅ | ❌ | ⚡ 빠름 | 🔴 복잡 |

## 📚 추가 학습 자료

- [Railway 공식 문서](https://docs.railway.app/)
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Python 가상환경 가이드](https://docs.python.org/3/tutorial/venv.html)

## 🎉 성공!

Railway로 배포하면 **슬립 모드 없이** 빠르고 안정적인 웹 애플리케이션을 운영할 수 있습니다!

---

**💡 팁**: Railway는 무료 플랜에서도 슬립 모드가 없어서 첫 요청도 빠르게 응답합니다. Render보다 훨씬 빠른 배포 경험을 제공합니다!