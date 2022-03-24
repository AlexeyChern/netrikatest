from django.db.models import Count

from .models import City, People
from .serializers import Peopler, Cityer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.template import loader
from django.http import HttpResponse


class GetCityInfo(APIView):
    def get(self, request, pk):
        serial = Peopler(People.objects.filter(city=pk), many=True)
        cityname = Cityer(City.objects.get(id=pk)).data['cityname']
        return Response({"City": cityname, "People from selected city": serial.data})


def index(request):
    template = loader.get_template('index.html')
    cities = City.objects.annotate(Count('people')).order_by('-people__count')[0:10]
    citiesinfo = []
    for i in cities:
        citiesinfo.append(
            {"id": i.id, "cityname": i.cityname, "count": i.people__count})
    people = People.objects.select_related('city')
    peopleinfo = []
    for i in people:
        peopleinfo.append({"fio": i.fio, "city": i.city.cityname, "cityid": i.city.id})
    context = {
        'cities': citiesinfo,
        'people': peopleinfo
    }
    return HttpResponse(template.render(context, request))


def citypage(request, pk):
    template = loader.get_template('citypage.html')
    peoplefromcity = People.objects.filter(city=pk)
    peopleinfo = []
    for i in peoplefromcity:
        peopleinfo.append({"fio": i.fio})
    cityname = peoplefromcity[0].city.cityname
    context = {
        'cityname': cityname,
        'people': peopleinfo
    }
    return HttpResponse(template.render(context, request))

#
# class ClearState(APIView):
#     def get(self, request):
#         City.objects.all().delete()
#         People.objects.all().delete()
#         return Response("Done")
