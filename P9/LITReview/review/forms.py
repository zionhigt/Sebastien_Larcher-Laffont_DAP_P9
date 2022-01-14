from django import forms
from review.models import Review


class CreateReviewForm(forms.ModelForm):
    RATING_CHOISES = [(i, f"-{i}") for i in range(5 + 1)]
    rating_choices = forms.ChoiceField(label="Note", choices=RATING_CHOISES, widget=forms.RadioSelect)

    class Meta:
        model = Review
        fields = ('rating_choices', 'headline', 'body')
