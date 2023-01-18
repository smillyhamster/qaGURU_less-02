from selene.support.shared import browser
from selene import have, be


def test_google_good_search(open_browser):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests'))


def test_google_bad_search(open_browser):
    browser.element('[name=q]').should(be.blank).type('sdfg5245tfg2452134sgsdfg').press_enter()
    browser.element('[id=topstuff]').should(
        have.text('Your search - sdfg5245tfg2452134sgsdfg - did not match any documents.'))
