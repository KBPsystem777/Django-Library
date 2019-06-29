from django.db import models
from django.urls import reverse
import uuid

# Genre Model
class Genre(models.Model):
    # Model representing a book Genre
    name = models.CharField(max_length=200, help_text="Enter the book genre (e.g. Horror, History)")

    def __str__(self):
        # String for representing the Model object
        return self.name


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text="Enter a brief description about the book")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN Number</a>')

    # Many to many fields cause genre contains many books.
    # Books can cover many genre
    genre = models.CharField('ISBN', max_length=13, help_text="Select a genre of this book")

    def __str__(self):
        # String for representing object model
        return self.title
    def get_absolute_url(self):
        # Returns a url to access a detail record of this book
        return reverse('book-detail', args=[str(self.id)])

# Author model
class Author(models.Model):
    ''' Model representing an author '''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        # Returns a url to access a particular author instance
        return reverse('author_detail', args=[str(self.id)])
    
    def __str__(self):
        # String for representing the obj model
        return f'{self.last_name}, {self.first_name}'

#Book Instance
class BookInstance(models.Model):
    '''Model representing a specificc copy of the book'''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this book")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.DateField(null=True, blank=True)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On-Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices = LOAN_STATUS,
        blank = True,
        default = 'm',
        help_text = 'Book Availability'
    )

    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        '''String for representing a Model Object'''
        return f'{self.id}({self.book.title})'
