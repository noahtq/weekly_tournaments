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
        report_data = {
            'bug_url':f'http://{settings.ALLOWED_HOSTS[0]}.com',
            'description': '',
            'instructions': '',
            'occured': timezone.now()
        }
        report_form = BugReportForm(data={
            'bug_url':f'http://{settings.ALLOWED_HOSTS[0]}.com',
            'description': '',
            'instructions': '',
            'occured': timezone.now()
        })
        response = self.client.post(reverse('analytics-bug-report'), {'bug_url': report_data['bug_url'], 'occured': report_data['occured']})
        self.assertRedirects(response, reverse('events-home'))

        