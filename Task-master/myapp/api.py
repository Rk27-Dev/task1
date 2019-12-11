from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class profileList(APIView):
	def get(self, request):
		model = profile.objects.all()
		serializer = profileSerializers(model, many = True)
		return Response(serializer.data)

	def post(self,request):
		serializer = profileSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class profileDetail(APIView):
	def get(self, request, id=id):
		model = profile.objects.get(id=id)
		serializer = profileSerializers(model)
		return Response(serializer.data)

	def put(self,request):
		serializer = profileSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


