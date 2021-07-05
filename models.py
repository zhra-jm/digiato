from datetime import datetime

from peewee import Model, TextField, CharField, DateTimeField, BooleanField
from playhouse.db_url import connect


database = connect('mysql://zahra:3078@127.0.0.1:3306/digiato')


class BaseModel(Model):
    class Meta:
        database = database

    def __str__(self):
        return str(self.id)


class Digiato(BaseModel):
    link = TextField()
    title = TextField(null=True)
    author = CharField(max_length=32, null=True)
    date_written = CharField(max_length=32, null=True)
    date = DateTimeField(default=datetime.now())
    pdf_link = TextField(null=True)
    text = TextField(null=True)
    flag = BooleanField(default=False)

    @staticmethod
    def create_data_table():
        database.create_tables(
            [Technology, Mobile, Car, Business, HowStuffWorks, Science, Review]
        )

    @staticmethod
    def reader(model_list):
        for model in model_list:
            return model.select().model.link

    @staticmethod
    def update_flag():
        pass


class Technology(Digiato):
    pass


class Mobile(Digiato):
    pass


class Car(Digiato):
    pass


class Business(Digiato):
    pass


class HowStuffWorks(Digiato):
    pass


class Science(Digiato):
    pass


class Review(Digiato):
    pass
