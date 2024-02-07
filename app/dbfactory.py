from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import config
from app.models import member, board

# sqlite 사용시 check_same_thread를 추가 - 쓰레드 사용 안 함
engine = create_engine(config.dbconn, echo=True, connect_args={'check_same_thread':False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 서버 시작 시 테이블 생성
def db_startup() :
    member.Base.metadata.create_all(engine)
    board.Base.metadata.create_all(engine)