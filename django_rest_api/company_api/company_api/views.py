from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("this is my home page ")
    frens=["ali","ahmed","hassan"]
    return JsonResponse(frens,safe=False)
