from django.db import models


class Job(models.Model):
    NEW = 'NEW'
    APPLIED = 'APP'
    INTERVIEWING = 'INT'
    AWAITING_DECISION = 'AWD'
    NEGOTIATING_OFFER = 'NGO'
    ACCEPTED_OFFER = 'ACP'
    DECLINED_OFFER = 'DCL'
    STOPPED_PURSUING = 'STP'
    REJECTED = 'REJ'

    company = models.ForeignKey('contacts.Company', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=3, choices=[
        (NEW, 'New Opportunity'),
        (APPLIED, 'Application Submitted'),
        (INTERVIEWING, 'Interviewing'),
        (AWAITING_DECISION, 'Awaiting Decision')
    ], null=False, blank=False, default=NEW)

    @property
    def is_being_pursued(self):
        return self.status not in (
            self.ACCEPTED_OFFER,
            self.DECLINED_OFFER,
            self.STOPPED_PURSUING,
            self.REJECTED,
        )

    def __str__(self):
        title = self.title
        company = self.company
        return f'{title} @ {company}'
