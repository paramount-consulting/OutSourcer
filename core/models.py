from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class PaymentTypes(models.Model):
    """
    Types of payments that a company can require. Eg. Hourly, Monthly etc.
    """
    type_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.type_name


class Currency(models.Model):
    """
    Types of available currencies
    """
    currency_name = models.CharField(max_length=200)
    currency_short_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.currency_short_name


class TimeUnit(models.Model):
    """
    Units of measure for projects duration. Eg. Weeks, Months, Years
    """
    unit_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.unit_name


class Country(models.Model):
    """
    A set of available countries for company location
    """
    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=200)

    def __unicode__(self):
        return self.country_name


class Category(models.Model):
    """
    Categories are the mean by which we differentiate projects by their economical areas.
    """
    category_name = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.category_name


class Company(models.Model):
    """
    Defines the structure of a Company entity in Outsourcer
    """
    company_name = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=200, null=True, blank=True)
    employees_no = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    country = models.ForeignKey(Country, null=True, blank=True)
    county = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    slug_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    external_link = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.company_name


class Project(models.Model):
    """
    Defines the structure of a Project entity in Outsourcer
    """
    project_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    by_company = models.ForeignKey(Company, null=True, blank=True, related_name='published_by')
    approximate_duration = models.CharField(max_length=200, null=True, blank=True)
    approximate_duration_time_unit = models.ForeignKey(TimeUnit, null=True, blank=True)
    description = models.TextField()
    work_description = models.TextField(default='')
    slug_name = models.CharField(max_length=200, null=True)
    required_techs = models.TextField(null=True)
    approximate_hours_per_week = models.IntegerField(default=0)
    payment_type = models.ForeignKey(PaymentTypes, null=True, blank=True)
    payment_amount = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, null=True)
    min_ppl_required = models.IntegerField(null=True, default=0)
    category = models.ForeignKey(Category, null=True)

    def save(self, *args, **kwargs):
        try:
            r = settings.REDIS_INIT
            r.delete(':1:drfc_default_Project_' + str(self.id))
        except Exception:
            pass
        super(Project, self).save(*args, **kwargs)

    def delete(self):
        try:
            r = settings.REDIS_INIT
            r.delete(':1:drfc_default_Project_' + str(self.id))
        except Exception:
            pass
        super(Project, self).delete()

    def __unicode__(self):
        return self.project_name


class Bid(models.Model):
    """
    Bids are the mean by which a company makes an fee offer to take a project
    """
    payment_type = models.ForeignKey(PaymentTypes, null=True, blank=True)
    payment_amount = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, null=True)
    project = models.ForeignKey(Project, null=True, related_name='bid_on')
    by_company = models.ForeignKey(Company, null=True, related_name='bid_by')

    def __unicode__(self):
        return self.by_company


class Comment(models.Model):
    """
    Companies can post comments to other companies' projects
    """
    on_project = models.ForeignKey(Project, null=True, related_name='comment_on')
    comment = models.TextField(null=True)
    by_company = models.ForeignKey(Company, null=True, related_name='comment_by')

    def __unicode__(self):
        return self.by_company


class Recommendation(models.Model):
    """
    Recommendations can be mutually granted between companies
    """
    by_company = models.ForeignKey(Company, null=True, related_name='by_company')
    for_company = models.ForeignKey(Company, null=True, related_name='for_company')

    def __unicode__(self):
        return self.by_company

