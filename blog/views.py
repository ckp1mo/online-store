from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import BlogRecordForm
from blog.models import BlogRecord


class BlogRecordCreateView(CreateView):
    model = BlogRecord
    form_class = BlogRecordForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.title)
            new_rec.save()
        return super().form_valid(form)


class BlogRecordUpdateView(UpdateView):
    model = BlogRecord
    fields = ('title', 'body', 'preview',)

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.title)
            new_rec.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogRecordListView(ListView):
    model = BlogRecord

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogRecordDetailView(DetailView):
    model = BlogRecord

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogRecordDeleteView(DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('blog:list')


def change_status(request, pk):
    record_item = get_object_or_404(BlogRecord, pk=pk)
    if record_item.is_published:
        record_item.is_published = False
    else:
        record_item.is_published = True

    record_item.save()
    return redirect(reverse('blog:list'))
