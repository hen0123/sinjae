import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")

import django
django.setup() # cmd python manage.py shell

import json
from pybo.models import Thema,Path

theme = ['한양도성길', '생태문화길', '한강지천길/계절길', '서울둘레길']

# [코스명, 구간명, 세부코스, 길이, 시간]
road_1 =[] # 한양도성길
road_2 =[] # 생태문화길
road_3 =[] # 한강지천길/계절길
road_4 =[] # 서울둘레길

for i in range(4):
    Thema.objects.create(
        t_no=i+1, #테마번호
        t_name= theme[i], #테마명
    )

with open("서울 두드림길 정보.json", "r", encoding='UTF8') as f:
    json_data = json.load(f)
    for json in json_data['DATA']:
        if theme[0] == json["course_category_nm"]: # 한양도성길
            road_1.append([json["course_category_nm"], json["course_name"],json['detail_course'] ,json["distance"],json["lead_time"]])

        elif theme[1] == json["course_category_nm"]: #생태문화길
            road_2.append([json["course_category_nm"], json["course_name"],json['detail_course'] ,json["distance"],json["lead_time"]])

        elif theme[2] == json["course_category_nm"]: #한강지천길/계절길
            road_3.append([json["course_category_nm"], json["course_name"],json['detail_course'] ,json["distance"],json["lead_time"]])

        elif theme[3] == json["course_category_nm"]: #서울둘레길
            road_4.append([json["course_category_nm"], json["course_name"],json['detail_course'] ,json["distance"],json["lead_time"]])
f.close()

roads = road_1 + road_2 + road_3 + road_4 # 전체 길

road_1_name =list(set([x[1] for x in road_1])) # 6개
road_2_name =list(set([x[1] for x in road_2])) # 87개
road_3_name =list(set([x[1] for x in road_3])) # 33개
road_4_name =list(set([x[1] for x in road_4])) # 8개
road_name = road_1_name+ road_2_name+ road_3_name+ road_4_name # 구간 이름은 총 134개

data = [] # 정제된 데이터

for name in road_name:
    for road in roads:
        if road[1] == name:
            data.append([road[0],road[1],road[2],road[3],road[4]]) # 테마명, 구간명, 세부코스, 길이, 시간
            break

count = 1
for i in range(1,len(theme)+1):
    for d in data:
        if Thema.objects.get(t_no=i).t_name in d:
            Path.objects.create(
                p_no=count, # 구간번호
                th_no= Thema.objects.get(t_no=i), #테마 번호
                p_name = d[1],
                detail = d[2],
                distance = d[3],
                time = d[4],
            )
            count+=1
