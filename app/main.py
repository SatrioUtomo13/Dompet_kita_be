from fastapi import FastAPI
from app.routers import user, group, expense, auth, goal, dropdown
from app.db import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Dompet Kita")

# izinkan origin frontend
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Buat semua tabel jika belum ada
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user.router)
app.include_router(group.router)
app.include_router(expense.router)
app.include_router(auth.router)
app.include_router(goal.router)
app.include_router(dropdown.router)