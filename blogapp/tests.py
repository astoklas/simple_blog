from django.test import TestCase
from blogapp.models import BlogArticle

class TestCase(TestCase):
    def setUp(self):
        BlogArticle.objects.create(title="TitleA", blog_content="roar", user=None)
        BlogArticle.objects.create(title="TitleB", blog_content="meow", user=None)

    def test_blogs(self):
        blogs = BlogArticle.objects.all();


    def get_user(self):
# Create your tests here.
