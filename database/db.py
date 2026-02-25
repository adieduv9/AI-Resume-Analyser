from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///resume_data.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

class ResumeAnalysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    match_score = Column(Float)
    quality_score = Column(Float)
    timestamp = Column(String)

Base.metadata.create_all(engine)