from .models import Subscriber
from django.forms import ModelForm


class SubscriberForm(ModelForm):

    class Meta:
        model = Subscriber
        fields = ['email']
