import json

class Fingerprint():
    def info(self, json_data):
        content = json.loads(json_data)
        sha = content['sha']
        version = content['version']

        return content, sha, version