class RoseDictionary:
    def __init__(self):
        self.data = []

    def __getitem__(self, key):
        for k, v in self.data:
            if k == key:
                return v
        raise KeyError(f'Key "{key}" not found in dictionary.')

    def __setitem__(self, key, value):
        self.data.append((key, value))

    def pop_item(self, raise_error=False, default=None, error_msg=None):
        if not self.data:
            if raise_error:
                raise KeyError(error_msg if error_msg else '')
            elif default is not None:
                return default
            else:
                return error_msg if error_msg else 'Dictionary was empty, and no default value/message was specified.'
        else:
            return self.data.pop()

    def get_item(self, key, raise_error=False, default=None, error_msg=None):
        for k, v in self.data:
            if k == key:
                return v
        if raise_error:
            raise KeyError(error_msg if error_msg else '')
        elif default is not None:
            return default
        else:
            return error_msg if error_msg else 'Value was not found, and no default value/message was specified.'


# Example Usage
d = RoseDictionary()
d["key1"] = "value1"
d["key2"] = "value2"

print(d["key1"])
print(d.get_item("key1"))
print(d.get_item("key3", default="Default Value"))
print(d.pop_item())
print(d.get_item("key1", error_msg="Error message"))
print(d.get_item("key2", error_msg="Error message 2"))
print(d.pop_item())
d.get_item("key3", default="Default Value", raise_error=True, error_msg="Hi")


   


    




    