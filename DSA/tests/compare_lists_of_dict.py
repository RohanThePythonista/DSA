l1 = {"name": "rohan", "test": {"id": 37}}
l2 = {"test": {"id": 37}, "name": "rohan"}

# print(sorted(l1) == sorted(l2))

import json


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def data_generator(item):
    """
    :param item: a message to be added in batch
    :return: Serialized ``obj`` to a JSON formatted ``str``
    """
    message = ""
    try:
        message = json.dumps(item, indent=2, sort_keys=True).encode(encoding='utf-8')
    except UnicodeDecodeError as err:
        pass
        # self.logger.error("cannot dump json: %s" % err)
    return message


print(data_generator(l1) == data_generator(l2))


def calculate_hash(json_dict):
    """
       calculates the hash of an ORDERED json dict
        :param json_dict:
        :return: hash value
        """
    try:
        json_bin = json.dumps(json_dict, ensure_ascii=False, sort_keys=True).encode(encoding='utf-8')
    except TypeError as ex:
        # self.logger.error("no valid json object %s, because %s" % (json_dict, ex))
        return
    hash_calculator = hashlib.sha224(json_bin)
    hash = hash_calculator.digest()[:16]
    hash_encoded64 = base64.urlsafe_b64encode(hash)
    string_hash_base64 = hash_encoded64.decode('utf8')  # hash as string needed, to put into json later
    return string_hash_base64


print(calculate_hash(l1) == calculate_hash(l2))
