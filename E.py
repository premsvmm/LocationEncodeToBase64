import base64
import sys
import json

class E:
    def encode(self,Location):
        try:
            encoded_value = base64.b64encode(bytes((f'Location:{Location}'), 'utf-8'))
            return encoded_value.decode("utf-8")
        except:
            return "Exception during encode"


if __name__ == '__main__':
    e = E()
    arguments = sys.argv[1].split(',')
    list = []
    for value in arguments:
        list.append(e.encode(value))

    length = len(list)
    if length == 1:
        print(list[0])
    else :
        print(json.dumps(list))

