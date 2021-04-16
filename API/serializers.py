from API.models import School, Eatery, Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class EaterySerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Eatery
        fields = '__all__'
    
    def get_reviews(self, obj):
        eateryReviews = Review.objects.filter(eatery = obj)
        returnList = []
        for review in eateryReviews:
            dic = {}
            dic["comment"] = review.comment
            dic["numeric_review"] = review.numeric_review
            returnList.append(dic)
        return returnList 

class SchoolSerializer(serializers.ModelSerializer):
    eaterys = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = '__all__'
    
    def get_eaterys(self, obj):
        schoolEaterys = Eatery.objects.filter(school = obj)
        returnList = []
        for eatery in schoolEaterys:
            returnList.append(eatery.name)
        return returnList
