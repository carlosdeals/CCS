from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import CommentForm, FeedbackForm
from django.core.mail import mail_admins



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'listing.html'
    paginate_by = 3

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'view_blog.html'

def post_detail(request, slug):
    template_name = 'view_blog.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])
            mail_admins(subject, message)

            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')
    else:
        f = FeedbackForm()
    return render(request, 'feedback.html', {'form': f})



# @login_required
# def add_messages(request):
#     username = request.user.username
#     messages.add_message(request, messages.INFO, f"Hello {username}")
#     messages.add_message(request, messages.WARNING, "DANGER WILL ROBINSON")

#     return HttpResponse("Messages added", content_type="text/plain")
#     ß
# @user_passes_test(lambda user: user.is_staff)
# def staff_place(request):
#     return HttpResponse("Employees must wash hands", content_type="text/plain")

# @login_required
# def private_place(request):
#     return HttpResponse("Shhh, members only!", content_type="text/plain")

# def listing(request):
#     data = {
#         "blogs": Blog.objects.all(),
#     }

#     return render(request, "listing.html", data)

# def view_blog(request):
#     blog = Blog.objects.get()

#     if request.method == 'POST':
#         form = CommentForm(request.POST)

#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()

#             return redirect('view_blog')
#     else:
#         form = CommentForm()

#     return render(request, 'blog/view_blog.html', {'post': post, 'form': form})

# def see_request(request):
#     text = f"""
#         Some attributes of the HttpRequest object:

#         scheme: {request.scheme}
#         path:   {request.path}
#         method: {request.method}
#         GET:    {request.GET}
#         user:   {request.user}
#     """

#     return HttpResponse(text, content_type="text/plain")

# def user_info(request):
#     text = f"""
#         Selected HttpRequest.user attributes:

#         username:     {request.user.username}
#         is_anonymous: {request.user.is_anonymous}
#         is_staff:     {request.user.is_staff}
#         is_superuser: {request.user.is_superuser}
#         is_active:    {request.user.is_active}
#     """

#     return HttpResponse(text, content_type="text/plain")
