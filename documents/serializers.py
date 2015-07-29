from rest_framework import serializers
from documents.models import Document, DocumentPermission

__author__ = 'smuravko'


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'author', 'summary', 'private_number')


class DocumentCreateSerializer(serializers.Serializer):
    private_number = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)
    summary = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)
    file = serializers.FileField(required=False, allow_null=True)


class DocumentUpdateSerializer(serializers.ModelSerializer):
    private_number = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)
    summary = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = Document
        fields = ('summary', 'private_number')


class DocumentPermissionSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentPermission
        fields = ('user', 'can_read', 'can_update', 'can_delete', )
