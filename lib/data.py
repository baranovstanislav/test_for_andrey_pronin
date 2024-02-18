from selenium.webdriver.common.by import By


class Data:
    @staticmethod
    def journal_link(name):
        return By.XPATH, f'//p[contains(text(), "{name}")]'

    @staticmethod
    def switch_language_link(language):
        return By.CSS_SELECTOR, f".inner--desktop .lang-toggler__btn[value='{language}']"

    URL = 'https://pajis.archeo.ru/'

    LANGUAGE_LIST = ('ru', 'en')

    OLD_JOURNAL_NAMES_LIST = {'ru': ('Первобытная археология. Журнал междисциплинарных исследований, 2019, №1',
                                     'Первобытная археология. Журнал междисциплинарных исследований, 2019, №2',
                                     'Первобытная археология. Журнал междисциплинарных исследований, 2020, №1',
                                     'Первобытная археология. Журнал междисциплинарных исследований, 2020, №2',
                                     'Первобытная археология. Журнал междисциплинарных исследований, 2021, №1',
                                     'Первобытная археология. Журнал междисциплинарных исследований, 2021, №2',
                                     'Первобытная археология. Журнал междисциплинарных исследований, 2022, №1',
                                     'Первобытная археология. Журнал междисциплинарных исследований, 2022, №2',
                                     'Первобытная археология. Журнал междисциплинарных исследований, 2023, №1'),
                              'en': ('PREHISTORIC ARCHAEOLOGY. JOURNAL OF INTERDISCIPLINARY STUDIES, 2019, №1',
                                     'PREHISTORIC ARCHAEOLOGY. JOURNAL OF INTERDISCIPLINARY STUDIES, 2019, №2',
                                     'PREHISTORIC ARCHAEOLOGY. JOURNAL OF INTERDISCIPLINARY STUDIES, 2020, №1',
                                     'PREHISTORIC ARCHAEOLOGY. JOURNAL OF INTERDISCIPLINARY STUDIES, 2020, №2',
                                     'PREHISTORIC ARCHAEOLOGY. JOURNAL OF INTERDISCIPLINARY STUDIES, 2021, №1',
                                     'PREHISTORIC ARCHAEOLOGY. JOURNAL OF INTERDISCIPLINARY STUDIES, 2021, №2',
                                     'PREHISTORIC ARCHAEOLOGY. JOURNAL OF INTERDISCIPLINARY STUDIES, 2022, №1',
                                     'PREHISTORIC ARCHAEOLOGY. JOURNAL OF INTERDISCIPLINARY STUDIES, 2022, №2',
                                     'PREHISTORIC ARCHAEOLOGY. JOURNAL OF INTERDISCIPLINARY STUDIES, 2023, №1')}

    CURRENT_JOURNAL_NAMES_LIST = {'ru': 'Первобытная археология. Журнал междисциплинарных исследований, 2023, №2',
                                  'en': 'PREHISTORIC ARCHAEOLOGY. JOURNAL OF INTERDISCIPLINARY STUDIES, 2023, №2'}

    ARCHIVE_LINK = (By.CSS_SELECTOR, '.menu__nav > [href="/archive/"]')

    CURRENT_JOURNAL_LINK = (By.CSS_SELECTOR, '.menu__nav > [href="/current-issue/"]')

    JOURNAL_PAGE_TITLE = (By.CSS_SELECTOR, '.main h2.page__title')

    BUTTON_SIDE_MENU = (By.CSS_SELECTOR, 'button.header__burger-btn.burger-btn')
