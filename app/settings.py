from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    userid: str = ''
    passwd: str = ''
    # dbname: str = 'clouds2024.db'
    dbname: str = 'bigdata'
    dburl: str = 'bigdata.czg2yvgfhlpe.ap-northeast-2.rds.amazonaws.com'
    # dbconn: str = f'sqlite:///app/{dbname}'
    dbconn: str = f'mysql+pymysql://{userid}:{passwd}@{dburl}:3306/{dbname}?charset=utf8mb4'
    # db_conn = f'oracle+cx_oracle://{userid}:{passwd}'

    # class Config:
    #     env_file = '.env'


config = Settings()

