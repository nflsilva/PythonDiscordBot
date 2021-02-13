import unittest

from pythondiscordbot.talking.talking_module import TalkingModule, NoPhrasesLeftException


class TestTalkingModule(unittest.TestCase):

    def test_create_phrase(self):

        sut = TalkingModule()
        new_phrase = "This is a new test phrase"

        sut.put_phrase(new_phrase)
        stored_phrase = sut.get_phrase()

        self.assertEqual(new_phrase, stored_phrase)

    def test_get_phrase_error(self):

        sut = TalkingModule()

        try:
            sut.get_phrase()
            self.fail()
        except NoPhrasesLeftException:
            pass
