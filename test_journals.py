from lib.base_cases import BaseCases
from lib.data import Data
import pytest
from lib.Environment import website_language


class TestJournalsShouldRemain:
    # Определяем нужный язык вебсайта через переменную окружения LANG_ENV.
    # Если переменная не назначена, то по умолчанию выбирается русский язык (ru)

    language = website_language.get_website_language()
    names_old = Data.OLD_JOURNAL_NAMES_LIST.copy()[language]
    current_journal_name = Data.CURRENT_JOURNAL_NAMES_LIST.copy()[language]

    @pytest.mark.old_journal
    @pytest.mark.parametrize('old_journal_name', names_old)
    def test_old_journal_should_be_in_archive(self, browser, old_journal_name):
        page = BaseCases(browser)
        page.open()
        page.switch_language(self.language)
        page.go_to_side_menu()
        page.go_to_archive_page()
        page.should_be_journal_in_archive(old_journal_name)
        page.go_to_journal_page(old_journal_name)
        page.should_be_journal_on_journal_page(old_journal_name)

    @pytest.mark.current_journal
    def test_current_journal_should_be_in_current_issue(self, browser):
        page = BaseCases(browser)
        page.open()
        page.switch_language(self.language)
        page.go_to_side_menu()
        page.go_to_current_issue_catalog()
        page.should_be_journal_on_journal_page(self.current_journal_name)
