import re
"""
def email_validation_check():
    pass
"""

def password_validation_check(pwd):
    """
    checking pasword validataion
    :param pwd: password string
    :return: True or False (boolean) : the result of checking validation
    """s
    if len(pwd) < 6 or len(pwd) > 12:
        print(pwd, '의 길이가 적당하지 않습니다')
        return False

    if re.findall('[a-zA-Z0-9]+', pwd)[0] != pwd:
        print(pwd, '는 숫자와 문자로만 구성되어야 합니다')
        return False

    if len(re.findall('[a-z]', pwd)) == 0 or len(re.findall('[A-Z]',pwd)) == 0:
        print(pwd,'는 영문 대소문자가 함께 존재하지 않습니다.')
        return False

    print(pwd, '는 비밀번호로 적당합니다')
    return True

if __name__ == "__main__":
    password_validation_check('23jke')
    password_validation_check('53weff76')
    password_validation_check('20@ke%')
    password_validation_check('3k45O45')