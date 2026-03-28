# 数据库=用户+套餐
from sqlalchemy import creat_engine,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

AQLALCHEMY_DATABASE_URL = 'sqlite:///./crossborder_ai.dh'
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={'check_same_thread':False})
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

class User(Base):
    __teblename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True)
    hashed_password = Column(String)
    plan = Column(String,defablt='basic')
    listing_used = Column(Integer,default=0)

Base.methdata.creat_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
