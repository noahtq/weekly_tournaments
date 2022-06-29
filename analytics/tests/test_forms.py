from django.test import TestCase
from django.utils import timezone
from django.conf import settings
from analytics.forms import BugReportForm
from datetime import timedelta


class BugReportFormTest(TestCase):
    def testBugUrlLabel(self):
        form = BugReportForm()
        label = form.fields['bug_url'].label
        expected = 'URL of page where bug occured'
        self.assertEqual(label, expected)

    def testDescriptionLabel(self):
        form = BugReportForm()
        label = form.fields['description'].label
        expected = 'Describe what went wrong'
        self.assertEqual(label, expected)

    def testInstructionsLabel(self):
        form = BugReportForm()
        label = form.fields['instructions'].label
        expected = 'Explain how to recreate the error (what were you doing before the error occured)'
        self.assertEqual(label, expected)

    def testOccuredLabel(self):
        form = BugReportForm()
        label = form.fields['occured'].label
        expected = 'Time and date of error'
        self.assertEqual(label, expected)

    def testOccuredInFuture(self):
        bug_url = f'http://{settings.ALLOWED_HOSTS[0]}.com'
        current_time = timezone.now()
        time_in_future = current_time + timedelta(minutes=1)
        form = BugReportForm(data={'bug_url': bug_url, 'occured': time_in_future})
        self.assertFalse(form.is_valid())

    def testOccuredInPast(self):
        bug_url = f'http://{settings.ALLOWED_HOSTS[0]}.com'
        current_time = timezone.now()
        time_in_past = current_time - timedelta(minutes=1)
        form = BugReportForm(data={'bug_url': bug_url, 'occured': time_in_past})
        self.assertTrue(form.is_valid())

    def testWrongUrlBase(self):
        test_url = 'https://www.apple.com/iphone/'
        test_datetime = timezone.now() - timedelta(minutes=1)
        form = BugReportForm(data={'bug_url': test_url, 'occured': test_datetime})
        self.assertFalse(form.is_valid())

    def testCorrectUrlBase(self):
        test_url = f'https://{settings.ALLOWED_HOSTS[0]}.com/event/3/'
        test_datetime = timezone.now() - timedelta(minutes=1)
        form = BugReportForm(data={'bug_url': test_url, 'occured': test_datetime})
        self.assertTrue(form.is_valid())