from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
import uvicorn
import os

# Pydantic 모델 정의
class UserCreate(BaseModel):
    name: str
    email: str
    age: Optional[int] = None
    bio: Optional[str] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    bio: Optional[str] = None

class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str
    age: Optional[int] = None
    bio: Optional[str] = None
    status: str
    created_at: str
    updated_at: str

class ApiResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None
    timestamp: str

# 가상 데이터베이스 (실제 프로덕션에서는 데이터베이스 사용)
users_db = {}
user_counter = 1

# FastAPI 앱 인스턴스 생성
app = FastAPI(
    title="🚀 멋진 FastAPI 애플리케이션",
    description="현대적이고 아름다운 API 서비스",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 루트 엔드포인트 - 아름다운 HTML 페이지
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🚀 멋진 FastAPI 애플리케이션</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
            }
            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 3rem;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                border: 1px solid rgba(255, 255, 255, 0.2);
            }
            h1 { font-size: 3rem; margin-bottom: 1rem; }
            p { font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.9; }
            .links { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
            .link {
                background: rgba(255, 255, 255, 0.2);
                color: white;
                text-decoration: none;
                padding: 0.8rem 1.5rem;
                border-radius: 10px;
                transition: all 0.3s ease;
                border: 1px solid rgba(255, 255, 255, 0.3);
            }
            .link:hover {
                background: rgba(255, 255, 255, 0.3);
                transform: translateY(-2px);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            }
            .status { 
                margin-top: 2rem; 
                padding: 1rem; 
                background: rgba(76, 175, 80, 0.2); 
                border-radius: 10px; 
                border: 1px solid rgba(76, 175, 80, 0.5);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 멋진 FastAPI 애플리케이션</h1>
            <p>현대적이고 아름다운 API 서비스에 오신 것을 환영합니다!</p>
            <div class="links">
                <a href="/docs" class="link">📚 API 문서</a>
                <a href="/health" class="link">💚 헬스 체크</a>
                <a href="/users" class="link">👥 사용자 목록</a>
                <a href="/stats" class="link">📊 통계</a>
            </div>
            <div class="status">
                <strong>✅ 서버 상태: 정상 작동 중</strong><br>
                <small>FastAPI + Railway로 구동 중</small>
            </div>
        </div>
    </body>
    </html>
    """

# 헬스 체크 엔드포인트
@app.get("/health", response_model=ApiResponse)
async def health_check():
    return ApiResponse(
        success=True,
        message="서버가 정상적으로 작동 중입니다",
        data={
            "status": "healthy",
            "uptime": "정상",
            "version": "2.0.0"
        },
        timestamp=datetime.now().isoformat()
    )

# 사용자 목록 조회
@app.get("/users", response_model=List[UserResponse])
async def get_users():
    if not users_db:
        return []
    return list(users_db.values())

# 특정 사용자 조회
@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    return users_db[user_id]

# 사용자 생성
@app.post("/users", response_model=ApiResponse)
async def create_user(user_data: UserCreate):
    global user_counter
    user_id = user_counter
    user_counter += 1
    
    now = datetime.now().isoformat()
    new_user = UserResponse(
        user_id=user_id,
        name=user_data.name,
        email=user_data.email,
        age=user_data.age,
        bio=user_data.bio,
        status="active",
        created_at=now,
        updated_at=now
    )
    
    users_db[user_id] = new_user
    
    return ApiResponse(
        success=True,
        message="사용자가 성공적으로 생성되었습니다",
        data=new_user.dict(),
        timestamp=now
    )

# 사용자 정보 수정
@app.put("/users/{user_id}", response_model=ApiResponse)
async def update_user(user_id: int, user_data: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    
    existing_user = users_db[user_id]
    update_data = user_data.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(existing_user, field, value)
    
    existing_user.updated_at = datetime.now().isoformat()
    users_db[user_id] = existing_user
    
    return ApiResponse(
        success=True,
        message="사용자 정보가 성공적으로 업데이트되었습니다",
        data=existing_user.dict(),
        timestamp=datetime.now().isoformat()
    )

# 사용자 삭제
@app.delete("/users/{user_id}", response_model=ApiResponse)
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    
    del users_db[user_id]
    
    return ApiResponse(
        success=True,
        message="사용자가 성공적으로 삭제되었습니다",
        timestamp=datetime.now().isoformat()
    )

# 통계 정보
@app.get("/stats", response_model=ApiResponse)
async def get_stats():
    total_users = len(users_db)
    active_users = len([u for u in users_db.values() if u.status == "active"])
    
    return ApiResponse(
        success=True,
        message="통계 정보를 성공적으로 조회했습니다",
        data={
            "total_users": total_users,
            "active_users": active_users,
            "inactive_users": total_users - active_users,
            "server_version": "2.0.0"
        },
        timestamp=datetime.now().isoformat()
    )

# 서버 실행 (로컬 개발용)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
