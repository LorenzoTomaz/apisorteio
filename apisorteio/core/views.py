from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from apisorteio.core.sorteio import sorteio_loja, sort

class ApiSorteio(viewsets.ModelViewSet):

    def sorteio_api(self, request):

      if request.method == 'GET':
        sort_sort = sort()
        return Response({'ganhador': sort_sort})

    def sorteio_api_loja(self, request):

      if request.method == 'GET':
        sort_sort = sorteio_loja()
        return Response({'ganhador': sort_sort})