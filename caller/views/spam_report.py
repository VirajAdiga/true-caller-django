from rest_framework import generics, permissions
from caller.models import SpamReport
from caller.serializers import SpamReportSerializer


class SpamReportView(generics.CreateAPIView):
    queryset = SpamReport.objects.all()
    serializer_class = SpamReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)
