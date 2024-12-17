from rest_framework import serializers
from .models import User, Contact, SpamReport


# Serializers related to User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'phone_number', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            name=validated_data['name'],
            email=validated_data.get('email')
        )
        return user


# Serializers related to Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number', 'email']


# Serializers related to Spam Report model
class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamReport
        fields = ['id', 'phone_number', 'reason']


# Serializer for Search API
class SearchResultSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()
    spam_likelihood = serializers.IntegerField()


class DetailedResultSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_number = serializers.CharField()
    spam_likelihood = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    def get_spam_likelihood(self, obj):
        return SpamReport.objects.filter(phone_number=obj.phone_number).count()

    def get_email(self, obj):
        request = self.context.get('request')
        if isinstance(obj, User):
            if Contact.objects.filter(user=obj, phone_number=request.user.phone_number).exists():
                return obj.email
        return None
