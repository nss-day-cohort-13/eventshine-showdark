import datetime

def convert_html_datetime_to_python_datetime(html_dt):
	"""
	Converts an HTML5 datetime-local object to a python datetime.datetime object

	Args- HTML5 datetime-local objects
	"""
	print("~: ", html_dt)
	date_in = html_dt
	date_processing = date_in.replace('T', '-').replace(':', '-').replace('Z', '').split('-')
	date_processing = [int(v) for v in date_processing]
	date_out = datetime.datetime(*date_processing)

	return date_out

