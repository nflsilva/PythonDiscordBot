import unittest

from pythondiscordbot.talking.talking_module import \
    TalkingModule, \
    NoPhrasesLeftException, \
    PhraseNotFoundException, \
    PhreaseAlreadyExistsException


class TestTalkingModule(unittest.TestCase):

    def test_create_phrase(self):

        sut = TalkingModule()
        new_phrase = "This is a new test phrase"

        sut.put_phrase(new_phrase)
        stored_phrase = sut.get_phrase()

        self.assertEqual(new_phrase, stored_phrase)

    def test_create_duplicated(self):

        sut = TalkingModule()
        new_phrase = "This is a new phrase. Will be duplicated"

        sut.put_phrase(new_phrase)

        try:
            sut.put_phrase(new_phrase)
            self.fail(
                "Method did not throw Exception when there are duplicated phrases.")
        except PhreaseAlreadyExistsException:
            pass

    def test_get_phrase_error(self):

        sut = TalkingModule()

        try:
            sut.get_phrase()
            self.fail(
                "Method did not throw Exception when there are no phrases stored.")
        except NoPhrasesLeftException:
            pass

    def test_update_phrase(self):

        original_phrase = "Original"
        new_phrase = "Updated"
        sut = TalkingModule()

        sut.put_phrase(original_phrase)
        sut.update_phrase(0, new_phrase)
        updated_phrase = sut.get_phrase()

        self.assertEquals(new_phrase, updated_phrase)

    def test_update_phrase_error(self):

        impossible_ids = [-1, 1, 5.9]
        sut = TalkingModule()

        for id in impossible_ids:

            try:
                sut.update_phrase(id, "Updated")
            except PhraseNotFoundException:
                continue

            self.fail(f"Method did not throw Exception with invalid id {id}.")

    def test_delete_phrase(self):

        sut = TalkingModule()
        new_phrase = "This is a new test phrase"

        sut.put_phrase(new_phrase)
        sut.remove_phrase(0)

        self.assertEquals(sut.number_of_phrases(), 0)

    def test_delete_phrase_error(self):

        impossible_ids = [-1, 1, 5.9]
        sut = TalkingModule()

        for id in impossible_ids:
            try:
                sut.remove_phrase(id)
            except PhraseNotFoundException:
                continue

            self.fail(f"Method did not throw Exception with invalid id {id}.")
