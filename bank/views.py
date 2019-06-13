from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q

from .models import BankDetails

class IfscDetails(APIView):
    def get(self, request):
        ifsc = request.query_params.get('ifsc', None)
        if not ifsc:
             queryset = BankDetails.objects.all()
             ifsc_list = []
             for q in queryset:
                 ifsc_list.append(q.ifsc_code)
             return Response({'ifsc_list': ifsc_list})
        else:
            bank_details = BankDetails.objects.filter(ifsc_code=ifsc).values()[0]
            del bank_details['id']
            return Response(bank_details)

class BranchDetails(APIView):
    def get(self, request):
        bank = request.query_params.get('bank', None)
        bank_city = request.query_params.get('city', None)
        banks_list = []
        if not bank or not bank_city:
            queryset = BankDetails.objects.all()
            for b in queryset:
                banks_list.append({'branch':b.branch, 'ifsc_code':b.ifsc_code, 'bank_id':b.bank_id,\
                'bank_address':b.bank_address, 'city':b.city, 'district':b.district, 'state': b.state, 'bank_name':b.bank_name})
            return Response({'branchs': banks_list})
        else:
            banks = BankDetails.objects.filter(Q(bank_name=bank) & Q(city=bank_city))
            for b in banks:
                banks_list.append({'branch':b.branch, 'ifsc_code':b.ifsc_code, 'bank_id':b.bank_id,\
                'bank_address':b.bank_address, 'city':b.city, 'district':b.district, 'state': b.state, 'bank_name':b.bank_name})
            return Response({'branchs': banks_list})
