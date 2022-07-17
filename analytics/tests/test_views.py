from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from analytics.forms import BugReportForm
from django.utils import timezone
from datetime import timedelta


class SubmitReportViewTest(TestCase):

    def testViewUrlExists(self):
        response = self.client.get('/bug-report/')
        self.assertEquals(response.status_code, 200)

    def testViewUrlAccessibleByName(self):
        response = self.client.get((reverse('analytics-bug-report')))
        self.assertEquals(response.status_code, 200)

    def testViewUsesCorrectTemplate(self):
        response = self.client.get((reverse('analytics-bug-report')))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'analytics/bug_report.html')

    def testViewRedirectsOnSuccess(self):

        data = {
        'bug_url': f'http://{settings.ALLOWED_HOSTS[0]}.com',
        'description': '',
        'instructions': '',
        'occured': timezone.now()
        }

        post_dict = {'csrfmiddlewaretoken': ['vrw8rX5253dSN19SCO78G8GNlhBIpHt3ZVCChchZW09pNfTf8y0hudRxcj0IY9Vo'], 'bug_url': ['http://localhost:8000/'], 'description': ['adasda'], 'instructions': ['asdada'], 'occured': ['2022-06-29 22:52:51'], 'initial-occured': ['2022-06-29 22:52:51']}
        response = self.client.post(
            reverse('analytics-bug-report'),
            data
        )
        response = reverse('events-home')
        self.assertRedirects(response, reverse('events-home'))

        