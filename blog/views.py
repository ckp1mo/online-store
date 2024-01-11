from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from blog.forms import BlogRecordForm, BlogRecordUpdateForm
from blog.models import BlogRecord


class BlogRecordCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = BlogRecord
    form_class = BlogRecordForm
    success_url = reverse_lazy('blog:list_post')
    permission_required = 'blog.add_blogrecord'

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.title)
            new_rec.user = self.request.user
            new_rec.save()
        return super().form_valid(form)


class BlogRecordUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = BlogRecord
    form_class = BlogRecordUpdateForm
    permission_required = 'blog.change_blogrecord'

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.title)
            new_rec.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view_post',     args=[self.kwargs.get('pk')])


class BlogRecordListView(LoginRequiredMixin, ListView):
    model = BlogRecord

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.is_superuser or self.request.user.has_perm('blog.set_published') :
            return queryset
        return queryset.filter(is_published=True)


class BlogRecordDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = BlogRecord
    permission_required = 'blog.view_blogrecord'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogRecordDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('blog:list_post')
    permission_required = 'blog.delete_blogrecord'


@permission_required('blog.set_published')
def change_status(request, pk):
    record_item = get_object_or_404(BlogRecord, pk=pk)
    if record_item.is_published:
        record_item.is_published = False
    else:
        record_item.is_published = True

    record_item.save()
    return redirect(reverse('blog:list_post'))
