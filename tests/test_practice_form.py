from selene import browser, have

from demoqa_tests.pages.registration_page import RegistrationPage


def test_registration_user():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('DARYA')
    registration_page.fill_last_name('TRUFANOVA')
    registration_page.fill_email('ch.irka@yandex.ru')
    registration_page.select_gender('Female')
    registration_page.fill_mobile('0123456789')
    registration_page.fill_date_of_birth('2000', 'December', '10')
    browser.element('#subjectsInput').type('Maths').press_enter()  # Активировать поле Subjects, ввести Maths

    registration_page.select_hobbies('Music')
    registration_page.upload_picture('ya.jpg')
    registration_page.fill_current_address('Moscow')

    browser.element('#react-select-3-input').type('NCR').press_enter()   # Открыть выпадающий список Select State, выбрать NCR
    browser.element('#react-select-4-input').type('Delhi').press_enter() # Открыть выпадающий список Select City, выбрать Delhi

    browser.element('#submit').click() # Нажать кнопку Submit

    # THEN
    browser.element('//td[preceding-sibling::td[contains(.,"Student Name")]]').should(have.exact_text('DARYA TRUFANOVA'))
    browser.element('//td[preceding-sibling::td[contains(.,"Student Email")]]').should(have.exact_text('ch.irka@yandex.ru'))
    browser.element('//td[preceding-sibling::td[contains(.,"Gender")]]').should(have.exact_text('Female'))
    browser.element('//td[preceding-sibling::td[contains(.,"Mobile")]]').should(have.exact_text('0123456789'))
    browser.element('//td[preceding-sibling::td[contains(.,"Date of Birth")]]').should(have.exact_text('10 December,2000'))
    browser.element('//td[preceding-sibling::td[contains(.,"Subjects")]]').should(have.exact_text('Maths'))
    browser.element('//td[preceding-sibling::td[contains(.,"Hobbies")]]').should(have.exact_text('Music'))
    browser.element('//td[preceding-sibling::td[contains(.,"Picture")]]').should(have.exact_text('ya.jpg'))
    browser.element('//td[preceding-sibling::td[contains(.,"Address")]]').should(have.exact_text('Moscow'))
    browser.element('//td[preceding-sibling::td[contains(.,"State and City")]]').should(have.exact_text('NCR Delhi'))

    browser.element('#closeLargeModal').click() # Нажать кнопку Close