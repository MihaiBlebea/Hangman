
class Cleaner:
    items = {
        "." : "",
        "," : "",
        "-" : "",
        "_" : ""
    }

    def get_keys(self):
        return list(self.items.keys())

    def clean(self, str):
        keys = self.get_keys()
        for key in keys:
            str = str.replace(key, self.items[key]).strip().lower()
        return str
