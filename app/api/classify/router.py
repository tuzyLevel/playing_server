# import os
# import shutil
# from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
# from sqlalchemy.orm import Session
# from schemas.users.schema import CreateUserSchema, RequestDummyUserSchema
# from models.users.crud import (
#     get_user, create_user, get_user_by_email, get_users)
# from models.database import get_db
# from pydantic import BaseModel
import stat
import pwd
from PIL import Image
# from typing import List, Tuple
# import os
from typing import List
import datetime

from fastapi import APIRouter, File, UploadFile, Form
import shutil
from pathlib import Path
import os
import json
# from schemas.classify.schema import FileInfo


classify_router = APIRouter()


# UPLOAD_DIR = "public/uploaded_folder"
# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR)


# @classify_router.post("/")
# async def upload_files(
#     files: List[UploadFile] = File(...),
#     file_infos: str = Form(...)
# ):
#     file_infos_list = json.loads(file_infos)
#     results = []
#     for file, info in zip(files, file_infos_list):
#         print(info)
#         file_info = FileInfo(**info)
#         content = await file.read()
#         results.append({
#             "filename": file.filename,
#             "content_type": file.content_type,
#             "file_info": file_info,
#             "content_size": len(content)
#         })
#     return results
