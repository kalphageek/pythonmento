import re

def email_validation_check(email):
    if re.findall(r'[\w.-]+@[\w.-]+.\w+', email)[0] != email:
        print(email, '는 이메일 형식에 맞지 않습니다.')
        return False

    print(email, '는 이메일 형식으로 적당합니다.')
    return True

if __name__ == '__main__':
    email_validation_check('#ddf#q@gmail*cm')
    email_validation_check('jindeok.jeong@sk.com')