from django.shortcuts import render
import folium
from .models import Path

# 낙산
def home1(request):
    m = folium.Map(location=[37.58001023, 127.0071747], width=850, height=500,zoom_start=13.5)
    folium.Marker(
        [37.5878892, 127.0037098], popup="<i>혜화문</i>").add_to(m)

    folium.Marker(
        [37.5809508, 127.0083084], popup="<i>낙산공원</i>").add_to(m)

    folium.Marker(
        [37.5711907, 127.009506], popup="<i>흥인지문</i>").add_to(m)

    t = m._repr_html_()
    data = {}
    data['map'] = t
    hanyang = Path.objects.filter(th_no=1)
    data['hanyang'] = hanyang
    return render(request,'course/낙산.html', data)

# 남산
def home2(request):
    m = folium.Map(location=[37.55407998,126.9939333], width=850, height=500,zoom_start=13.5)
    folium.Marker(
        [37.5581817,127.007114], popup="<i>장충체육관</i>").add_to(m)

    folium.Marker(
        [37.5515763,127.0002206], popup="<i>국립극장</i>").add_to(m)

    folium.Marker(
        [37.5550786, 126.9797865], popup="<i>백범광장</i>").add_to(m)

    folium.Marker(
        [37.5514833, 126.9886119], popup="<i>남산N서울타워</i>").add_to(m)
    t = m._repr_html_()
    data = {}
    data['map'] = t
    hanyang = Path.objects.filter(th_no=1)
    data['hanyang'] = hanyang
    return render(request,'course/남산.html', data)

# 백악
def home3(request):
    m = folium.Map(location=[37.5947919,126.9832862], width=850, height=500,zoom_start=13.5)
    folium.Marker(
        [37.5926027,126.9664771], popup="<i>창의문</i>").add_to(m)

    folium.Marker(
        [37.5912832,126.9900967], popup="<i>와룡공원</i>").add_to(m)

    folium.Marker(
        [37.5947919,126.9832862], popup="<i>말바위안내소</i>").add_to(m)

    folium.Marker(
        [37.5956584,126.9810576], popup="<i>숙정문</i>").add_to(m)

    folium.Marker(
        [37.5878892,127.0037098], popup="<i>혜화문</i>").add_to(m)
    t = m._repr_html_()
    data = {}
    data['map'] = t
    hanyang = Path.objects.filter(th_no=1)
    data['hanyang'] = hanyang

    return render(request,'course/백악.html', data)

# 숭례문
def home4(request):
    m = folium.Map(location=[37.56046588, 126.9754813], width=850, height=500,zoom_start=13.5)
    folium.Marker(
        [37.5550786,126.9797865], popup="<i>백범광장</i>").add_to(m)

    folium.Marker(
        [37.5682025,126.9686779], popup="<i>돈의문터(서대문 강북삼성병원)</i>").add_to(m)

    folium.Marker(
        [37.5601399,126.9753099], popup="<i>숭례문</i>").add_to(m)
    folium.Marker(
        [37.5584425,126.978151], popup="<i>남대문시장</i>").add_to(m)
    t = m._repr_html_()
    data = {}
    data['map'] = t
    hanyang = Path.objects.filter(th_no=1)
    data['hanyang'] = hanyang

    return render(request,'course/숭례문.html', data)

# 인왕산
def home5(request):
    m = folium.Map(location=[37.58451994, 126.9649505], width=850, height=500,zoom_start=13.5)
    folium.Marker(
        [37.5922425,126.9672678], popup="<i>윤동주시인의언덕</i>").add_to(m)

    folium.Marker(
        [37.585032042186754, 126.95737903501436], popup="<i>인왕산</i>").add_to(m)

    folium.Marker(
        [37.5682025, 126.9686779], popup="<i>돈의문터</i>").add_to(m)

    folium.Marker(
        [37.5926027, 126.9664771], popup="<i>창의문</i>").add_to(m)
    t = m._repr_html_()
    data = {}
    data['map'] = t
    hanyang = Path.objects.filter(th_no=1)
    data['hanyang'] = hanyang

    return render(request,'course/인왕산.html', data)

def home6(request):
    m = folium.Map(location=[37.564865, 127.0088354], width=850, height=500,zoom_start=13.5)
    folium.Marker(
        [37.558128, 127.0070114], popup="<i>장충체육관</i>").add_to(m)

    folium.Marker(
        [37.5643621, 127.0099875], popup="<i>광희문</i>").add_to(m)

    folium.Marker(
        [37.5657792, 127.0088366], popup="<i>동대문역사문화공원</i>").add_to(m)

    folium.Marker(
        [37.5711907, 127.009506], popup="<i>흥인지문</i>").add_to(m)
    data = {}
    t = m._repr_html_()
    data['map'] = t
    hanyang = Path.objects.filter(th_no=1)
    data['hanyang'] = hanyang

    return render(request,'course/흥인지문.html', data)