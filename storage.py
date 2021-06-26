from models import database, Technology, Mobile, Car, Business, HowStuffWorks, Science, Review
from importer import TechnologyImporter, MobileImporter, \
    CarImporter, BusinessImporter, HowStuffWorksImporter, ScienceImporter, ReviewImporter


class MySqlStorage:

    @staticmethod
    def create_table():
        database.create_tables(
            [Technology, Mobile, Car, Business, HowStuffWorks, Science, Review]
        )

    @staticmethod
    def importer(dic):
        importer_classes = [
            TechnologyImporter, MobileImporter, CarImporter,
            BusinessImporter, HowStuffWorksImporter, ScienceImporter,
            ReviewImporter
        ]

        for _class in importer_classes:
            print(_class.load(dic))

    @staticmethod
    def reader(model_list, column):
        for model in model_list:
            return model.select().column







