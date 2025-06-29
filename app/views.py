from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Thread, Comment
from .forms import ThreadForm

from django.contrib.auth.decorators import login_required



def index(request):
    name_list = list(Thread.objects.values_list('thread_name', flat=True))

    """
    ログインユーザーのIDをテンプレートに渡すビュー関数
    """
    user_id = request.user.id

    context = {
        'name_list': name_list,
        'user_id': user_id,
    }  # ここで辞書にする
    return render(request, 'app/index.html', context)

def board_detail(request, slug, password):
    thread = get_object_or_404(Thread, slug=slug)

    # Check if the provided password matches the thread's password
    if thread.password != password:
        messages.error(request, "Incorrect password. Access denied.")
        return redirect('index')

    comments = thread.comments.all()

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:  # 内容が空でないことを確認
            Comment.objects.create(thread=thread, content=content)
            return redirect('board_detail', slug=slug, password=password)  # 投稿後にリダイレクト

    context = {
        'board_slug': slug,
        'thread': thread,
        'comments': comments
    }
    return render(request, 'app/board.html', context)

def create_board(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        redirect_site = request.POST.get('slug')
        redirect_pass = request.POST.get('password')
        print(form)
        if form.is_valid():
            form.save()  # フォームの内容を保存して新しいThreadを作成
            return redirect('board_detail', slug=redirect_site, password=redirect_pass)
    else:
        form = ThreadForm()  # 空のフォームを表示
    context = {
        'form': form
    }
    return render(request, 'app/create_board.html', context)
