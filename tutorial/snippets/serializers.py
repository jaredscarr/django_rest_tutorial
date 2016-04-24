from rest_framework import serializers
from snippets.models import Snippet
from snippets.serializers import UserSerializer
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    """Snippet Serializer."""

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    snippets = serializers.PrimaryKeyRelatedField(many=True,
                                                  queryset=Snippet.objects.all()
                                                  )

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


class UserList(generics.ListAPIView):
    """Read only generic based views."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Read only generic based views."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
