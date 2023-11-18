from selene.api import *
import os

from selene.core.command import js
import allure


class RegistrationPage:
    def open(self):
        with allure.step('Open registration page'):
            browser.open(f'https://demoqa.com/automation-practice-form')
        return self

    def close_banner(self):
        with allure.step('Close banner'):
            browser.execute_script('document.querySelector("#fixedban").remove()')
        return self

    def fill_first_name(self, value):
        with allure.step(f'Fill first name: {value}'):
            browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        with allure.step(f'Fill last name: {value}'):
            browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_user_email(self, value):
        with allure.step(f'Fill user email: {value}'):
            browser.element('#userEmail').should(be.blank).type(value)
        return self

    def select_gender(self, value):
        with allure.step(f'Select gender: {value}'):
            browser.element(f'[value={value}] + label').click()
        return self

    def fill_user_number(self, value):
        with allure.step(f'Fill user number: {value}'):
            browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        with allure.step(f'Fill date of birth: {year}-{month}-{day}'):
            browser.element('#dateOfBirthInput').click()
            browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(month)).click()
            browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(year)).click()
            browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        with allure.step(f'Fill subject: {value}'):
            browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        return self

    def fill_hobby(self, value):
        with allure.step(f'Fill hobby: {value}'):
            browser.element(f"//*[contains(text(),'{value}')]").click()
        return self

    def upload_picture(self, value):
        with allure.step(f'Upload picture: {value}'):
            browser.element('#uploadPicture').send_keys(os.path.abspath(f'resources/{value}'))
        return self

    def fill_current_address(self, value):
        with allure.step(f'Fill current address: {value}'):
            browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def fill_state(self, value):
        with allure.step(f'Fill state: {value}'):
            browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def fill_city(self, value):
        with allure.step(f'Fill city: {value}'):
            browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def submit(self):
        with allure.step('Submit the form'):
            browser.element('#submit').should(be.visible).perform(command=js.click)
        return self

    def should_register_user(self, *result):
        with allure.step('Verify user registration'):
            browser.element('.table').all('td').even.should(
                have.exact_texts(result))
        return self


registration_page = RegistrationPage()
