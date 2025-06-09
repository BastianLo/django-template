from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class RefreshTokenView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


@api_view(['GET'])
def current_user(request):
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
        'firstName': user.first_name,
        'lastName': user.last_name,
        'is_superuser': user.is_superuser,
        'is_staff': user.is_staff,
        'is_active': user.is_active,
        'groups': [group.name for group in user.groups.all()],
        'user_permissions': [perm.name for perm in user.user_permissions.all()],
        'permissions': [perm.pk for perm in user.user_permissions.all()],
    })