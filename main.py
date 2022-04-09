import pandas as pd
import zlib
import base64
import config


def decode_base64_and_inflate(b64string):
    decoded_data = base64.b64decode(b64string)
    return zlib.decompress(decoded_data, -15)


def deflate_and_base64_encode(string_val):
    zlibbed_str = zlib.compress(string_val)
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode(compressed_string)


def generate_code(file_name, tab_name):
    df = pd.ExcelFile(file_name)
    target = df.parse(tab_name)
    target = target.values.tolist()
    target = pre_processing(target)

    target = str(target)
    target = target.replace('nan', '" "')
    target = target.replace("'", '"')
    target = bytes(str(target), 'utf-8')
    print(target)


def pre_processing(target_list):
    for index in range(len(target_list)):
        for value in range(len(target_list[index])):
            if type(target_list[index][value]) == float:
                target_list[index][value] = round(target_list[index][value], 1)
            elif target_list[index][value] == ' ':
                print(index, value, True)

    return target_list


if __name__ == '__main__':
    generate_code("PATH TO YOUR FILE", "THE TAB NAME IN YOUR EXCEL FILE")
