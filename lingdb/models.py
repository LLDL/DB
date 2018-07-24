from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Adult(models.Model):
    sfuID = models.IntegerField('SFU ID')
    givenName = models.CharField(
        'Given Name', 
        max_length = 100,
    )
    surName = models.CharField(
        'Surname',
        max_length = 100,
    )
    birthDate = models.DateField(
        'Birth Date',
    )
    address = models.CharField(
        'Address',
        max_length=200,
    )
    yearsOfEducation = models.SmallIntegerField(
        'Years of Education',
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(50),
        ]
    )
    phone = models.CharField(
        max_length=50,
    )
    email = models.EmailField()

    FEMALE = 'FEMALE'
    MALE = 'MALE'
    OTHER = 'OTHER'
    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHER, 'Other'),
    )
    gender = models.CharField(
        max_length = 6, 
        choices = GENDER_CHOICES,
        default = OTHER,
    )

    PHONE = 'PHONE'
    EMAIL = 'EMAIL'
    CONTACT_CHOICES = (
        (PHONE, 'Phone'),
        (EMAIL, 'Email'),
    )
    contactPref = models.CharField(
        max_length = 5,
        choices = CONTACT_CHOICES,
        default = PHONE,
    )    


    WDM = 'WEEKDAY_MORNINGS'
    WDA = 'WEEKDAY_AFTERNOONS'
    WDE = 'WEEKDAY_EVENINGS'
    WEM = 'WEEKEND_MORNINGS'
    WEA = 'WEEKEND_AFTERNOONS'
    WEE = 'WEEKEND_EVENINGS'
    DNC = 'DO_NOT_CALL'
    ANY = 'ANYTIME'

    PHONETIME_CHOICES = (
        (WDM, 'Weekday Mornings'),
        (WDA, 'Weekday Afternoons'),
        (WDE, 'Weekday Evenings'),
        (WEM, 'Weekend Mornings'),
        (WEA, 'Weekend Afternoons'),
        (WEE, 'Weekend Evenings'),
        (DNC, 'Do Not Call'),
        (ANY, 'Anytime'),
    )

    phoneTime = models.CharField(
        max_length = 20,
        choices = PHONETIME_CHOICES,
        default = ANY,
    )

class Child(models.Model):
    givenName = models.CharField(max_length=100)
    surName = models.CharField(max_length=100)
    birthDate = models.DateField('Birth Date')
    gestationLengthWeeks = models.SmallIntegerField()
    fullTerm = models.BooleanField()
    birthWeight = models.SmallIntegerField()
    birthHeight = models.SmallIntegerField()
    personalNotes = models.TextField(max_length=1000)
    # hxRepeatedEarInfection
    # lastEarInfection
    # hereditaryAuditoryProblems
    # hereditaryLanguagePathologies
    # healthNotes

    FEMALE = 'FEMALE'
    MALE = 'MALE'
    OTHER = 'OTHER'
    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHER, 'Other'),
    )
    gender = models.CharField(
        max_length = 6, 
        choices = GENDER_CHOICES,
        default = OTHER,
    )