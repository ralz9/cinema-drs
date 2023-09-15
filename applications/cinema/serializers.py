from rest_framework import serializers

from applications.cinema.models import Rating, Movie, Like

class LikeSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Like
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')

    """
    Когда вы создаете собственный сериализатор, который наследует от serializers.ModelSerializer, как в вашем случае, 
    вы можете переопределить метод to_representation, чтобы настроить, как объект будет сериализован в словарь (JSON-подобный объект).
    """
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['like_count'] = instance.likes.filter(is_like=True).count()
        """
        instance.likes - это обратная связь (related_name), которая позволяет получить все связанные объекты Like,
         привязанные к данному instance (фильму).
        instance в данном контексте представляет объект модели Movie, который сериализуется с дополнительными полями 
        like_count и rating, указывающими на количество лайков и среднюю оценку для этого фильма.
        """
        rating_result = 0
        for rating in instance.ratings.all():
            rating_result += rating.rating
        if rating_result:
            rep['rating'] = rating_result / instance.ratings.all().count()
        else:
            rep['rating'] = 0
        return rep


    class Meta:
        model = Movie
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Rating
        fields = ('rating',)
