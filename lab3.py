"""Write a function in Python with a string such that it accepts a parameter- “stringsplit”.
 This encoded string will contain your name, domain name and register number. 
 You can separate the values in the string by any number of underscores."""

def decode_string(stringsplit):
    values = stringsplit.split('_')
    decoded_dict = {
        'name': values[0], 
        'domain': values[1],
        'register_number': values[2]
    }
    return decoded_dict

encoded_string = "Pavan_tourism_2347243"
decoded_data = decode_string(encoded_string)
print(decoded_data)
