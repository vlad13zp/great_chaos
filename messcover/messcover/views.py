from django.views.generic.base import TemplateView
from messcover import actions
from messcover import tasks


class TreeView(TemplateView):
    template_name = 'tree.html'

    def get_context_data(self, **kwargs):
        context = super(TreeView, self).get_context_data(**kwargs)

        context['main_urls'] = actions.get_main_urls()
        context['help_urls'] = actions.get_help_urls()

        return context


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        actions.clear_base()
        return context


class CrawlView(TemplateView):
    template_name = 'crawl.html'

    def get_context_data(self, **kwargs):
        context = super(CrawlView, self).get_context_data(**kwargs)

        # actions.run_spider()
        tasks.run_spider()
        return context
