# Create your views here.


from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import SearchForm

from wiki.models import Article
from pybb.models import Post, Topic
from news.models import Post as NewsPost

class DummyEmptyQueryset(object):
    """
    A simple dummy class when a search
    should not be run. The template expects
    a queryset and checks for the count member.
    """
    def count(self):
        return 0

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
         
        if form.is_valid():
            query = form.cleaned_data["search"]
            do_wiki = form.cleaned_data["incl_wiki"]
            do_forum = form.cleaned_data["incl_forum"]
            do_news = form.cleaned_data["incl_news"]
            
            wiki_results = Article.search.query(query) if do_wiki else DummyEmptyQueryset()
            forum_results_topic = Topic.search.query(query) if do_forum else DummyEmptyQueryset()
            forum_results_post = Post.search.query(query) if do_forum else DummyEmptyQueryset()
            news_results = NewsPost.search.query(query) if do_news else DummyEmptyQueryset()
    
            template_params = {
                "wiki_results": wiki_results,
                "forum_hits": forum_results_post.count() + forum_results_topic.count(),
                "forum_results_topic": forum_results_topic,
                "forum_results_post": forum_results_post,
                "news_results": news_results,
                "search_form": form,
                "post": True,
            }

            return render_to_response("wlsearch/search.html",
                       template_params,
                       context_instance=RequestContext(request))
    else:
        form = SearchForm()

    template_params = {
        "search_form": form,
        "post": False,
    }
    return render_to_response("wlsearch/search.html",
                              template_params,
                              context_instance=RequestContext(request))

