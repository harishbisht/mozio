from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import Provider
from .serializers import ProviderSerializer
# Create your views here.



class ProviderList(APIView):
	def get_object(self, pk):
		try:
			return Provider.objects.get(pk=pk)
		except Provider.DoesNotExist:
			raise Http404
	def get(self,request):
		provider = Provider.objects.all()
		serializer = ProviderSerializer(provider, many=True)
		return Response(serializer.data)

	def post(request):
		serializer = ProviderSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		provider = self.get_object(pk)
		provider.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

