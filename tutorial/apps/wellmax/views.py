from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserServiceEvaluationForm, UserInfoForm
from .models import UserInfo


def user_info_view(request):
    form = UserInfoForm()

    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user = form.save()
            key = user.unique_id
            return redirect('wellmax:evaluation', key)
        else:
            print(form.errors)
            return HttpResponse('Form Failed !!!, try again')

    context = {'form': form}
    return render(request, 'user_info.html', context)


def user_evaluation_view(request, token):
    form = UserServiceEvaluationForm()
    if request.method == 'POST':
        form = UserServiceEvaluationForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = UserInfo.objects.get(unique_id=token)
            data.save()
            messages.success(request, 'Спасибо !, Успешно отправлено, можно отправить еще раз')
            return redirect('wellmax:profile')
        else:
            print(form.errors)
            return HttpResponse('Form Failed !!!, try again')
    context = {'form': form}
    return render(request, 'user_evaluation.html', context)