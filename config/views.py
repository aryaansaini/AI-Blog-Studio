from django.http import HttpResponse

def home(request):
    return HttpResponse("🚀 AI Blog Studio API is Running Successfully!")