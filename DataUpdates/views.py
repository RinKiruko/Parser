from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import requests
from bs4 import BeautifulSoup

from .models import Cryptocurrency
from datetime import date, time

config = 'postgresql://django:abcd1234@localhost:5432/Parser'
engine = create_engine('postgresql://django:abcd1234@localhost:5432/Parser')
Session = sessionmaker(bind=engine)

def update_currency(new_data):
	session = Session()
	currency = session.query(Cryptocurrency).filter_by(Symbol=new_data['Symbol']).first()	
	
	processed_data = organize_data(new_data, 
								   last_update_timestamp=currency.LastUpdateTimestamp)
	if currency is not None:		
		for key,value in new_data.items():
			try:
				currency.__dict__[key] = value
			except KeyError:
				return KeyError('Currency Attribute doesn\'t exist')
				continue
		currency.LastUpdateTimestamp = int(time.time())
		session.commit()
	else:
		new_currency = Cryptocurrency(new_data)
		new_currency.LastUpdateTimestamp = int(time.time())
		session.add(new_currency)
		session.commit()


def organize_data(extracted_data, last_update_timestamp=None):
	OrganizedData = {}
	for day in extracted_data['MarketDays']:
		
		pass # magic 
	
	return OrganizedData 
	''' OrganizeData structure: 
	{
		'Title': ... ,
		'Symbol': ... ,
		'MarketDays': {
			'2017-07-23': {
				'Volume 24h': 311231,
				'MarketCap': 31123,
				'Open': 2131222,
				'Close':3121,
				'Trend': 'Bear' | 'Bull'
			}
		},
		'Deals': {
			'timestamp(from time.time())': price

		}
	}
	'''

def request_data(title):
	response = requests.get(currency.as_url())
	soup = BeautifulSoup(response.text())
	
	parsed_data = {}
	for time_container in soup.find_all(class_='date'):
		pass # parsing magic
		# price = soup.find_all(class='price')
		# dt = datetime(time_container.get_text())
		# day = dt.day
		# TransactionTime = dt.time
		# parsed_data['time'] = int(price)	
	return parsed_data