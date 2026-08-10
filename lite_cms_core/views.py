"""Django Lite CMS Views."""

from django.apps import apps
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def search(request, template="lite_cms_core/search_results.html", extra_context=None):
    """
    Display search results.

    Takes an optional "contenttype" GET parameter in the form "app-name.ModelName"
    to limit search results to a single model.
    """
    query = request.GET.get("q", "")
    try:
        parts = request.GET.get("type", "").split(".", 1)
        search_model = apps.get_model(*parts)
        # pylint: disable=pointless-statement
        search_model.objects.search  # noqa: B018
        results = search_model.objects.search(query, for_user=request.user)
    except (ValueError, TypeError, LookupError, AttributeError):
        search_types = settings.SEARCH_MODEL_CHOICES
        results = []
        for search_type in search_types:
            parts = search_type.split(".", 1)
            if len(parts) != 2:
                continue  # pragma: no cover
            app_label, model_name = parts
            try:
                search_model = apps.get_model(app_label, model_name)
            except LookupError:  # pragma: no cover
                continue  # pragma: no cover
            results += search_model.objects.search(query, for_user=request.user)
        search_type = _("Everything")
    else:
        search_type = search_model._meta.verbose_name_plural.capitalize()
        results = search_model.objects.search(query, for_user=request.user)

    paginator = Paginator(results, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {"query": query, "results": page_obj,
               "search_type": search_type, "total": len(results)}
    context.update(extra_context or {})
    return render(request, template, context)


def ext_search_form(request):
    """
    Extended search form.

    The extended search form lets users select a model to search on.
    """
    search_choices = set()
    for name in settings.SEARCH_MODEL_CHOICES:
        parts = name.split(".", 1)
        if len(parts) != 2:
            continue  # pragma: no cover
        app_label, model_name = parts
        try:
            model = apps.get_model(app_label, model_name)
        except LookupError:  # pragma: no cover
            continue  # pragma: no cover
        search_choices.add((model._meta.verbose_name.title(), name))
    return render(
        request,
        "lite_cms_core/ext_search_form.html",
        {
            "search_model_choices": search_choices,
        },
    )
