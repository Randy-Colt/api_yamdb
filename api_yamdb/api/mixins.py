from rest_framework import mixins, viewsets


class ListCreateDeleteMixin(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    lookup_field = 'slug'
