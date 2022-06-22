from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers

from ..models import Movie, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchlist',)


def name_length(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("The name length is too short")
        else:
            return value


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    review = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(validators=[name_length])
    # description = serializers.CharField()
    # is_active = serializers.BooleanField()

    def get_len_name(self, obj):
        return len(obj.name)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        su = 0
        for x in representation['review']:
            su = su + x['rating']
        representation['sum_ratings'] = su
        representation['avg_rating'] = su/representation['num_ratings']
        return representation

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("The name length is too short")
    #     else:
    #         return value
    #
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description are too similar")
        else:
            return data


class StreamPlatformSerializer(serializers.ModelSerializer):
    movie = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='get_movie_detail'
    )

    class Meta:
        model = StreamPlatform
        fields = '__all__'