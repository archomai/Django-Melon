from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    # User클래스를 정의
    # Installed_APPS에 members application 추가
    # AUTH_USER_MODEL 정의 (Appname.ModelClassName)
    # 모든 application들의 migrations폴더 내의 Migration 파일 전부 삭제
    # makemigrations - > migrate

    # 데이터베이스에 member_user 데이블이 생성되었는지 확인
