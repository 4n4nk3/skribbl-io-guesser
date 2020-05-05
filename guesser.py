from time import sleep
from re import findall
from selenium import webdriver


def build_my_regexp(word: str) -> str:
    built_regexp = r'\b'
    for letter in word:
        if letter == '_':
            built_regexp += r'\w'
        else:
            built_regexp += letter
    built_regexp += r'\b'
    return built_regexp


def search_wordlist(current_regexp: str) -> list:
    with open('English_wordlist.txt', 'r') as in_file:
        wordlist = findall(current_regexp, in_file.read())
    return wordlist



if __name__ == '__main__':
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()
    my_driver.get('https://skribbl.io/')

    while True:
        input('Press enter when ready...')
        print('Started!')

        # Get list of language that it is possible to select from dropdown menu
        guess_form = my_driver.find_element_by_id('inputChat')
        old_word = ''
        win = False
        while win is False:
            current_word = my_driver.find_element_by_id('currentWord').text
            if '_' not in current_word:
                print('I think that it\'s not your turn now!')
                break
            elif old_word != current_word:
                old_word = current_word
                sleep(2)
                guess_form.send_keys('Inizio :D')
                guess_form.submit()
                my_regexp = build_my_regexp(current_word)
                my_wordlist = search_wordlist(my_regexp)
                for word in my_wordlist:
                    sleep(0.5)
                    guess_form.send_keys(word)
                    guess_form.submit()
                    sleep(0.5)
                    messages = my_driver.find_element_by_id('boxMessages')
                    my_messages_extractor = [element.get_attribute('innerHTML') for element in
                                          messages.find_elements_by_tag_name('span')]
                    for _ in my_messages_extractor:
                        current_message = my_messages_extractor.pop()
                        if current_message == 'Inizio :D':
                            break
                        elif 'guessed the word!' in current_message:
                            win = True
                    if win:
                        break
                    else:
                        current_word = my_driver.find_element_by_id('currentWord').text
                        if current_word != old_word:
                            break

