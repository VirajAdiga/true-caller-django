from rest_framework import generics, permissions

from caller.models import SpamReport
from caller.models.user import User
from caller.models.contact import Contact
from caller.serializers import SearchResultSerializer, DetailedResultSerializer


class ConstructResultSet:
    def _construct_current_result_set(self, result_set):
        current_results = []
        for result in result_set:
            current_results.append({
                'name': result.name,
                'phone_number': result.phone_number,
                'spam_likelihood': self.get_spam_likelihood(result.phone_number)
            })
        return current_results

    def get_spam_likelihood(self, phone_number):
        return SpamReport.objects.filter(phone_number=phone_number).count()


class SearchView(generics.ListAPIView, ConstructResultSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SearchResultSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        if not query:
            return []

        # Search for users and contacts whose names start with the query
        users_start = User.objects.filter(name__istartswith=query)
        contacts_start = Contact.objects.filter(name__istartswith=query)

        # Search for users and contacts whose names contain the query but do not start with it
        users_contain = User.objects.filter(name__icontains=query).exclude(name__istartswith=query)
        contacts_contain = Contact.objects.filter(name__icontains=query).exclude(name__istartswith=query)

        results = []
        results.extend(self._construct_current_result_set(users_start))
        results.extend(self._construct_current_result_set(contacts_start))
        results.extend(self._construct_current_result_set(users_contain))
        results.extend(self._construct_current_result_set(contacts_contain))
        return results


class SearchByPhoneNumberView(generics.ListAPIView, ConstructResultSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SearchResultSerializer

    def get_queryset(self):
        phone_number = self.request.query_params.get('phone-number', '')
        if not phone_number:
            return []

        results = []

        # Search for registered users with the given phone number
        users = User.objects.filter(phone_number=phone_number)
        if users.exists():
            results.extend(self._construct_current_result_set(users))
            return results

        # If no registered users found, search for contacts with the given phone number
        contacts = Contact.objects.filter(phone_number=phone_number)
        results.extend(self._construct_current_result_set(contacts))
        return results


class DetailedView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DetailedResultSerializer

    def get_object(self):
        phone_number = self.kwargs['phone_number']
        user = User.objects.filter(phone_number=phone_number).first()
        if user:
            return user
        contact = Contact.objects.filter(phone_number=phone_number).first()
        if contact:
            return contact
        return None
