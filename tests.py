import pytest
from functions import base64_encoder, verman_cipher, ru_vigenere_cipher, ru_caesars_cipher, eng_caesars_cipher, eng_vigenere_cipher

@pytest.mark.parametrize("text, key, mode, result", [
    ("Пиво", 0, True, "Пиво"),
    ("Пиво", 3, True, "Тлес"),
    ("Пиво", -3, True, "Мёял"),
    ("Alban", -3, True, "Alban"),
    ("Пиво", 0, False, "Пиво"),
    ("Тлес", 3, False, "Пиво"),
    ("Мёял", -3, False, "Пиво"),
    ("Alban", -3, False, "Alban")
])
def test_caesar_ru(text, key, mode, result):
    assert ru_caesars_cipher(text, key, mode) == result
    
@pytest.mark.parametrize("text, key, mode, result", [
    ("Beer", 0, True, "Beer"),
    ("Beerz", 3, True, "Ehhuc"),
    ("Beer", -3, True, "Ybbo"),
    ("Пиво", -3, True, "Пиво"),
    ("Beer", 0, False, "Beer"),
    ("Beer", 3, False, "Ybbo"),
    ("Beerz", -3, False, "Ehhuc"),
    ("Пиво", -3, False, "Пиво")
])
def test_caesar_eng(text, key, mode, result):
    assert eng_caesars_cipher(text, key, mode) == result
    

@pytest.mark.parametrize("text, mode, result", [
    ("вавымфс", True, "Это не Base64"),
    ("Beer", True, "QmVlcg=="),
    ("", True, ""),
    ("0LLQsNCy0YvQvNGE0YE=", False, "Это не Base64"),
    ("QmVlcg==", False, "Beer"),
    ("", False, "")
])
def test_base64(text, mode, result):
    assert base64_encoder(text, mode) == result
    
@pytest.mark.parametrize("text, key, mode, result", [
    ("Пиво", "Балаган", True, "Рино"),
    ("Пиво", "", True, ""),
    ("Рино", "Балаган", False, "Пиво")
])
def test_vigenere_ru(text, key, mode, result):
    assert ru_vigenere_cipher(text, key, mode) == result


@pytest.mark.parametrize("text, key, mode, result", [
    ("Beer", "cryptii", True, "Jvcg"),
    ("Beer", "", True, ""),
    ("Jvcg", "cryptii", False, "Beer")
])
def test_vigenere_eng(text, key, mode, result):
    assert eng_vigenere_cipher(text, key, mode) == result
