import logging

from django import http
from django.conf import settings
from django.template import RequestContext, loader
from django.contrib.sites.models import Site

log = logging.getLogger('perfect404')


def page_not_found(request, template_name='perfect404.html'):
    """
    Perfect 404 handler.

    Templates: `perfect404.html`
    Context:
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/')
    """
    referer = request.META.get('HTTP_REFERER', '')
    log.warning('missing %r, referer %r' % (request.path, referer))

    internal = False
    iam = 'http://%s' % Site.objects.get_current().domain
    if referer[:len(iam)] == iam:
        internal = True

    if settings.ADMINS:
        contact = dict(zip(('name', 'email'), settings.ADMINS[0]))
    else:
        contact = None

    t = loader.get_template(template_name)
    context = RequestContext(
        request, {
            'request': request,
            'request_path': request.path,
            'referer': referer,
            'internal': internal,
            'contact': contact,
        })
    content = t.render(context.flatten())
    return http.HttpResponseNotFound(content)
