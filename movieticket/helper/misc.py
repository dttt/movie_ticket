# -*- coding: utf-8 -*-


class Message(object):

    REQUIRED_MESSAGE = 'Khung này không thể bỏ trống'
    REQUIRED = {'required': REQUIRED_MESSAGE}
    PASSWORD_NOT_MATCH = "Mật khẩu không trùng nhau"
    PASSWORD_LENGTH_NOT_VALID = "Độ dài mật khẩu từ 6 đến 20 kí tự"
    EMAIL_PASSWORD_NOT_MATCH = "Email and password is not match"
    BEGIN_DATE_END_DATE_NOT_VALID = "Ngay ket thuc phai hon ngay ban dau"


def get_loop_time(lists):
    times = [0]
    i = 0
    for item in lists:
        times.append(i + 1)
    return times
