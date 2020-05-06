from time import sleep
from re import findall
from selenium import webdriver


def build_my_regexp(word: str) -> str:
    """Build regexp based on displayed characters tips."""

    built_regexp = r'\b'
    for letter in word:
        if letter == '_':
            built_regexp += r'\w'
        else:
            built_regexp += letter
    built_regexp += r'\b'
    return built_regexp


def search_wordlist(current_regexp: str) -> set:
    """Return a set of lowercase matching words because the website is case-insensitive)."""

    with open('English_wordlist.txt', 'r') as in_file:
        wordlist = set(map(str.lower, findall(current_regexp, in_file.read())))
    return wordlist


def try_and_guess(driver, word):
    sleep(0.5)
    guess_form = driver.find_element_by_id('inputChat')
    guess_form.send_keys(word)
    guess_form.submit()
    sleep(0.5)
    messages = driver.find_element_by_id('boxMessages')
    messages_extractor = [element.get_attribute('innerHTML') for element in
                          messages.find_elements_by_tag_name('span')]
    for _ in messages_extractor:
        current_message = messages_extractor.pop()
        if current_message == 'Inizio :D':
            return False
        elif 'guessed the word!' in current_message:
            return True


def play_to_win(driver) -> str:
    old_word = ''
    attempted = set()
    win = False
    current_word = driver.find_element_by_id('currentWord').text
    while win is False:
        if '_' not in current_word:
            print('I think that it\'s not your turn now!')
            break
        elif old_word != current_word:
            old_word = current_word
            sleep(2)
            guess_form = driver.find_element_by_id('inputChat')
            guess_form.send_keys('Inizio :D')
            guess_form.submit()
            my_regexp = build_my_regexp(current_word)
            my_wordlist = {word for word in search_wordlist(my_regexp) if word not in attempted}
            for word in my_wordlist:
                win = try_and_guess(driver, word)
                if win:
                    break
                else:
                    current_word = driver.find_element_by_id('currentWord').text
                    attempted.add(word)
                    if current_word != old_word:
                        break
    return old_word



if __name__ == '__main__':
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()
    my_driver.get('https://skribbl.io/')

    input('Press enter when ready...')
    print('Started!')
    my_old_word = ''
    while True:
        try:
            my_word = my_driver.find_element_by_id('currentWord').text
            if '_' not in my_word:
                print('I think that it\'s not your turn now!')
            elif my_word != my_old_word:
                my_old_word = play_to_win(my_driver)
        except:
            print('Exception caught but kept running...')
        sleep(5)
