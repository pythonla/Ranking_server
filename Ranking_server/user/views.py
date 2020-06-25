from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

from user.models import Client
# Create your views here.


@csrf_exempt
def upload(request):

    if request.method == "GET":
        return HttpResponse("请使用POST请求")
    else:

        client_num = request.POST.get("client_num")
        score = request.POST.get("score")
        try:
            obj = Client.objects.get(number=client_num)
            if obj.receiver_mobile != int(score):
                print("score not equal")
                obj.receiver_mobile = score
                obj.save()
            else:
                print("score equal")

        except Client.DoesNotExist:
            print("notfound, will create",client_num,score)
            Client.objects.create(number=client_num,receiver_mobile=score)

        return HttpResponse("OK")


def getresult(request):
    client_num = request.GET.get("client_num")
    id_range = request.GET.get("rank_range")
    if id_range:
        ret = Client.objects.filter(id__range=id_range.split(",")).order_by("-receiver_mobile")
    else:
        ret = Client.objects.all().order_by("-receiver_mobile")
    d = []
    for i in ret:
        d.append({"Rank":i.pk, "client":i.number, "score":i.receiver_mobile })

    try:
        obj = Client.objects.get(number=client_num)

        if obj:
            d.append({"Rank":obj.pk, "client":obj.number, "score":obj.receiver_mobile })
    except:
        pass

    return JsonResponse(d, safe=False)
