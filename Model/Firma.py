import json


class Firma:
    'Firma Objekt'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Ansprechpartner:
    'Ansprechpartner Objekt'
