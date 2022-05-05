# from django.http import JsonResponse
from rest_framework.views import APIView

from base.api.serializers import RegisterSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response

# def getRoutes(request):
#     routes=[
#         'api/token',
#         'api/token/refresh'
#     ]
#     return JsonResponse(routes, safe=False)

# register API


class UserRegisterView(APIView):
    def post(self, request):
        serializer_class = RegisterSerializer
        if serializer_class.is_valid():
            serializer_class.validated_data['password'] = make_password(
                serializer_class.validated_data['password'])
            user = serializer_class.save()

            status_code = status.HTTP_201_CREATED
            response = {
                'success': 'True',
                'status code': status_code,
                'message': 'User registered  successfully',
            }
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'status_code': status_code,
                'error_message': 'This email has already exist!',
            }

        return Response(response, status=status_code)
