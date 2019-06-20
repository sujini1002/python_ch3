from django.db import models

# Create your models here.
# python이 class의 정보를 가지고 DB 테이블을 생성한다.(ORM)
class Emaillist(models.Model):
    # 클래스 변수 -- 자동으로 pk인 id를 생성한다.(ORM)
    first_name = models.CharField(max_length=50) # 장고가 알아서 varchar(50)으로 생성시켜줌
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'EmailList({self.first_name,self.last_name,self.email})'
