from django.shortcuts import render
from rest_framework import generics

# Create your views here.
class ClassCreateView(generics.CreateAPIView):
    permission_classes = (CanCreateMenu,)
    serializer_class = MenuCSerializer

    def perform_create(self, serializer):
        serializer.save(cafe=get_object_or_404(Cafe, pk=self.kwargs.get('cafe_id')),
                        staff=self.request.user.user_profile)
