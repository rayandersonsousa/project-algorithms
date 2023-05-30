import pyteste
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Teste para a criptografia de chave par
    assert encrypt_message("luffy", 2) == "ffy_ul"

    # Teste para a criptografia de chave ímpar
    assert encrypt_message("luffy", 3) == "yff_ul"

    # Teste para a criptografia de chave inválida
    assert encrypt_message("luffy", 56) == "yfful"

    # Teste para a criptografia de chave inválida e string vazia
    assert encrypt_message("", 56) == ""

    # Teste para a criptografia com parametros incorretos
    with pyteste.raises(TypeError):
        encrypt_message(56, "luffy")