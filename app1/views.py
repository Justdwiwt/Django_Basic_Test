# Create your views here.

from django.shortcuts import render
from app1 import models


# user_list = [
#     {"user": "Tom", "pwd": "111"},
#     {"user": "Jan", "pwd": "111"},
#     {"user": "Lily", "pwd": "111"},
# ]


def index(request):
    # return HttpResponse("success")
    # return render(request, "index.html", )
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # print(username, password)
        # temp = {"user": username, "pwd": password}
        # user_list.append(temp)
        models.UserInfo.objects.create(user=username, pwd=password)
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": user_list})
