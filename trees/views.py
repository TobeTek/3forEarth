from django.shortcuts import render
from rest_framework import generics, permissions
# Create your views here.
from .models import Tree, TreeType
from .serializers import TreeSerializer, TreeTypeSerializer
from .permissions import IsSponsorOrReadOnly, IsCompanyOrReadOnly

class TreeListView(generics.ListCreateAPIView):
    permissions_class = (permissions.IsAuthenticated,)
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
class SponsorTreeListView(generics.ListCreateAPIView):
    def get_current_user(self):
        return self.request.user
    permissions_class = (IsSponsorOrReadOnly,)
    queryset = Tree.objects.all()
class TreeDetailView(generics.RetrieveUpdateDestroyAPIView):
    def dispatch(self,request, *args,**kwargs):
        print(self.request)
        return super(TreeDetailView,self).dispatch(request, *args,**kwargs)
    queryset = Tree.objects.all()
    permissions_class= (permissions.IsAuthenticated,)
    serializer_class = TreeSerializer
    def test_user(self):
        print(self.request.user.is_company) 
class TreeTypeListView(generics.ListCreateAPIView):
    permissions_class = (permissions.IsAuthenticated,)
    queryset = TreeType.objects.all()
    serializer_class = TreeTypeSerializer

