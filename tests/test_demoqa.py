from selene import browser, have
import os

def test_input_data():
    browser.open('/automation-practice-form')   # Перейти на сайт
    browser.element('#firstName').type('DARYA')  # Активировать поле Name, ввести имя
    browser.element('#lastName').type('TRUFANOVA') # Активировать поле Last Name,ввести фамилию
    browser.element('#userEmail').type('ch.irka@yandex.ru')   # Активировать поле Email, ввести адрес эл.почты

    browser.element('//label[contains(text(),"Female")]').click() # Выбрать пол Female

    browser.element('#userNumber').type('0123456789')   # Активировать поле Mobile, ввести номер телефона

    browser.element('#dateOfBirthInput').click()    # Активировать поле Date of Birth
    browser.element('.react-datepicker__year-select > option[value="2000"]').click()    # Активировать поле Год и выбрать из выпадающего списка 2000
    browser.element('.react-datepicker__month-select > option[value="11"]').click()     # Активировать поле Месяц и выбрать из выпадающего списка Декабрь
    browser.element('.react-datepicker__day--007').click()   # Выбрать дату 07.12.2000

    browser.element('#subjectsInput').type('Maths').press_enter()  # Активировать поле Subjects, ввести Maths

    browser.element('//label[contains(text(),"Music")]').click()   # Установить флаг у поля Music

    browser.element('#uploadPicture').send_keys(os.path.abspath("ya.jpg"))  # Нажать на кнопку "Выберите файл" и загрузить файл "ya.jpg"
    # Проверить, что инф. текст = "ya.jpg"

    browser.element('#currentAddress').type('Moscow')  # Активировать поле Current Address, ввести Moscow

    browser.element('#react-select-3-input').type('NCR').press_enter()   # Открыть выпадающий список Select State, выбрать NCR
    browser.element('#react-select-4-input').type('Delhi').press_enter() # Открыть выпадающий список Select City, выбрать Delhi

    browser.element('#submit').click() # Нажать кнопку Submit

    browser.element('//td[preceding-sibling::td[contains(.,"Student Name")]]').should(have.exact_text('DARYA TRUFANOVA'))
    browser.element('//td[preceding-sibling::td[contains(.,"Student Email")]]').should(have.exact_text('ch.irka@yandex.ru'))
    browser.element('//td[preceding-sibling::td[contains(.,"Gender")]]').should(have.exact_text('Female'))
    browser.element('//td[preceding-sibling::td[contains(.,"Mobile")]]').should(have.exact_text('0123456789'))
    browser.element('//td[preceding-sibling::td[contains(.,"Date of Birth")]]').should(have.exact_text('07 December,2000'))
    browser.element('//td[preceding-sibling::td[contains(.,"Subjects")]]').should(have.exact_text('Maths'))
    browser.element('//td[preceding-sibling::td[contains(.,"Hobbies")]]').should(have.exact_text('Music'))
    browser.element('//td[preceding-sibling::td[contains(.,"Picture")]]').should(have.exact_text('ya.jpg'))
    browser.element('//td[preceding-sibling::td[contains(.,"Address")]]').should(have.exact_text('Moscow'))
    browser.element('//td[preceding-sibling::td[contains(.,"State and City")]]').should(have.exact_text('NCR Delhi'))

    browser.element('#closeLargeModal').click() # Нажать кнопку Close