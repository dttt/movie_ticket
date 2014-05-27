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


class ScheduleHelper(object):

    def get_sorted_schedules(self, movie=None):
        result = []

        schedules = Schedule.objects.filter(movie=movie).distinct('room__theater')

        for schedule in schedules:
            theater = schedule.room.theater
            temp = {}

            temp['theater'] = theater
            temp['schedules'] = self.get_schedules_by_theater(
                movie=movie, theater=theater)

            result.append(temp)

        return result

    def get_schedules_by_theater(self, movie=None, theater=None):
        schedules = Schedule.objects.filter(
            movie=movie,
            room__theater=theater,
        )
        for schedule in schedules:
            temp = {}
            temp['date'] = schedule.date
            temp['schedules'] = Schedule.objects.filter(
                movie=movie,
                room__theater=theater,
                date=schedule.date,
            )
        return temp