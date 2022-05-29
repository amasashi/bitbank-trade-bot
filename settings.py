import configparser

conf = configparser.ConfigParser()
conf.read('settings.ini')


api_key = conf['bitbank']['api_key']
seacret_key = conf['bitbank']['seacret_key']


db =conf['database']['db']
user = conf['database']['user']
password = conf['database']['password']
host = conf['database']['host']
port = conf['database']['port']
database = conf['database']['database']
charset_type = conf['database']['charset_type']