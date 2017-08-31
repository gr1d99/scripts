import six


class CrawlerMeta(type):
    def __new__(mcs, *args, **kwargs):
        new_class = super(CrawlerMeta)
        print(new_class)
        return new_class.__new__(mcs, *args, **kwargs)



class MyCrawler(six.with_metaclass(CrawlerMeta, object)):
    def __init__(self):
        pass