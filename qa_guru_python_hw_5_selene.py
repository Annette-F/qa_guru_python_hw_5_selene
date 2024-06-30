import random

from selene import browser, by, be, have

def test_filling_and_sending_input(setting_browser):
    browser.open('/automation-practice-form')
    browser.element('[id=firstName]').should(be.blank).type('Anna')
    browser.element('[id=lastName]').should(be.blank).type('Fedorova')
    browser.element('[id=userEmail]').should(be.blank).type('email@mail.com')
    browser.element('[for=gender-radio-2]').click()
    browser.element('[id=userNumber]').should(be.blank).type('9001234567')
    # browser.element('[.react-datepicker__year-select]').element('[value=1982]').click()
    # browser.element('[.react-datepicker__month-select]').element('[value=2]').click()
    # browser.element('[class="react-datepicker__day react-datepicker__day--018"]').click()
    browser.element('[id=subjectsInput]').should(be.blank).type('AQA')
    # browser.element('for=hobbies-checkbox-1').click()
