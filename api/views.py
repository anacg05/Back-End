from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Autor, Editora, Livro
from .serializers import AutorSerializers, EditoraSerializers, LivroSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class AutoresView(ListCreateAPIView):

    queryset = Autor.objects.all()  # set pega get envia  
    serializer_class = AutorSerializers


@api_view(['GET', 'POST'])
def visu_autor(request):
    if request.method == 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializers(queryset, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':  # envia coisas
        serializer = AutorSerializers(data = request.data)
        
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
class EditorasView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializers


class LivrosView(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializers