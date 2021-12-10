# skribbl-io-guesser
A simple selenium automation written in python 3.8 to win at [skribbl.io](https://skribbl.io/) games.
I wrote this simple script to show to my ex-girlfriend's little sister, a passionate _skribbl.io_
player, how funny can programming actually be.

### Supported languages:
 - [x] English
 - [x] German

Could support any language if you create or scrape a specific wordlist for the lang that you want
and add 2 lines of code in guesser.py source to make it selectable via arguments.

### Requirements:
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver)

### Setup instructions:
```
git clone https://github.com/4n4nk3/scribbl-io-guesser.git
cd scribbl-io-guesser
pip install -r requirements.txt
```

### How to use:
```
python guesser.py --lang English
```
- A new Google Chrome window will open.
- Use that window to join a game of _skribbl.io_.
- When inside the lobby select the terminal in which the script is running and press enter.
- Wait for skribbl-io-guesser to win for you!

### Help:
```
usage: guesser.py [-h] --lang LANG

A simple selenium automation written in python to win at https://skribbl.io game.

optional arguments:
  -h, --help   show this help message and exit

required arguments:
  --lang LANG  Select desired language (eng, ger)

```
