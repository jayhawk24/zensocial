from django.views.generic import TemplateView

#The index page is redirected to groups page to this line is useless.
class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = "test.html"

class ThanksPage(TemplateView):
    template_name = "thanks.html"

