from datetime import datetime

from peewee import Model, TextField, CharField, DateTimeField, BooleanField
from playhouse.db_url import connect

database = connect('mysql://zahra:3078@127.0.0.1:3306/digiato')


class BaseModel(Model):
    class Meta:
        database = database

    def __str__(self):
        return str(self.id)


class Link(BaseModel):
    link = TextField()
    model_name = CharField(max_length=32)
    flag = BooleanField(default=False)


class Digiato(BaseModel):
    title = TextField(null=True)
    author = CharField(max_length=32, null=True)
    date_written = CharField(max_length=32, null=True)
    date = DateTimeField(default=datetime.now())
    pdf_link = TextField(null=True)
    text = TextField(null=True)

    @staticmethod
    def create_data_table():
        database.create_tables(
            [Technology, Mobile, Car, Business, HowStuffWorks, Science, Review, Link]
        )

    @staticmethod
    def link_reader():
        link_model = {'tech': [], 'mobile': [], 'car': [], 'business': [],
                      'howstuffworks': [], 'science': [], 'dgreview': []}
        for obj in Link.select():
            for link_model_name in link_model.keys():
                if link_model_name == obj.model_name:
                    link_model[link_model_name].append([obj.link, obj.id])
        return link_model

    @staticmethod
    def update_flag(link_id):
        q = Link.update(flag=True).where(Link.id == link_id)
        q.execute()


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
