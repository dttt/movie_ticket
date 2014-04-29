from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone

from .models import MovieTheater


class MovieTheaterTest(TestCase):
    """Contains all tests for movie theater model."""

    def test_add_MovieTheater(self):
        theater = MovieTheater()
        theater.name = 'Galaxy nguyen du'
        theater.address = 'nguyen du'
        theater.open_time = timezone.now().time()
        theater.close_time = timezone.now().time()
        theater.save()

        # Test number of theater change after save
        all_theater = MovieTheater.objects.all()
        self.assertEqual(len(all_theater), 1)
        first_theater = all_theater[0]
        self.assertEqual(first_theater, theater)

        #Test content in database and input.
        self.assertEqual(first_theater.name, theater.name)
        self.assertEqual(first_theater.address, theater.address)
        self.assertEqual(first_theater.open_time, theater.open_time)
        self.assertEqual(first_theater.close_time, theater.close_time)


class AdminTest(LiveServerTestCase):
    """Contains all test at admin page for facility app."""
    fixtures = ['users.json']

    def test_login(self):
        c = Client()
        response = c.get('/admin/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue('Log in' in response.content)

        c.login(username='dttt', password='totalwar')
        response = c.get('/admin/')
        self.assertTrue('Log out' in response.content)
