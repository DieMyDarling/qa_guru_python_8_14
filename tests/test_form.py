from pages.registration_page import registration_page
import allure
import pytest
from allure_commons.types import Severity


@allure.tag('web')
@allure.story('Тест сайта demoqa')
@allure.feature('Тест заполнения формы')
@allure.severity(Severity.NORMAL)
@pytest.mark.usefixtures("setup_browser")
def test_fill_form():
    with allure.step('Fill out the registration form'):
        registration_page.open()
        registration_page.close_banner()

        with allure.step('Fill out personal information'):
            (
                registration_page
                .fill_first_name('Alexey')
                .fill_last_name('Kokorev')
                .fill_user_email('test@gmail.ru')
                .select_gender('Male')
                .fill_user_number('1234567890')
                .fill_date_of_birth('1991', 'May', 15)
            )

        with allure.step('Fill out academic information'):
            (
                registration_page
                .fill_subject('Maths')
                .fill_hobby('Sports')
                .upload_picture('bat.png')
            )

        with allure.step('Fill out address information'):
            (
                registration_page
                .fill_current_address('Bali, Ubud, 1')
                .fill_state('NCR')
                .fill_city('Delhi')
                .submit()
            )

        with allure.step('Verify user registration'):
            registration_page.should_register_user(
                'Alexey Kokorev',
                'test@gmail.ru',
                'Male',
                '1234567890',
                '15 May,1991',
                'Maths',
                'Sports',
                'bat.png',
                'Bali, Ubud, 1',
                'NCR Delhi'
            )
