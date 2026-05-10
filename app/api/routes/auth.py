from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.db.database import get_db
from app.Schemas.user import UserCreate, UserLogin, Token, UserResponse
from app.crud import user as crud_user
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


# SIGNUP
@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate, db: Session = Depends(get_db)):

    # 1️ Check if user already exists
    existing_user = crud_user.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already registered"
        )

    # 2️ Hash password
    hashed_password = hash_password(user.password)

    # 3️ Create user
    try:
        return crud_user.create_user(db, user.email, hashed_password)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


#  LOGIN
@router.post("/login/oauth2", response_model=Token)
def login_oauth2(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = crud_user.get_user_by_email(db, form_data.username)

    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials"
        )

    access_token = create_access_token({"sub": str(db_user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }