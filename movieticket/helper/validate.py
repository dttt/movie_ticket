# -*- coding: utf-8 -*-


class Message(object):

    REQUIRED_MESSAGE = 'Khung này không thể bỏ trống'
    REQUIRED = {'required': REQUIRED_MESSAGE}
    PASSWORD_NOT_MATCH = "Mật khẩu không trùng nhau"
    PASSWORD_LENGTH_NOT_VALID = "Độ dài mật khẩu từ 6 đến 20 kí tự"