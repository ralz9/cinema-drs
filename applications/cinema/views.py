from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from applications.cinema.models import Like, Movie, Rating
from applications.cinema.serializers import RatingSerializer, MovieSerializer


class MovieAPIView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['owner', 'title']
    search_fields = ['title']
    ordering_fields = ['id']
    """
    get_or_create - получит объект из базы данных , и создаст  если его нету
    он возвращет кортеж был ли создан объект или он уже есть (Tru, False)  
    """
    @action(methods=['POST'], detail=True)
    def like(self, request, pk , *args, **kwargs):
        # user получаем нашего user из запроса
        try:
            user = request.user
            movie_id = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response('movie not found', status=404)
        # like_obj - это переменная, в которую сохраняется объект Like,
        # _ не будет использоваться в дальнейшем коде. он используется для хранения результата,
        # который вас не интересует (был ли объект создан или нет).
        like_obj, _ = Like.objects.get_or_create(owner=user, movie_id=pk)
        # is_like по умолчанию False при создани он станвиться Tru и сохраняеться
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'liked'
        # если False status будет unliked
        if not like_obj.is_like:
            status = 'unliked'
        # возвращаем либо liked , unliked
        return Response({'status': status})


    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, movie_id=pk)
        rating_obj.rating = serializer.data['rating']
        rating_obj.save()
        return Response(serializer.data)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


