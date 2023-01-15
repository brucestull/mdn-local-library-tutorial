from django.http import HttpResponse


def test_project_creation(request):
    return HttpResponse("Goodbuy, world! Enjoy the Sails!")