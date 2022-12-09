from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from tags.models import Tag
from tags.serializers import TagListSerializer


class TagsApiView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    pagination_class = None
    # permission_classes = [IsAuthenticated]
    