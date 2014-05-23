from collections import defaultdict

from django.utils import timezone

from movie.models import Version
from ticket.models import Schedule


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

    def get_schedule(self, movie=None, date=None, theater=None):
        if movie:
            schedules = Schedule.objects.get(
                movie=movie
            )

        sorted_schedules = defaultdict(list)
        for schedule in schedules:
            sorted_schedules[schedule.date].append(schedule)

        result = sorted_schedules.values()

        return result
