
class NoPhrasesLeftException(Exception):
    pass


class TalkingModule():

    def __init__(self):
        self._phrases = []

    def put_phrase(self, phrase):
        self._phrases.append(phrase)

    def get_phrase(self):
        if len(self._phrases) > 0:
            return self._phrases[(len(self._phrases) - 1)]
        else:
            raise NoPhrasesLeftException("There are no phrases left.")
