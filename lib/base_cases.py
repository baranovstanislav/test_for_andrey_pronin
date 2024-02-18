from selenium.common.exceptions import NoSuchElementException
from lib.data import Data


class BaseCases:
    def __init__(self, browser, timeout=5):
        self.browser = browser
        self.url = Data.URL
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):

        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_journal_in_archive(self, name):
        assert self.is_element_present(*Data.journal_link(name)), f"journal {name} is not presented in archive"

    def go_to_journal_page(self, name):
        journal_link = self.browser.find_element(*Data.journal_link(name))
        journal_link.click()

    def should_be_journal_on_journal_page(self, name):
        expected_journal_name = name.lower()

        actual_journal_name = self.browser.find_element(*Data.JOURNAL_PAGE_TITLE).text.strip().lower()

        assert expected_journal_name == actual_journal_name, f'journal {expected_journal_name} is not presented on page'

    def go_to_side_menu(self):

        assert self.is_element_present(*Data.BUTTON_SIDE_MENU), "side menu button is not presented"

        archive_link = self.browser.find_element(*Data.BUTTON_SIDE_MENU)
        archive_link.click()

    def go_to_archive_page(self):

        assert self.is_element_present(*Data.ARCHIVE_LINK), "archive link is not presented"

        archive_link = self.browser.find_element(*Data.ARCHIVE_LINK)
        archive_link.click()

    def go_to_current_issue_catalog(self):

        assert self.is_element_present(*Data.CURRENT_JOURNAL_LINK), "current issue link is not presented"

        journal_link = self.browser.find_element(*Data.CURRENT_JOURNAL_LINK)
        journal_link.click()

    def switch_language(self, language):
        assert self.is_element_present(*Data.switch_language_link(language)), "switch language button is not presented"

        switch_language_link = self.browser.find_element(*Data.switch_language_link(language))
        switch_language_link.click()
