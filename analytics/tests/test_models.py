from datetime import datetime
from django.test import TestCase
from analytics.models import BugReport
from django.utils import timezone
from datetime import timedelta


class BugReportTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        BugReport.objects.create(
            bug_url='http://localhost:8000/event/3/',
            description='', 
            instructions=''
        )

        BugReport.objects.create(
            bug_url='',
            description='', 
            instructions=''
        )

    def testBugUrlMaxLength(self):
        report = BugReport.objects.get(id=1)
        max_length = 200
        report_max_length = report._meta.get_field('bug_url').max_length
        self.assertEqual(report_max_length, max_length)

    def testBugUrlBlankOk(self):
        report = BugReport.objects.get(id=2)
        bug_url = report.bug_url
        expected = ''
        self.assertEqual(bug_url, expected)

    def testDescriptionBlankOk(self):
        report = BugReport.objects.get(id=1)
        description = report.description
        expected = ''
        self.assertEqual(description, expected)

    def testInstructionsBlankOk(self):
        report = BugReport.objects.get(id=1)
        instructions = report.instructions
        expected = ''
        self.assertEqual(instructions, expected)

    def testDefaultOccuredTime(self):
        report = BugReport.objects.get(id=1)
        expected = timezone.now()
        occured = report.occured
        #Checking that object was instantiated with current time, current time - object time
        deltatime = expected - occured
        #Margin for error as naturally the current time and the instantiated time
        #are going to be a little different because of the processing time
        max_allowed_microseconds = 100000
        time_over = timedelta(microseconds=max_allowed_microseconds)
        self.assertTrue(deltatime <= time_over)

    def testDefaultResolved(self):
        report = BugReport.objects.get(id=1)
        resolved = report.resolved
        self.assertFalse(resolved)

