from fastapi import APIRouter, HTTPException

from app.models.user_model import (
    UserRegister,
    UserLogin
)

from app.services.auth_service import (
    register_user,
    authenticate_user,
    get_user_by_id
)

from app.services.jwt_service import (
    create_access_token
)

router = APIRouter()


@router.post("/register")
def register(
    user: UserRegister
):

    user_id = register_user(
        user.name,
        user.email,
        user.password
    )

    if user_id is None:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(
    user: UserLogin
):

    user_id = authenticate_user(
        user.email,
        user.password
    )

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        user_id
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }