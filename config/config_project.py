import os

# coding: utf-8


# folder_input_path
folder_output_path = os.environ.get('folder_output_path', '/media/tuantmtb/WORK/wp/vnu/DoIT/data')
folder_python_path = os.environ.get('PYTHONPATH', '/media/tuantmtb/WORK/wp/startup/meowbees/git/research/bee_rnd')

timeout_concurrent_by_second = 600  # sec
debug_simulation = False
max_workers = int(os.environ.get('max_worker', 50))

SEND_GIRD_KEY = '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'
EMAIL_HOST = "email-smtp.eu-west-1.amazonaws.com"
EMAIL_PORT = "25"
EMAIL_HOST_USER = "AKIAJIIBDD6QQDUFEMGA"
EMAIL_HOST_PASSWORD = "AjhMLNvIlrFIA3w8rKK5cteDGv0ZoGyCnwgC8T3o5pgQ"
EMAIL_FROM = "no-reply@trans4work.com"
EMAIL_TO = "tuantmtb@gmail.com"

# ES 6.4.2
# Monitor and query: http://35.202.233.164/elk
ES_IP = os.environ.get('ES_IP', '35.202.233.164')
ES_USER = os.environ.get('ES_USER', 'user')
ES_PASS = os.environ.get('ES_PASS', 'uuanczUk8CGT')
ES_PORT = os.environ.get('ES_PORT', '80')

SPARK_MEMORY = os.environ.get('SPARK_MEMORY', '3')  # gb
SPARK_CORE = os.environ.get('SPARK_CORE', '3')  # cpu