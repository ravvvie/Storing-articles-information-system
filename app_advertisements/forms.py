from django import forms
from .models import Article, ArticleImage, HistoricalPerson


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ArticleForm(forms.ModelForm):
    images = MultipleFileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['scope'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['persons'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['images'].widget.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        model = Article
        fields = "__all__"
        exclude = "author", "is_published"

    def save(self, commit=True, author=None):
        result = super().save(commit=commit)
        result.author = author
        result.save()
        for image in self.cleaned_data['images']:
            ArticleImage.objects.create(
                article=result,
                image=image,
            )
        for person in self.cleaned_data['persons']:
            result.persons.add(person)
        return result
