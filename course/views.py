from django.shortcuts import render
import folium
from .models import Path

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


def home2(request):
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
    return render(request,'course/남산.html', data)

def home3(request):
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

    return render(request,'course/백악.html', data)

def home4(request):
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

    return render(request,'course/숭례문.html', data)

def home5(request):
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

    return render(request,'course/인왕산.html', data)

def home6(request):
    m = folium.Map(location=[37.58001023, 127.0071747], width=850, height=500,zoom_start=13.5)
    folium.Marker(
        [37.5878892, 127.0037098], popup="<i>혜화문</i>").add_to(m)

    folium.Marker(
        [37.5809508, 127.0083084], popup="<i>낙산공원</i>").add_to(m)

    folium.Marker(
        [37.5711907, 127.009506], popup="<i>흥인지문</i>").add_to(m)
    data = {}
    t = m._repr_html_()
    data['map'] = t
    hanyang = Path.objects.filter(th_no=1)
    data['hanyang'] = hanyang

    return render(request,'course/흥인지문.html', data)