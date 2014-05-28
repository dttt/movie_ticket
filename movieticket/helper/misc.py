# -*- coding: utf-8 -*-


class Message(object):

    REQUIRED_MESSAGE = 'Khung này không thể bỏ trống'
    REQUIRED = {'required': REQUIRED_MESSAGE}
    PASSWORD_NOT_MATCH = "Mật khẩu không trùng nhau"
    PASSWORD_LENGTH_NOT_VALID = "Độ dài mật khẩu từ 6 đến 20 kí tự"
    EMAIL_PASSWORD_NOT_MATCH = "Email and password is not match"
    BEGIN_DATE_END_DATE_NOT_VALID = "Ngay ket thuc phai hon ngay ban dau"
    CREATE_TICKETS_HELP = 'Tao tat ca ve cho mot lan chieu.\nTham so truyen vao co dang "schedule_id schedule_id ..."'
