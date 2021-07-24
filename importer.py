from models import Link, Technology, Mobile, Car, Business, HowStuffWorks, Science, Review


class BaseImporter:
    model = None
    cat_name = None

    @classmethod
    def load(cls, class_list):
        instances = list()

        for instance in class_list:
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
            print(_class.load(dic[_class.cat_name]))

    @staticmethod
    def link_importer(link_list):
        instances = list()
        for instance in link_list:
            instances.append(LinkImporter.model.create(**instance))
        return instances


class LinkImporter(BaseImporter):
    model = Link
    cat_name = 'link'


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
