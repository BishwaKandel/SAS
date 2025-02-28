from django.shortcuts import render
from rest_framework import generics, status
from .models import *
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated



class RegisterView(generics.CreateAPIView):
    queryset = HRManager.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        manager_id = response.data.get('ManagerID')  # Return the Manager ID in the response
        return Response({
            "status": True,
            "message": "User created successfully",
            "managerId": manager_id
        })   


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer   

    def get(self, request):
        # Fetch all HRManagers
        query_set = HRManager.objects.all()
        serializer = HRManagerSerializer(query_set, many=True)
        return Response({
            'data': serializer.data,
            'status': True
        })


    def post(self, request, *args, **kwargs):
        ManagerID = request.data.get('ManagerID')
        password = request.data.get('password')
        user = authenticate(ManagerID=ManagerID, password=password)
        
        try:
            user = HRManager.objects.get(ManagerID= ManagerID)
        except HRManager.DoesNotExist:
            return Response({
                'message': 'Invalid email or password',
                'status': False
            }, status=401)

        if check_password(password, user.password):  # ✅ Manually check hashed password
            refresh = RefreshToken.for_user(user)
            user_serializer = HRManagerSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data,
                'status': True
            })
        else:
            return Response({
                'message': 'Invalid email or password',
                'status': False
            }, status=401)

 
        

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password changed successfully!"}, status=status.HTTP_200_OK)



class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Password reset successfully. You can now log in with your new password."}, status=status.HTTP_200_OK)