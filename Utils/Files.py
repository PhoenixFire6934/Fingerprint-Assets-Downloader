import json

class Files:
    def get_all(self, json_data):
        flist = []
        for i in json.loads(json_data)['files']:
            flist.append(i['file'])

        return flist