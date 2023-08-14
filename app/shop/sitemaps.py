from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 1
    protocol = 'https'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)
