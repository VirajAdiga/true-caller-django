from rest_framework import generics, permissions
from caller.models.user import User
from caller.models.contact import Contact
from caller.serializers import SearchResultSerializer


class SearchView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SearchResultSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query')
        results = []
        if query:
            users = User.objects.filter(name__icontains=query)
            contacts = Contact.objects.filter(name__icontains=query)
            for user in users:
                results.append({
                    'name': user.name,
                    'phone_number': user.phone_number,
                    'email': user.email
                })
            for contact in contacts:
                results.append({
                    'name': contact.name,
                    'phone_number': contact.phone_number,
                    'email': contact.email
                })
        return results


class SearchByPhoneNumberView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SearchResultSerializer

    def get_queryset(self):
        phone_number = self.request.query_params.get('phone_number')
        results = []
        if phone_number:
            users = User.objects.filter(phone_number=phone_number)
            contacts = Contact.objects.filter(phone_number=phone_number)
            for user in users:
                results.append({
                    'name': user.name,
                    'phone_number': user.phone_number,
                    'email': user.email if self.request.user in user.contacts.all() else None
                })
            for contact in contacts:
                results.append({
                    'name': contact.name,
                    'phone_number': contact.phone_number,
                    'email': contact.email
                })
        return results
