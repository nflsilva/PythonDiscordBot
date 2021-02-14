import random


class NoPhrasesLeftException(Exception):
    pass


class PhraseNotFoundException(Exception):
    pass


class PhreaseAlreadyExistsException(Exception):
    pass


class TalkingModule():

    def __init__(self):
        self._phrases = []

    def _validateId(self, phrase_id):
        if phrase_id < 0 or phrase_id > len(self._phrases) - 1:
            raise PhraseNotFoundException(
                f"There are no phrases with id: {phrase_id}")

    def number_of_phrases(self):
        return len(self._phrases)

    def put_phrase(self, phrase):

        if phrase in self._phrases:
            raise PhreaseAlreadyExistsException

        self._phrases.append(phrase)

    def get_phrase(self):
        if len(self._phrases) > 0:
            phrase_index = random.randint(0, len(self._phrases)-1)
            return self._phrases[phrase_index]
        else:
            raise NoPhrasesLeftException("There are no phrases left.")

    def update_phrase(self, phrase_id, new_phrase):
        self._validateId(phrase_id)
        self._phrases[phrase_id] = new_phrase

    def remove_phrase(self, phrase_id):
        self._validateId(phrase_id)
        self._phrases.pop(phrase_id)
