import os
import sys

# need to change when deploy
folder_python_path = '/media/tuantmtb/WORK/Course/Master/InformationRetrevel/git/DistributedUrlCrawler'

sys.argv.append('/media/tuantmtb/WORK/Course/Master/InformationRetrevel/data')
max_worker = '50'

# default don't need to modify

folder_output_path = sys.argv[1]

print('folder_python_path:', folder_python_path)
print('folder_output_path :', folder_output_path)
print('max_worker :', max_worker)

os.putenv('PYTHONPATH', folder_python_path)
os.putenv('folder_output_path', folder_output_path)
os.putenv('max_worker', max_worker)

os.putenv('FLASK_ENV', 'development')
os.system('bash')