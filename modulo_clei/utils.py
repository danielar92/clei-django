from .models import CLEI
class CLEIMixin(object):
    clei = None
    def get_clei(self):
        if self.clei is None:
            clei_pk = self.kwargs.get('pk')
            self.clei = CLEI.objects.get(pk=clei_pk)
        return self.clei

    def get_context_data(self, **kwargs):
        context = super(CLEIMixin, self).get_context_data(**kwargs)
        context['clei'] = self.get_clei()
        return context

