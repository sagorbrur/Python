import gdata.youtube
 import gdata.youtube.service
 import psycopg2
 import sys
 from datetime import datetime
 import time
 import re
try:
    #you should read these from a config file
    conn=psycopg2.connect(host='localhost',database='databae_name',
