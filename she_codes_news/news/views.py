from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import NewsStory
from users.models import CustomUser
from .forms import StoryForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Add view for editing/updating a news story
class UpdateStoryView(UpdateView):
    form_class = StoryForm
    model = NewsStory
    template_name = 'news/updateStory.html'
    success_url = reverse_lazy('news:index')

# Add view for deleting a news story
class DeleteStoryView(DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

class searchAuthor(generic.ListView):
    template_name = 'news/authorSearch.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        query = self.request.GET.get("author")
        context = super().get_context_data(**kwargs)
        context['author_list'] = CustomUser.objects.all().order_by('username')
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        context['author_stories'] = NewsStory.objects.filter(author__username=query).order_by('-pub_date')
        return context
