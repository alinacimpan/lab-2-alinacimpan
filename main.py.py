def is_antipalindrome(n):
    """
    Determina daca un numar n este antipalindrom
    :param n: nr. intreg
    :return: True daca n este antipalindrom si False in caz contrar
    """
    # Un numar negativ nu este niciodata palindrom
    if n < 0:
        return True
    antipalindrom = True
    cn = n
    nr_cifre = 0
    # Determinam cate cifre are numarul citit
    while cn != 0:
        nr_cifre += 1
        cn = cn // 10
    # Determinam daca numarul citit este antipalindrom
    while n > 9:
        if n // (10 ** (nr_cifre - 1)) == n % 10:
            antipalindrom = False
        n = n % (10 ** (nr_cifre - 1))
        n = n // 10
        nr_cifre -= 2
    return antipalindrom


def test_is_antipalindrome():
    assert is_antipalindrome(-1) is True
    assert is_antipalindrome(2773) is False
    assert is_antipalindrome(2783) is True
if __name__ == '__main__':
    main()