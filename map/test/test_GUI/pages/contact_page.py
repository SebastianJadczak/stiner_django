import logging


class ContactPage:
    '''Klasa odpowiedzialna za zakładkę Kontakt.'''

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.name_input_by_id = 'id_name'
        self.email_input_by_id = 'id_email'
        self.comments_textarea_by_id = 'id_comments'
        self.send_input_by_xpath = "//input[@value='Wyślij']"

    def send_message(self, name, email, comments):
        """Wypełniamy formularz wiadomoci i wysyłamy."""
        self.logger.info('Wypełnianie formularzu')
        self.driver.find_element_by_id(self.name_input_by_id).send_keys(name)
        self.driver.find_element_by_id(self.email_input_by_id).send_keys(email)
        self.driver.find_element_by_id(self.comments_textarea_by_id).send_keys(comments)
        self.driver.find_element_by_xpath(self.send_input_by_xpath).click()
