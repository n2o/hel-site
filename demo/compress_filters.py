from django.conf import settings
from compressor.filters.css_default import CssAbsoluteFilter
from compressor.utils import staticfiles

class CustomCssAbsoluteFilter(CssAbsoluteFilter):
    def __init__(self, *args, **kwargs):
        super(CustomCssAbsoluteFilter, self).__init__(*args, **kwargs)
        self.url = '%s%s' % (settings.FULL_DOMAIN, settings.STATIC_URL)
        self.url_path = self.url

    def find(self, basename):
        # The line below is the original line.  I removed settings.DEBUG.
        # if settings.DEBUG and basename and staticfiles.finders:
        if basename and staticfiles.finders:
            return staticfiles.finders.find(basename)
