from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.search import index
from wagtail.admin.panels import (
    FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel)
from publications.models import Publication

# Wagtail models
class CiteIndexPage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    intro = RichTextField(blank=True)
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    def get_context(self, request):
        citekeys = []
        publications = Publication.objects.all().order_by('citekey', '-year', '-month', '-id')

        for publication in publications:
            if publication.type.hidden:
                continue
            else:
                citekeys.append((publication.citekey, []))
            citekeys[-1][1].append(publication)

        # Update template context
        context = super(CiteIndexPage, self).get_context(request)
        context['citekeys'] = citekeys
        return context


CiteIndexPage.content_panels = Page.content_panels + [
    FieldPanel('subtitle'),
    FieldPanel('intro'),
]
