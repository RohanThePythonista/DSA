import json


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


path = "test.json"

l1 = [{"name": "rohan", "test": {"id": 37}, "test_lists": [{"test_lists": 12}, {"test_lists": 13}, {"test_lists": 14}]},
      {"name": "rohan", "test": {"id": 37}, "test_lists": [{"test_lists": 12}, {"test_lists": 13}, {"test_lists": 14}]}]
l2 = [{"test": {"id": 37}, "name": "rohan", "test_lists": [{"test_lists": 14}, {"test_lists": 13}, {"test_lists": 12}]},
      {"name": "rohan", "test": {"id": 37}, "test_lists": [{"test_lists": 12}, {"test_lists": 13}, {"test_lists": 14}]}]

test_dict = [{"name": "rohn", "id": 13737}]
with open("test.json", "w") as fp:
    json.dump(l1, fp, indent=4)

with open("test.json") as fp:
    expected_json = json.load(fp)

print(type(expected_json))
print(expected_json)

print(l1 == expected_json)
print(ordered(l1) == ordered(expected_json))
