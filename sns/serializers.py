from rest_framework import serializers
from .models import Episode, Comment


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )

    episode_url = serializers.ModelSerializer.serializer_url_field(
        view_name='episode_detail')

    class Meta:
        model = Episode
        fields = ('id', 'number', 'title',
                  'description', 'comments', 'upload', 'episode_url')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    episode = serializers.PrimaryKeyRelatedField(
        queryset=Episode.objects.all(), source='episode.id')

    class Meta:
        model = Comment
        fields = ('id', 'episode', 'comment', 'episode_id')

    def create(self, validated_data):
        comment = Comment.objects.create(episode=validated_data['episode']['id'],
        comment=validated_data['comment'])
        return comment
