import os
import logging

logging.basicConfig(filename="logging.log", level=logging.DEBUG)


def split_extension(filepath):
    name, extension = os.path.splitext(filepath)
    return extension

def xor_encryption(user_msg, key):
    try:
        result = []

        bmsg = user_msg.encode()
        bmsg_list = list(bmsg)

        key_list = list(key)
        bmsg_len = len(bmsg)
        key_len = len(key)
        for char in range(bmsg_len):
            xor = bmsg_list[char] ^ key_list[char % key_len]
            result.append(xor)
        result_join = "".join(str(result))
        new_result = result_join[1:-1]
        return new_result
        logging.info(f"new_result: {new_result}")  # debugging
    except Exception as e:
        logging.debug(f"Error: {e}")

def xor_decryption(user_msg, key):
    try:
        char_to_remove = ","
        user_msg_split = user_msg.split(char_to_remove)
        int_msg = []
        for num in user_msg_split:
            int_num = int(num)
            int_msg.append(int_num)

        bytes_msg = bytes(int_msg)
        user_msg_list = list(bytes_msg)

        original_bytes_list = []
        msg_len = len(user_msg_list)
        key_len = len(key)

        for i in range(msg_len):
            xor_result = user_msg_list[i] ^ key[i % key_len]
            original_bytes_list.append(xor_result)

        original_bytes = bytes(original_bytes_list)
        decode_msg = original_bytes.decode('utf-8')
        return decode_msg
    except Exception as e:
        logging.debug(f"Error: {e}")