from selene.support.shared import browser

from demoqa_tests.resources import resource_path


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
        # browser.element('#react-select-3-input').type(
        #    'NCR').press_enter()  # Открыть выпадающий список Select State, выбрать NCR
        # browser.element('#react-select-4-input').type(
        #    'Delhi').press_enter()  # Открыть выпадающий список Select City, выбрать Delhi

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def select_gender(self, value):
        self.gender.click(value)

    def fill_mobile(self, value):
        self.mobile.type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()  # Активировать поле Date of Birth
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    browser.element('#subjectsInput').type('Maths').press_enter()  # Активировать поле Subjects, ввести Maths

    def select_hobbies(self, value):
        self.hobbies.click(value)

    def upload_picture(self,value):
        self.picture.set_value(resource_path(value))

    def fill_current_address(self, value):
        self.current_address.type(value)

    browser.element('#react-select-3-input').type(
        'NCR').press_enter()  # Открыть выпадающий список Select State, выбрать NCR
    browser.element('#react-select-4-input').type(
        'Delhi').press_enter()  # Открыть выпадающий список Select City, выбрать Delhi

    browser.element('#submit').click()  # Нажать кнопку Submit

