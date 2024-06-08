from django.db import models

from django.db.models import UniqueConstraint 
from django.db.models.functions import Lower 

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
