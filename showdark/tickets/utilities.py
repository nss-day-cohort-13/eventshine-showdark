from django.apps import AppConfig

class UtilityConfig(AppConfig):
    name = 'utilities'

    def convert_html_datetime_to_python_datetime(self, html_dt):
    	"""
    	Converts an HTML5 datetime-local object to a python datetime.datetime object

    	Args- HTML5 datetime-local objects
    	"""
    	date_in = html_dt
    	date_processing = date_in.replace('T', '-').replace(':', '-').split('-')
    	date_processing = [int(v) for v in date_processing]
    	date_out = datetime.datetime(*date_processing)

    	return date_out

