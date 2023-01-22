# MDN Local Library Tutorial

Code for learning some concepts used in MDN's Local Library tutorial.

## Purposes

* Use this tutorial to review Django testing concepts.
  * Testing knowledge is needed for my portfolio app.
* Use this tutorial to review how to modify Django Admin interface.

## Concepts I Need to Further Explore

* <https://docs.djangoproject.com/en/4.1/ref/exceptions/#django.core.exceptions.ValidationError>
  * [`catalog/forms.py`](./catalog/forms.py) - Line 19

## Interesting Concept Descriptions

* `Binding`:
  * "However, if this is a POST request, then we create our form object and populate it with data from the request. This process is called "binding" and allows us to validate the form."
  * "Binding" is the process of creating a form object from the data provided by the user, and any other 'hidden' data.

## Resources

* [Django Tutorial: The Local Library website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
* [The Django admin documentation generator](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/)
* MDN's [django-locallibrary-tutorial](https://github.com/mdn/django-locallibrary-tutorial) fully developed app
* `brucestull`'s [mdn-local-library-tutorial](https://github.com/brucestull/mdn-local-library-tutorial) repository
