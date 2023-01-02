from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import *
from .serializer import *


@api_view(['POST'])
def create(request):
    item = request.POST.get('item')
    status = request.POST.get('status')
    todo = Todo.objects.create(item=item, status=status)
    ser = TodoSerializer(todo)
    return Response(ser.data)


@api_view(['GET'])
def get_item(request):
    itemm = request.GET.get('item')
    todo = Todo.objects.filter(item__icontains=itemm)
    ser = TodoSerializer(todo, many=True)
    return Response(ser.data)


@api_view(['PUT'])
def status(request):
    id_todo = request.POST.get('id_todo')
    edit_status = request.POST.get('status')
    todo = Todo.objects.get(id=id_todo)
    todo.status = edit_status
    todo.save()
    ser = TodoSerializer(todo)
    return Response(ser.data)


@api_view(['PUT'])
def item(request):
    id_todo = request.POST.get('id_todo')
    edit_item = request.POST.get('item')
    todo = Todo.objects.get(id=id_todo)
    todo.item = edit_item
    todo.save()
    ser = TodoSerializer(todo)
    return Response(ser.data)
