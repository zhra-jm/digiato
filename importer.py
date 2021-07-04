from models import Technology, Mobile, Car, Business, HowStuffWorks, Science, Review


class BaseImporter:
    model = None
    cat_name = None

    @classmethod
    def load(cls, dic):
        instances = list()

        for instance in dic[cls.cat_name]:
            instances.append(cls.model.create(**instance))

        return instances

    @staticmethod
    def loader(dic):
        importer_classes = [
            TechnologyImporter, MobileImporter, CarImporter,
            BusinessImporter, HowStuffWorksImporter, ScienceImporter,
            ReviewImporter
        ]

        for _class in importer_classes:
            print(_class.load(dic))


class TechnologyImporter(BaseImporter):
    model = Technology
    cat_name = 'tech'


class MobileImporter(BaseImporter):
    model = Mobile
    cat_name = 'mobile'


class CarImporter(BaseImporter):
    model = Car
    cat_name = 'car'


class BusinessImporter(BaseImporter):
    model = Business
    cat_name = 'business'


class HowStuffWorksImporter(BaseImporter):
    model = HowStuffWorks
    cat_name = 'howstuffworks'


class ScienceImporter(BaseImporter):
    model = Science
    cat_name = 'science'


class ReviewImporter(BaseImporter):
    model = Review
    cat_name = 'dgreview'


