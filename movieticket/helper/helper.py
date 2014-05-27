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

    def get_schedule(self, movie=None):
        sorted_schedules = []
        if movie:
            schedules = Schedule.objects.filter(
                movie=movie.movie
            )
        if schedules:
            for schedule in schedules:
                sorted_schedules.append(
                    {schedule.room.theater: {schedule.date: {schedule}}})

            d = defaultdict(list)
            for k, v in sorted_schedules:
                d[k].append(v)
            d.items()
            print d
            return sorted_schedules

        return None
