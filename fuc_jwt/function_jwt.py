#https://www.youtube.com/watch?v=Of1V5JV6voc&t=104s
from jwt import encode, decode
from jwt import exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse

def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

def write_token(data: dict):
    token = encode(payload={**data, 
                            "exp": expire_date(1) },
                            key=getenv("SECRET"), 
                            algorithm="HS256")
    #token = encode(payload={**data, "exp": datetime.now().utcnow+timedelta(hours=8) }, key=getenv("SECRET"), algorithm="HS256")
    return token


def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)

