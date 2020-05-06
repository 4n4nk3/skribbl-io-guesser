"""Scrape wordlists collected by skibbliohints.github.io"""

from time import sleep

from selenium import webdriver

if __name__ == '__main__':
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()

    # Loading website and waiting for it to be ready
    my_driver.get('https://skribbliohints.github.io/')
    sleep(5)

    # Get list of language that it is possible to select from dropdown menu
    lang_selector = my_driver.find_element_by_id("languageSelect")
    lang_possibilities = [x for x in lang_selector.find_elements_by_tag_name("option")]
    # Cycle each language and create its specific wordlist
    for possibility in lang_possibilities:
        possibility.click()
        sleep(5)
        lang = possibility.get_attribute('value')
        words_elements = my_driver.find_elements_by_class_name("b")
        my_words_extractor = (element.get_attribute('innerHTML') for element in words_elements)
        # Create a different file for each language
        with open(f'{lang}_wordlist.txt', 'w') as out_file:
            for word in my_words_extractor:
                out_file.write(f'{word}\n')
    my_driver.close()
