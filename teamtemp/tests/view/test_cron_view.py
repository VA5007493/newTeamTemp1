from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from teamtemp.tests.factories import WordCloudImageFactory, TemperatureResponseFactory


class CronViewTestCases(TestCase):
    def test_cron_view_default_pin(self):
        url = reverse('cron', kwargs={'pin': '0000'})

        wordcloud = WordCloudImageFactory()

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cron_view_long_pin(self):
        settings.CRON_PIN = '1234567812345678'
        url = reverse('cron', kwargs={'pin': '1234567812345678'})

        response = TemperatureResponseFactory(request__archive_schedule=7)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cron_view_wrong_pin(self):
        url = reverse('cron', kwargs={'pin': '6666'})

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
