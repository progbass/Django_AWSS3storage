# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Document

# Create your views here.
class DocumentCreateView(CreateView):
	model = Document
	fields = ('upload',)
	success_url = reverse_lazy('upload')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		documents = Document.objects.all()
		context['documents'] = documents
		return context