from django.db.models import query
from contact.serializers import ContactSerializer
from rest_framework import generics, permissions
from contact.models import Contact


class ContactView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
