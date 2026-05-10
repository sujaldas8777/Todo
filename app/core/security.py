from datetime import datetime, timedelta
from jose import jwt  
from passlib.context import CryptContext

SECRET_KEY = "6636c76d0638c0cf677d64fd1d9285ab8aa02574dd7713591f3df50dc023f868"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    password = password[:72]  # bcrypt limit
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    plain = plain[:72]
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)