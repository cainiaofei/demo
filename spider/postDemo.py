import json
import requests

id = 122
ip = "127.0.0.1"
text = "测试"
type = 1
pid = 123
tid = 456
did = "xcsdfdf"
mid = 123456

pipi_post_info = {
    "id": id,
    "ip": ip,
    "text": text,
    "type": type,
    "extra": '{"pid":%d,"tid":%d,"mid":%d,"did":"%s"}' % (pid, tid, mid, did)
}

params = json.dumps(pipi_post_info)

r = requests.post(url = API_ENDPOINT, data = data)

print(params)


