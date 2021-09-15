from unittest import TestCase

from textalytics_core.resources import TextInput

from tests.test_config import SAMPLE_TEXT
from textalytics_stanza.stanza_entity_recognition import StanzaEntityRecognizer


class TestStanzaEntityRecognizer(TestCase):
    def test_stanza_recognize_entities(self):
        text_inupt = TextInput(source_text = SAMPLE_TEXT)
        entity_recognizer = StanzaEntityRecognizer()
        entities = entity_recognizer.recognize_entities(text_inupt)
        assert entities
        assert len(entities.entities) > 0
        print(entities.entities)
