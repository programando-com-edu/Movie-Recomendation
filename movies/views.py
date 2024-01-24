from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from movies.models import Movie


# Create your views here.


class GetMoviesIdsView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = (AllowAny,)

    def filtered_ids(self, filters={}):
        try:
            movies_qs = Movie.objects.prefetch_related('genres', 'streaming', 'buy', 'rent').filter(**filters)
            movies_ids = movies_qs.values_list('id', flat=True)
            return movies_ids
        except Exception as e:
            print(str(e))
            return []

    def post(self, request, *args, **kwargs):
        return Response(self.filtered_ids(request.data))
