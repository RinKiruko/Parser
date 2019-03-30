from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, Date, Time
from sqlalchemy.dialects.postgresql import JSON, HSTORE


Base = declarative_base()
class Cryptocurrency(Base):
    __tablename__ = 'Currencies'

    ID = Column(Integer, primary_key=True, unique=True)
    Title = Column(String)
    Symbol = Column(String)
    ListingDate = Column(Date)
    Market = Column(JSON)
    Deals = Column(HSTORE)
    Url = Column(String)
    LastUpdateTimestamp = Column(Time)
    def __str__(self):
        return self.Title

    def as_url(self):
        return 'www.exchange.com/currency/%s' % self.Title