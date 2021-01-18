"""Django models utilities."""

# Django
from django.db import models


class HistoryModel(models.Model):
    """Comparte Heep base model.

    HistoryModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']




# Django models utilities here.
# from django.db import models



# class ModeloAHeredar(models.model):
#     """ Comparte el base model
    
#         acts as an abstract base class from wich every
#         other model in the project will inherit. This class provides
#         every  table with the following attributes:
#             * Created (datetime): store the datetime the object was created.
#             * mofified (datetime): store the las datetime the object was modified.
#     """
#     created = models.DatetimeField(
#         'created at',
#         auto_now_add = True #graba la fecha automatica en el momento de creacion
#         help_text = 'Date time on wich the object was created.'
#     )
#     modified = models.DatetimeField(
#         'modified at',
#         auto_now = True #graba la fecha automatica en el momento de modificacion
#         help_text = 'Date time on wich the object was modified.'
#     )
#     class Meta:
#         """ Meta option """
#         # SON PROPIEDADES QUE NOS INTERESAN, como ordenamiento, etc
#         abstract = True #exponen un molde de atributos
#         # proxy extienden de una tabla ya existente
#         get_lastest_by = 'created'
#         ordering = ['-created','-modified']

# class Student(ModeloAHeredar):
#     name = models.CharField()

#     #puedo heredar la meta tambien
#     class Meta(ModeloAHeredar.Meta)
#         db_table = 'student_role'

    
# class Person(models.Model)
#     first_name = models.CharField()
#     last_name = models.CharField()

# class MyPerson(Person):
#     class Meta:
#         proxy = True
#     def say_hi(name):
    

# SI ESCRIBO MyPerson.objects.all()

#ricardo = Myperson.objects.get(pk=1)
# ricardo.say_hi()