from django.db import models

from django.db.models import UniqueConstraint 
from django.db.models.functions import Lower
from django.urls import reverse 
# Create your models here.
# my_feild_name = models.Charfield(max_length=20, help_text='Enter field documentation') example of a field/column of data 

class Genre(models.Model):
    #Model representing a book genre

    name = models.CharField(
        max_length=200,
        unique=True, 
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
    )
 #String for representing the Model object
    def _str_(self):
        return self.name
    
    #return the url to access a particular genre instance. 
    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])

    class Meta: 
        Constraints = [
            UniqueConstraint(
                Lower('name'),
                name = "genre_name_case_insensitive_unique",
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]

        class Book(models.Model):
            title = models.Chatfield(max_length=200)
            author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True) #used FK because book can only have one author, but author can have many books
            summary = models.TextField(maxlength=13,
                                       unique=True,
                                       help_text= '13 Character <a href="https://www.isbn-international.org/content/what-isbn')
            
            #many to many genrs can contain many books and Books can cover many genres. 

            #b.c Genre class has been created we can specify the object above 

            genre = models.ManyToManyField(
                Genre, help_text = "Select a genre for this book")
            
            def _str_(self):
                return self.title
            
            def get_absolute_url(self):
                return reverse('book-detail', args=[str(self.id)])
import uuid # Required for unique book instances

class BookInstance(models.Model):

    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'