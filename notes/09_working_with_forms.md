# Django Tutorial Part 9: Working with forms

* <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms>

## Useful Descriptions

* `Binding data to the form means that the user-entered data and any errors are available when we need to redisplay the form.`

## Alternate Versions of Code

* `RenewBookModelForm`

  * [`catalog/forms.py`](./catalog/forms.py):

    ```python
    from django.forms import ModelForm

    from catalog.models import BookInstance

    class RenewBookModelForm(ModelForm):
        def clean_due_back(self):
        data = self.cleaned_data['due_back']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data

        class Meta:
            model = BookInstance
            fields = ['due_back']
            labels = {'due_back': _('Renewal date')}
            help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')}
    ```

  * [`catalog/views.py`](./catalog/views.py):

    ```python
    #...
    def renew_book_librarian(request, pk):
        """
        View function for a Librarian to renew a specific `BookInstance`.
        """
        book_instance = get_object_or_404(BookInstance, pk=pk)

        if request.method == 'POST':
            #...
            form = RenewBookModelForm(request.POST)
            #...
        else:
            #...
            form = RenewBookModelForm(initial={'due_back': proposed_renewal_date})
            #...

        return render(request, 'catalog/book_renew_librarian.html', context)
    ```

## Current Location

* <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#views>
