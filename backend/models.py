from sqlalchemy import Column, Integer, Float, DateTime
from database import Base
from sqlalchemy import Column, Integer, Float, DateTime, Boolean

# Historical solar generation data
class HistoricalGeneration(Base):
    __tablename__ = "historical_generation"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    generation_mw = Column(Float)


# Prediction results from ML model
class Prediction(Base):
    __tablename__ = "prediction"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    predicted_mw = Column(Float)

from database import engine


print("Tables created successfully")

class DeviationAnalysis(Base):
    __tablename__ = "deviation_analysis"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    actual_mw = Column(Float)
    predicted_mw = Column(Float)
    deviation = Column(Float)


class AnomalyDetection(Base):
    __tablename__ = "anomaly_detection"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    deviation = Column(Float)
    anomaly = Column(Boolean)


from sqlalchemy import Column, Integer, Float, Boolean, DateTime
from database import Base


class RevenueLoss(Base):
    __tablename__ = "revenue_loss"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    deviation = Column(Float)
    electricity_price = Column(Float)
    revenue_loss = Column(Float)