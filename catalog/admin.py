from django.contrib import admin

from .models import Author, Language, Genre, Book, BookInstance


# BookInline
########################################################################
class BookInline(admin.TabularInline):
    """
    Defines format of `Book` inline insertion.
    """
    model = Book
########################################################################

# Author
########################################################################
# admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'date_of_birth',
        'date_of_death',
    )
    fields = [
        'first_name',
        'last_name',
        (
            'date_of_birth',
            'date_of_death',
        ),
    ]
    inlines = [
        BookInline,
    ]

# admin.site.register(Author, AuthorAdmin)
########################################################################


# Language
########################################################################
# admin.site.register(Language)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    fields = [
        'name',
    ]
########################################################################


# Genre
########################################################################
# admin.site.register(Genre)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    fields = [
        'name',
    ]
########################################################################


# BookInstanceInline
########################################################################
class BookInstanceInline(admin.TabularInline):
    """
    Defines format of `BookInstance` inline insertion.
    """
    model = BookInstance
########################################################################


# Book
########################################################################
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'display_genre',
    )
    fields = [
        'title',
        'author',
        'summary',
        'isbn',
        'genre',
        'language',
    ]
    inlines = [
        BookInstanceInline,
    ]
########################################################################


# BookInstance
########################################################################
# admin.site.register(BookInstance)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'status',
        'borrower',
        'due_back',
        'id',
    )
    list_filter = (
        'status',
        'due_back',
    )
    fieldsets = (
        ('General Information', {
            'fields': (
                'book',
                'imprint',
                'id',
            ),
        }),
        ('Availability', {
            'fields': (
                'status',
                'due_back',
                'borrower',
            ),
        }),
    )
########################################################################


