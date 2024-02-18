import os


class Environment:
    LANGUAGE_BASE = 'ru'

    LANGUAGES = ('ru', 'en')

    def __init__(self):

        try:
            self.env = os.environ['LANG_ENV']
        except KeyError:
            self.env = self.LANGUAGE_BASE

    def get_website_language(self):
        if self.env in self.LANGUAGES:
            return self.env
        else:
            raise Exception(f'Unknown value of LANG_ENV variable {self.env}')


website_language = Environment()
