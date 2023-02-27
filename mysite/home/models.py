from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1 #"""No child page for homepage."""
    banner_title = models.CharField(max_length=100, blank=False, null=True, default="Title not added")
    banner_subtitle = RichTextField(features=["bold", "italic"], default="SubTitle not added")
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+")
    """Not using any related name, just using field name"""
    banner_cta = models.ForeignKey("wagtailcore.Page", null=True, blank=False, on_delete=models.SET_NULL, related_name="+")
    """Not using any related name, just using field name"""
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image"),
        PageChooserPanel("banner_cta")]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
