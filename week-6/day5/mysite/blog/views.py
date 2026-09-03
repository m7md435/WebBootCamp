from django.shortcuts import render

POSTS = [
	{
		'id': 1,
		'title': 'A Simple Guide to Django URLs',
		'category': 'django',
		'summary': 'Learn how project and app URL files work together.',
	},
	{
		'id': 2,
		'title': 'Why Named Routes Matter',
		'category': 'python',
		'summary': 'Build links that keep working when URL paths change.',
	},
]


def post_list(request):
	return render(request, 'list.html', {'posts': POSTS})


def post_detail(request, post_id):
	post = next((post for post in POSTS if post['id'] == post_id), None)
	if post is None:
		from django.http import HttpResponseNotFound
		return HttpResponseNotFound('404: Post not found')
	return render(request, 'detail.html', {'post': post})


def category_posts(request, category):
	posts = [post for post in POSTS if post['category'] == category]
	return render(request, 'category.html', {
		'category': category,
		'posts': posts,
	})
