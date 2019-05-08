import csv


def list_uid_to_csv(list_uid, file_path):
    with open(file_path, 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for data in list_uid:
            wr.writerow([int(data)])
            # wr.writerow([data])