from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_registration_user():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    (
    registration_page
    .fill_first_name('DARYA')
    .fill_last_name('TRUFANOVA')
    .fill_email('ch.irka@yandex.ru')
    .select_gender()
    .fill_mobile('0123456789')
    .fill_date_of_birth('2000', 'December', '10')
    .fill_subjects('Maths')
    .select_hobbies()
    .upload_picture('ya.jpg')
    .fill_current_address('Moscow')
    .select_state_and_city('NCR', 'Delhi')

    .submit_form()
    )

    # THEN
    registration_page.should_have_registered(
            'DARYA',
            'TRUFANOVA',
            'ch.irka@yandex.ru',
            'Female',
            '0123456789',
            '10 December,2000',
            'Maths',
            'Music',
            'ya.jpg',
            'Moscow',
            'NCR',
            'Delhi'
        )
