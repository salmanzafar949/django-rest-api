from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'pk',
            'user',
            'title',
            'content',
            'createdAt'
        ]

    read_only_fields = ['pk', 'user']

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('Title Must be unique')
        else:
            return value
