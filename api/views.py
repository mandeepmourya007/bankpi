from django.shortcuts import render
from . models import bank,branch
from rest_framework import viewsets
from .serializers import BankSerializer,BranchSerializer



def index(request):


    return render(request,"index.html")



class BankViewSet(viewsets.ModelViewSet):
    
    queryset = bank.objects.all()
    serializer_class =BankSerializer

class BranchViewSet(viewsets.ModelViewSet):
    
    queryset = branch.objects.all()
    serializer_class =BranchSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        # bank,city = self.kwargs['data'].split('-')
        # bank = self.request.query_params.get('bank', None)
        # city = self.request.query_params.get('city', None)
        # bankid =bank.objects.filter(name=bank)
        # print(bankid)
        queryset = branch.objects.all()
        return      queryset#Purchase.objects.filter(purchaser__username=username)
