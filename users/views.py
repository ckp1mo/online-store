import random
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView
from users.forms import UserRegisterForm, UserForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verification')

    def form_valid(self, form):
        self.object = form.save()
        verify_code = ''.join([str(random.randint(0, 9)) for i in range(8)])
        self.object.verification_code = verify_code
        self.object.is_active = False
        self.object.save()
        send_mail(
            subject='Поздравляем с регистрацией.',
            message='Вы успешно зарегистрировались на платформе онлайн магазина SkyStore\n'
                    f'Для активации аккаунта в специальной форме введите код: {verify_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email],
        )
        return super().form_valid(form)


class VerificationView(TemplateView):
    template_name = 'users/verification.html'

    def mail_verification(self, request):
        verify_code = request.POST.get('verification_code')
        user_code = User.objects.filter(verification_code=verify_code).first()
        if user_code is not None and user_code.verification_code == verify_code:
            user_code.is_active = True
            user_code.save()
            return redirect('users:login')
        else:
            return redirect('users:login')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def generate_new_password(request):
    new_password = User.objects.make_random_password()
    send_mail(
        subject='Смена пароля',
        message=f'Вы успешно изменили пароль. Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))
