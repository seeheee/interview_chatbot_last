from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from .models import Article
from django.http import HttpResponseRedirect
from django.contrib import messages

def deleteContent(request):
    delData = Article.objects.get(pk=request.GET.get("pk"))
    delData.delete()
    return HttpResponseRedirect("/article/")

class ArticleListView(TemplateView):
    template_name = 'article_list.html'

    def get(self, request, *args, **kwargs):
        print(request.GET)
        queryset = Article.objects.all()
        ctx = {
            'articles': queryset
        }
        return self.render_to_response(ctx)

class ArticleDetailView(TemplateView):
    template_name = 'article_detail.html'
    queryset = Article.objects.all()
    pk_url_kwargs = 'article_id'

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        article = queryset.filter(pk=pk).first()

        if not article:
            raise Http404('invalid pk')
        return article

    def get(self, request, *args, **kwargs):
        article = self.get_object()

        ctx = {
            'article': article
        }
        return self.render_to_response(ctx)


class ArticleCreateUpdateView(TemplateView):
    template_name = 'article_update.html'
    queryset = Article.objects.all()
    pk_url_kwargs = 'article_id'

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        article = queryset.filter(pk=pk).first()

        if pk and not article:
            raise Http404('invalid pk')
        return article

    def get(self, request, *args, **kwargs):
        article = self.get_object()

        ctx = {
            'article': article,
        }
        return self.render_to_response(ctx)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        post_data = {key: request.POST.get(key) for key in ('title', 'content', 'author')}
        for key in post_data:
            if not post_data[key]:
                messages.error(self.request, '{} 값이 존재하지 않습니다.'.format(key), extra_tags='danger')

        if len(messages.get_messages(request)) == 0:
            if action == 'create':
                article = Article.objects.create(**post_data)
                messages.success(self.request, '게시글이 저장되었습니다.')
            elif action == 'update':
                article = self.get_object()
                for key, value in post_data.items():
                    setattr(article, key, value)
                article.save()
                messages.success(self.request, '게시글이 수정되었습니다.')
            else:
                messages.error(self.request, '알 수 없는 요청입니다.', extra_tags='danger')

            return HttpResponseRedirect('/article/') # 정상적인 저장이 완료되면 '/articles/'로 이동됨

        ctx = {
            'article': self.get_object() if action == 'update' else None
        }
        return self.render_to_response(ctx)


class ArticleDeleteView(TemplateView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()
    pk_url_kwargs = 'article_id'

    def remove(self, request, pk):
        article = self.get_object(pk=pk)
        if request.method == 'POST':
            article.delete()
            messages.success(self.request, '게시글이 삭제되었습니다.')
            return HttpResponseRedirect('/article/')
        else:
            messages.error(self.request, '알 수 없는 요청입니다.', extra_tags='danger')

        return HttpResponseRedirect('/article/')  # 정상적인 저장이 완료되면 '/articles/'로 이동됨
