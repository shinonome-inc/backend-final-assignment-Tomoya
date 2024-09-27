# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import TweetForm
from .models import Tweet


class HomeView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'tweets/home.html'
    context_object_name = 'tweets'
    ordering = ['-created_at']

    def get_queryset(self):
        return Tweet.objects.select_related('user').order_by('-created_at')


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    form_class = TweetForm
    template_name = 'tweets/tweet_form.html'
    success_url = reverse_lazy('tweets:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
