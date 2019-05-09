from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    time_since_pub = serializers.SerializerMethodField()

    class Meta:
        model = Article
        exclude = ('id',)
        # fields = "__all__" # give me all the fields from the model to serialize
        # fields = ('title', 'description', 'body') # give me specific tuple of fields from the model to serialize

    def get_time_since_pub(self, object):
        pub_date = object.pub_date
        now = datetime.now()
        time_delta = timesince(pub_date)
        return time_delta

    def validate(self, data):
        """ Check that description and title are different """
        if data['title'] == data['description']:
            raise serializers.ValidationError("TItle & Description must be different")
        else:
            return data

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title must be at least 2 characters long")
        else:
            return value




# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     pub_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.pub_date = validated_data.get('pub_date', instance.pub_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         """ Check that description and title are different """
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("TItle & Description must be different")
#         else:
#             return data
    
#     def validate_title(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Title must be at least 2 characters long")
#         else:
#             return value
