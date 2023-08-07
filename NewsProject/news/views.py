

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import NewsForm
from .models import News
from .filters import  NewNewsFilter #NewsFilter

class NewsList(ListView):
    model = News
    ordering = 'publish_date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 5

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = NewsFilter(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context
class NewsDetail(DetailView):
    model = News
    template_name = 'news_single.html'
    context_object_name = 'news_single'

# def create_news(request):
#     form = NewsForm()
#
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/news/')
#
#     return render(request, 'news_edit.html', {'form': form})

class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'news_single_edit.html'

class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'

class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class NewsSearch(ListView):
    model = News
    ordering = 'publish_date'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewNewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

