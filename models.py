from datetime import datetime

from peewee import Model, TextField, CharField, DateTimeField, BooleanField
from info import database


class BaseModel(Model):
    class Meta:
        database = database

    def __str__(self):
        return str(self.id)


class Link(BaseModel):
    link = TextField()
    model_name = CharField(max_length=32)
    flag = BooleanField(default=False)

    @classmethod
    def link_importer(cls, link_list):
        instances = list()
        for instance in link_list:
            instances.append(cls.create(**instance))
        print(instances)


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

    @staticmethod
    def loader(dic):
        importer_dict = {Technology: 'tech', Mobile: 'mobile', Car: 'car',
                         Business: 'business', HowStuffWorks: 'howstuffworks',
                         Science: 'science', Review: 'dgreview'
                         }
        for _class, cat in importer_dict.items():
            print(_class.load(dic[cat]))

    @classmethod
    def load(cls, class_list):
        instances = list()

        for instance in class_list:
            instances.append(cls.create(**instance))

        return instances


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
