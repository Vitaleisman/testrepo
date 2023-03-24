import re
import os
from playwright.sync_api import Page, Error, expect
from dotenv import load_dotenv

class Criteria():
    
    def __init__(self):
        load_dotenv()
        self.URL = os.getenv('URL')

    def goto_criteria(self, page: Page):
        page.goto(self.URL+'home')
        page.get_by_test_id("header-component__nav__link-skillpool-page").click()
        page.get_by_test_id("skill-pool-page__action-bar__new-entity-button").click()
        page.get_by_test_id("skill-content-from__question-input").fill('Vitalya Lox')
        page.get_by_test_id("skill-content-from__answer-input").fill('Vitalya Lox')
        page.get_by_test_id("skill-content-from__comment-input").fill('Vitalya Lox')
        page.get_by_test_id("skill-content-from__submit").click()
        #page.get_by_test_id("skill-pool-page__elements-527__dropdown").click()
        #page.get_by_test_id("skill-pool-page__elements-527__edit-button").click()
        #page.get_by_test_id("skill-content-form__skill-set-select").click()
        #page.get_by_test_id("skill-content-from__submit").click()
        #page.locator.select_option(value="TEST")

        page.get_by_test_id("skill-pool-page__action-bar__filters-skillset-select").click()
        page.locator.select_option(value="TEST")
        #page.get_by_test_id("skill-pool-page__action-bar__filters-skillset__value-TEST").click()
        #page.get_by_test_id("skill-pool-page__action-bar__filters-skillset__value-REST").click()

        page.wait_for_timeout(4000)
        
