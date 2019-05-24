from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index,Boolean,Date,Float,Text,CHAR
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:19971012@127.0.0.1:3306/zhihu", max_overflow=5)
Base = declarative_base()


class LIVE(Base):
    __tablename__ = 'Lives'
    id = Column(String(30),primary_key=True)
    tags = Column(String(30))
    speaker = Column(String(100))
    starts_at = Column(Date())
    created_at = Column(Date())
    ends_at = Column(Date())
    original_price = Column(Float())
    fee = Column(Float())
    purchasable = Column(Boolean())
    is_refundable = Column(Boolean())
    in_promotion = Column(Boolean())
    liked_num = Column(Integer())
    people_count = Column(Integer())
    review_count = Column(Integer())
    review_score = Column(Float())
    feedback_score = Column(Float())
    description = Column(Text())
    subject = Column(String(200))
    attachment_count = Column(Integer())
    audio_duration = Column(Integer())
    reply_message_count = Column(Integer())
    speaker_audio_message_count = Column(Integer())
    speaker_message_count = Column(Integer())
    tags = Column(String(50))
    has_audition=Column(Boolean())
    income = Column(Float())
    cospeakers = Column(String(300))

class PERSON(Base):
    __tablename__ = 'user'
    id = Column(CHAR(100),primary_key=True)
    answer_count = Column(Integer())
    articles_count = Column(Integer())
    columns_count = Column(Integer())
    favorited_count = Column(Integer())
    follower_count = Column(Integer())
    following_count = Column(Integer())
    gender =Column(Integer())
    hosted_live_count = Column(Integer())
    live_count = Column(Integer())
    name=Column(CHAR(100))
    participated_live_count = Column(Integer())
    pins_count = Column(Integer())
    question_count = Column(Integer())
    thanked_count = Column(Integer())
    url_token=Column(CHAR(100))
    voteup_count = Column(Integer())

class FORWEB:
    def __init__(self,dic):
        self.__dict__=dic