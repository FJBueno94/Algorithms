from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    invalid_key = "Hello"
    invalid_message = 2

    with pytest.raises(TypeError):
        encrypt_message(invalid_message, invalid_key)

# m no final da mensagem devido a palavra "Hello"
# ordenada de forma decrescente ser igual ao resultado esperado
    valid_message = "Hellom"
    valid_key_even = 2

    assert encrypt_message(valid_message, valid_key_even) == "moll_eH"

    valid_key_odd = 3

    assert encrypt_message(valid_message, valid_key_odd) == "leH_mol"

    bigger_key = 10

    assert encrypt_message(valid_message, bigger_key) == "molleH"

