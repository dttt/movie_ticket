from django.utils import timezone

from movie.models import Version
from ticket.models import Schedule

from collections import defaultdict


class MovieHelper(object):

    now = timezone.now()

    def get_current(self, offset=None, limit=None):
        movies = Version.objects.filter(
            begin_date__lte=self.now,
            end_date__gte=self.now
        ).order_by('begin_date')[offset:limit]
        return movies

    def get_future(self, offset=None, limit=None):
        movies = Version.objects.filter(
            begin_date__gt=self.now,
        ).order_by('begin_date')[offset:limit]
        return movies


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

        print result
        return result

    def get_schedules_by_theater(self, movie=None, theater=None):
        schedules = Schedule.objects.filter(
            movie=movie,
            room__theater=theater,
        ).distinct('date')
        result = []
        for schedule in schedules:
            temp = {}
            temp['date'] = schedule.date
            temp['schedules'] = Schedule.objects.filter(
                movie=movie,
                room__theater=theater,
                date=schedule.date,
            )
            result.append(temp)
        return result
