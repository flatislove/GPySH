import json

def upload_to_json(data):
    new_l=[]
    for i in data:
        new_l.append(json.dumps(i.__dict__))
    try:
        with open('GPyS7H/contacts.json', 'w', encoding='utf-8') as jsonfile:
            jsonfile.write('{'+'\n'+'"data":'+'\n'+'['+',\n'.join(new_l)+']'+'\n'+'}')
    except Exception as ex:
        print("[INFO] Error while working with upload to Json: ",ex)
    return 1

def import_from_json():
    pass