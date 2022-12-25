from selene.support.shared import browser
from selene import be, have

browser.open('https://demoqa.com/automation-practice-form')
browser.element('.main-header').should(have.text('Practice Form'))
browser.element('#firstName').should(be.blank).type('Вася')
browser.element('#lastName').should(be.blank).type('Неизвестный')
browser.element('#userEmail').should(be.blank).type('vasya@yandex.ru')
browser.element('#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label').click()
browser.element('#userNumber').should(be.blank).type('70000000000')
browser.element('#subjectsInput').should(be.blank).type('Some test for subject')
browser.element('#currentAddress').should(be.blank).type('some address')
browser.element('#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label').click()

