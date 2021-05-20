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
    if request.body:
        body = json.loads(request.body)
        if len(body.keys()) == 2:
            if (isinstance(body['A'], str) or isinstance(body['B'], str)):
                answer['error'] = 'Not a number'
            else:
                result = body['A'] + body['B']
                answer['answer'] = result
        else:
            answer['error'] = 'Enter 2 numbers'
    return JsonResponse(answer)


def subtract_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.body:
        body = json.loads(request.body)
        if len(body.keys()) == 2:
            if (isinstance(body['A'], str) and isinstance(body['B'], str)):
                answer['error'] = 'Not a number'
            else:
                result = body['A'] - body['B']
                answer['answer'] = result
        else:
            answer['error'] = 'Enter 2 numbers'
    return JsonResponse(answer)


def multiply_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.body:
        body = json.loads(request.body)
        if len(body.keys()) == 2:
            if (isinstance(body['A'], str) and isinstance(body['B'], str)):
                answer['error'] = 'Not a number'
            else:
                result = body['A'] * body['B']
                answer['answer'] = result
        else:
            answer['error'] = 'Enter 2 numbers'
    return JsonResponse(answer)


def divide_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.body:
        body = json.loads(request.body)
        if len(body.keys()) == 2:
            if (isinstance(body['A'], str) or isinstance(body['B'], str)):
                answer['error'] = 'Not a number'
            else:
                if body['B'] != 0:
                    result = body['A'] / body['B']
                    answer['answer'] = result
                else:
                    answer['error'] = 'Division by 0'
        else:
            answer['error'] = 'Enter 2 numbers'
    return JsonResponse(answer)
