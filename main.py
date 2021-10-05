def is_palindrome(n):
    '''
    :param n: nr intreg
    :param copie: retinem nr n
    :return: true daca este palindrom , false in caz contrar
    '''
    copie=n
    inv=0
    while copie!=0:
        inv=inv*10+copie%10
        copie=copie//10

    if inv==n:
        return True
    else:
        return False

    def test_is_palindrome():
'''
    :return: Fucntia de testare ruleaza corespunzator
    '''
    assert is_palindrome(636) == True
    assert is_palindrome(78) == False
    assert is_palindrome(9892) == False
    assert is_palindrome(8998) == True
    assert is_palindrome(22222) == True


def is_superprime(n):
    '''
	:param n: nr. intreg
	:return:True daca n e nr. superprim si False in caz contrar
    '''
    if n < 2:
        return False
    else:
        while n != 0:
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    return False
            n = n//10
    return True
def test_is_superprime():
    '''
    testeaza daca functia is_superprime functioneaza
    :return: true daca nr. e superprim, false in caz contrar
    '''
    assert is_superprime(233) is True
    assert is_superprime(237) is False
    assert is_superprime(1) is False
