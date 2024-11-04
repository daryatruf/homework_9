from selene import have, command
from selene.support.shared import browser
from urllib3.util.wait import select_wait_for_socket

from demoqa_tests.resource import path


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('//label[contains(text(),"Female")]')
        self.mobile = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element('//label[contains(text(),"Music")]')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.select_state = browser.element('#state')
        self.select_city = browser.element('#city')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def select_gender(self):
        self.gender.click()
        return self

    def fill_mobile(self, value):
        self.mobile.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subjects(self, value):
        self.subjects.type(value).press_enter()
        return self

    def select_hobbies(self):
        self.hobbies.click()
        return self

    def upload_picture(self,value):
        self.picture.set_value(path(value))
        return self

    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    def select_state_and_city(self, state, city):
        self.select_state.click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()
        self.select_city().click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()
        return self

    def submit_form(self):
        browser.element('#submit').click()

    def should_have_registered(self, first_name, last_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture, address, state, city):
        browser.element('.modal-content').element('table').all('td').even.should(
            have.exact_texts(
            (f'{first_name} {last_name}'),
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            address,
            (f'{state} {city}')
        )
    )
        return self
