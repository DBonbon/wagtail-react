from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField

class Blog(Page):
    description = models.CharField(default="", max_length=200)
    published = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("published"),
    ]

    api_fields = [
        APIField("title"),
        APIField("description"),
        APIField("published"),
    ]