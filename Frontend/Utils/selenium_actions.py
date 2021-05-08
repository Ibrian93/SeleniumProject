import time


def slow_type(element, text, delay=0.1):
    for character in text:
        element.send_keys(character)
        time.sleep(delay)

