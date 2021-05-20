import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def add_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    print(request.body)
    if request.body:
        body = json.loads(request.body)
        try:
            number_1 = float(body['A'])
            number_2 = float(body['B'])
            result = number_1 + number_2
            answer['answer'] = result
            return JsonResponse(answer)
        except:
            answer['error'] = 'Enter 2 numbers'
            return JsonResponse(answer, status=400)


def subtract_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.body:
        body = json.loads(request.body)
        try:
            number_1 = float(body['A'])
            number_2 = float(body['B'])
            result = number_1 - number_2
            answer['answer'] = result
            return JsonResponse(answer)
        except:
            answer['error'] = 'Enter 2 numbers'
            return JsonResponse(answer, status=400)



def multiply_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.body:
        body = json.loads(request.body)
        try:
            number_1 = float(body['A'])
            number_2 = float(body['B'])
            result = number_1 * number_2
            answer['answer'] = result
            return JsonResponse(answer)
        except:
            answer['error'] = 'Enter 2 numbers'
            return JsonResponse(answer, status=400)


def divide_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.body:
        body = json.loads(request.body)
        try:
            number_1 = float(body['A'])
            number_2 = float(body['B'])
        except:
            answer['error'] = 'Enter 2 numbers'
            return JsonResponse(answer, status=400)
        if number_2 != 0:
            result = number_1 / number_2
            answer['answer'] = result
        else:
            answer['error'] = 'Division by 0'
            return JsonResponse(answer, status=400)
    return JsonResponse(answer)
