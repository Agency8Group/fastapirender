from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

# FastAPI 앱 인스턴스 생성
app = FastAPI(
    title="간단한 FastAPI 애플리케이션",
    description="Render 배포를 위한 테스트 애플리케이션",
    version="1.0.0"
)

# 루트 엔드포인트
@app.get("/")
async def root():
    return {"message": "안녕하세요! FastAPI 애플리케이션이 정상적으로 작동하고 있습니다! 🚀"}

# 헬스 체크 엔드포인트
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "서버가 정상적으로 작동 중입니다"}

# 사용자 정보 엔드포인트
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": f"사용자 {user_id}",
        "email": f"user{user_id}@example.com",
        "status": "active"
    }

# POST 엔드포인트 예시
@app.post("/users")
async def create_user(user_data: dict):
    return {
        "message": "사용자가 성공적으로 생성되었습니다",
        "user_data": user_data,
        "created_at": "2024-01-01T00:00:00Z"
    }

# 서버 실행 (로컬 개발용)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
