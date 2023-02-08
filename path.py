import json
import os

with open("C:/masil/site/한양도성길 위치.json", "r", encoding='UTF8') as f:
    j_data = json.load(f)
    for son in j_data['DATA']:
        if '(' in son['name']:
            num = son['name'].find('(')
            position[son['name'][:num]] = (son['lat'],son['lng'])
        elif "역" in son['name']:
            num = son['name'].find('(')
            position[son['name'][:num]] = (son['lat'],son['lng'])
        else:
            position[son['name']] = (son['lat'],son['lng'])
        point.append(position)
        position ={}
f.close()