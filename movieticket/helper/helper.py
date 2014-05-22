from django.utils import timezone

from movie.models import Version


class MovieHelper(object):

    def get_current(self):
        now = timezone.now()
        movies = Version.objects.filter(
            begin_date__lte=now,
            end_date__gte=now
        ).order_by('begin_date')[:5]
        return movies
