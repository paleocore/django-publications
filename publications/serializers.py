from rest_framework import serializers
from publications.models import Publication

class ReferenceSerializer(serializers.ModelSerializer):
	bibliographic_reference = serializers.SerializerMethodField()

	class Meta:
		model = Publication
		fields = ['bibliographic_reference']

	def get_bibliographic_reference(self, obj):
		return obj.render_reference()
