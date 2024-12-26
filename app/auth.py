from fastapi import Security, HTTPException
from fastapi.requests import Request
from fastapi import HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials


def authMiddleware( request: Request,credentials: HTTPBasicCredentials = Security(HTTPBasic())):
    if credentials.username not in "test" or credentials.password !="password":
          raise HTTPException(**{"status_code": 401, "detail": "Invalid authentication credentials!!!! Add valid api key "})
