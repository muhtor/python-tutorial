def set_str_upper(x):
    def make_upper(name):
        return name.upper()
    return make_upper


def set_array(x):
    def split_string(_str):
        convert_str_to_array = _str.split()
        return convert_str_to_array

    return split_string
