# -*- coding: utf-8 -*-


class Message(object):
    REQUIRED_MESSAGE = u'Khung này không thể bỏ trống'
    REQUIRED = {'required': REQUIRED_MESSAGE}
    PASSWORD_NOT_MATCH = u"Mật khẩu không trùng nhau"
    PASSWORD_LENGTH_NOT_VALID = u"Độ dài mật khẩu từ 6 đến 20 kí tự"
    EMAIL_PASSWORD_NOT_MATCH = u"Sai email đăng nhập hoặc mật khẩu"
    BEGIN_DATE_END_DATE_NOT_VALID = u"Ngay ket thuc phai hon ngay ban dau"
    CREATE_TICKETS_HELP = u'Create all tickets for schedule.\nParameters is a array of schedule_id "schedule_id schedule_id ..."'
