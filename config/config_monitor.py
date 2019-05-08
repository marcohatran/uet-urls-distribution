import os

version_data_current = os.environ.get('version_data_current', '20181202_121212')


time_need_check_ssh_interval_by_second = 30 * 60
time_need_check_count_data_interval_by_second = 60 * 60

list_instances_need_check = [
    {
        "name": "ts-fb-storage",
        "ip": "104.196.157.93",
        "ports": [22]
    }
]
