# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.core.urlresolvers import reverse

from service.models import WriteType, Writer, VisaType, Visa
from university.models import Country
from operation.models import UserCart
import json


# Create your views here.


class DocView(View):
    def get(self, request):
        all_types = WriteType.objects.all()
        all_docs = Writer.objects.all()

        type_id = request.GET.get('type', '')
        if type_id:
            all_docs = Writer.objects.filter(type=int(type_id))
        return render(request, 'doc.html', {'all_types': all_types,
                                             'all_docs': all_docs,
                                             'type_id': type_id,
                                             })

    def post(self, request):
        store_id = request.POST.get('doc_id', '')
        store_type = request.POST.get('store_type', '')

        json_data = {'status': 'success'}

        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('user:login'))
        user_cart = UserCart()
        user_cart.user = request.user
        user_cart.store_id = store_id
        user_cart.store_type = store_type
        user_cart.save()
        return HttpResponse(json.dumps(json_data), content_type="application/json")


class VisaView(View):
    def get(self, request):
        all_country = Country.objects.all()
        all_types = VisaType.objects.all()
        all_visas = Visa.objects.all()

        type_id = request.GET.get('type', '')
        if type_id:
            all_visas = Visa.objects.filter(type=int(type_id))
        return render(request, 'visa.html', {'all_types': all_types,
                                             'all_visas': all_visas,
                                             'type_id': type_id,
                                             'all_country':all_country,
                                             })


class DocDetailView(View):
    def get(self, request, doc_id):
        doc = Writer.objects.get(pk=int(doc_id))
        return render(request, 'doc-detail.html', {'doc': doc})
