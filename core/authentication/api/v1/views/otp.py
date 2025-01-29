from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import OTPRequestSerializer, OTPVerifySerializer
from rest_framework import status
from django.core.cache import cache

class OTPRequestApiView(APIView):

    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(cache.get(serializer.validated_data["phone"]))
            return Response({
                "message": "OTP sent successfully!"
            }, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class OTPVerifyApiView(APIView):
    
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            otp = serializer.validated_data['otp']

            cached_otp = cache.get(phone)
            print(cached_otp)
            if str(cached_otp) == otp:
                cache.delete(phone) 
                return Response({
                    "message": "OTP verified successfully!"
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "message": "Invalid OTP!"
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )