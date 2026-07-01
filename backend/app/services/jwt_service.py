import jwt
from datetime import datetime, timedelta

# Change this later to environment variable
SECRET_KEY = "CHANGE_THIS_TO_ENV_VARIABLE"

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24


def create_access_token(
    user_id: str
):

    expire_time = (
        datetime.utcnow()
        + timedelta(
            hours=ACCESS_TOKEN_EXPIRE_HOURS
        )
    )

    payload = {
        "user_id": str(user_id),
        "exp": expire_time
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    print("\nGenerated JWT:")
    print(token)

    return token


def verify_token(
    token: str
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print("\nDecoded JWT Payload:")
        print(payload)

        user_id = payload.get(
            "user_id"
        )

        if user_id is None:
            print(
                "\nJWT Error: "
                "user_id not found"
            )
            return None

        return str(user_id)

    except jwt.ExpiredSignatureError:

        print(
            "\nJWT Error: "
            "Token expired"
        )

        return None

    except jwt.InvalidTokenError as e:

        print(
            "\nJWT Invalid Token Error:"
        )
        print(e)

        return None

    except Exception as e:

        print(
            "\nUnexpected JWT Error:"
        )
        print(e)

        return None