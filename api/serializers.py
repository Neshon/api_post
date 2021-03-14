from rest_framework import serializers

from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    # данная строка преобразовывает id автора в имя автора
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
