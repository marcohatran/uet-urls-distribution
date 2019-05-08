from helper.reader_helper import load_json, store_file


def convert_json_to_line(input_path, output_path):
    data = load_json(input_path)
    output = ''

    for idx, element in enumerate(data):
        if (idx == 0):
            output = element
        else:
            output += '\n' + element
    store_file(output, output_path)

