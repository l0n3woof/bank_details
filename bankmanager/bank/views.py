from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q

from .models import BankDetails

class IfscDetails(APIView):
    def post(self, request):
        ifsc = request.data['ifsc']
        bank_details = BankDetails.objects.filter(ifsc_code=ifsc).values()[0]
        del bank_details['id']
        return Response(bank_details)

class BranchDetails(APIView):
    def post(self, request):
        bank = request.data['bank']
        bank_city = request.data['city']
        banks = BankDetails.objects.filter(Q(bank_name=bank) & Q(city=bank_city))
        banks_list = []
        for b in banks:
            banks_list.append({'branch':b.branch, 'ifsc_code':b.ifsc_code, 'bank_id':b.bank_id,\
            'bank_address':b.bank_address, 'city':b.city, 'district':b.district, 'state': b.state, 'bank_name':b.bank_name})
        return Response({'branchs': banks_list})
