from django import forms
from review.models import Review

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('ticket', 'rating', 'headline', 'body')