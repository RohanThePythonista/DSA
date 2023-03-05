"""
Using __getattr__ for nicer configuration API
Typically, you'll read configuration from files (such as YAML) and get them as a dictionary.
However in Python you'd like to write config.httpd.port and not config['httpd']['port']

__getattr__ is a hook method that's called by Python when regular attribute lookup fails
(not to be confused with the lower level __getattribute__, which is much harder to work with).
You can use it to wrap the configuration dictionary. Here's a small example.

"""


class ConfigWrapper:
    def __init__(self, cfg):
        self._cfg = cfg

    def __getattr__(self, attr):
        try:
            val = self._cfg[attr]
            if isinstance(val, dict):
                val = ConfigWrapper(val)
            return val
        except KeyError:
            raise AttributeError(attr)

    def __dir__(self):
        return list(self._cfg)


if __name__ == '__main__':
    # Demo
    cfg = {
        'httpd': {
            'port': 8080,
            'interface': 'localhost',
        },
        'user': 'gary',
    }

    w = ConfigWrapper(cfg)
    user = w.user
    # using f'string in python3.6+
    print(f'user: {user}')
    port = w.httpd.port
    print(f'httpd.port: {port}')
