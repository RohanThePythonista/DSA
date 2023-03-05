import requests
import json
from collections import defaultdict

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
todos = json.loads(response.text)

todos_by_user = defaultdict(int)
for todo in todos:
    if todo['completed'] is True:
        todos_by_user[todo['userId']] += 1

# print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)

max_complete = top_users[0][1]
# print(max_complete)
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))
# print(users)
max_users = " and ".join(users)
print(f"user(s) {max_users} completed {max_complete} TODOs")


def keep(todo):
    is_complete = todo['completed']
    has_max_count = str(todo['userId']) in users
    return is_complete and has_max_count


with open("filtered_json_file.json", "w") as write_file:
    filtered_todos = list(filter(keep, todos))
    print(filtered_todos)
    json.dump(filtered_todos, write_file, indent=4)


# below serialization has problem as json only serialize only built in
# json_str = json.dumps(6+8j)

def complex_encode(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        raise TypeError(f'Object of type {z.__class__.__name__} '
                        f'is not JSON serializable')


class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            super().default(self, z)
            pass


# json_str = json.dumps(6 + 8j, default=complex_encode)
json_str = json.dumps(6 + 8j, cls=ComplexEncoder)
print(json_str)


def decode_complex(my_dict):
    if "__complex__" in my_dict:
        return complex(my_dict['real'], my_dict['imaginary'])
    else:
        return my_dict


with open("complex_data.json", 'r') as complex_data:
    data = complex_data.read()
    z = json.loads(data, object_hook=decode_complex)
    print(z)
