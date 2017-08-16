from importlib import import_module


def generate(module, filename):
    print import_module('.')
    # if filename == 'urls':
    #     line_one = 'from django.conf.urls import url'
    #     line_two = 'from . import views'
    #     line_three = 'urlpatterns = []'
    #     next_line = '\n'
    #     skip_two_lines = next_line * 2
    #
    #     file_name = '%(f)s.py' % dict(f=filename)
    #     data = "%(line_one)s%(next_line)s" \
    #            "%(line_two)s%(next_line)s" \
    #            "%(skip_two_lines)s" \
    #            "%(line_three)s%(next_line)s" % dict(line_one=line_one,
    #                                                 line_two=line_two,
    #                                                 line_three=line_three,
    #                                                 next_line=next_line,
    #                                                 skip_two_lines=skip_two_lines
    #                                                 )
    #
    #     print data
    #
    #     with open(file_name, 'w') as f:
    #         f.write(data)

