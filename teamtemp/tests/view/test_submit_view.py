from django.core.urlresolvers import reverse
from django.test import TestCase

from teamtemp.tests.factories import TeamTemperatureFactory, TeamFactory


class SubmitViewTestCases(TestCase):
    def setUp(self):
        self.teamtemp = TeamTemperatureFactory()
        self.team = TeamFactory(request=self.teamtemp)

    def test_submit_response_view(self):
        response = self.client.get(reverse('submit', kwargs={'survey_id': self.teamtemp.id, 'team_name': self.team.team_name}))
        self.assertTemplateUsed(response, 'form.html')
        self.assertEqual(response.status_code, 200)
