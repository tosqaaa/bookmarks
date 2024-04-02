from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import ImageCreateForm
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Изображение добавлено успешно')
            return redirect(new_image.get_absolute_url())
        else:
            messages.error(request, 'Произошла ошибка добавления изображения')
    else:
        form = ImageCreateForm(data=request.GET)
    context = {
        'form': form
    }
    return render(request, 'images/image/create.html', context=context)


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    context = {
        'image': image
    }
    return render(request, 'images/image/detail.html', context=context)


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.user_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass
        return JsonResponse({'status': 'error'})
