from rest_framework import serializers

from outsidemerch.models import Stage, Event, Artist, Store, Item


class StageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stage


class EventSerializer(serializers.ModelSerializer):
    artists = serializers.SlugRelatedField(many=True, slug_field='name', source="artist")

    class Meta:
        model = Event
        fields = ('id', 'time', 'name', 'stage', 'artists')


class ArtistSerializer(serializers.ModelSerializer):
    events = serializers.SlugRelatedField(many=True, slug_field='name', source="artist")

    class Meta:
        model = Artist
        fields = ("id", "name", "events")


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.SlugRelatedField(slug_field='name', source="artist")

    class Meta:
        model = Store
        fields = ("id", "artist", "title")


class ItemSerializer(serializers.ModelSerializer):
    store = serializers.SlugRelatedField(slug_field='title', source='store')

    class Meta:
        model = Item
        fields = ("id", "store", "name", "description", "created_time")
