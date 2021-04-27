from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class BlogPosts(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "testuser",
            email = "testuser@gmail.com",
            password = "1234567@"
        )
        self.post = Post.objects.create(
            title = "Zuri Internship",
            author = self.user,
            body = "Instructors Are Moving Faster Than Their Shadow"
        )

    def test_string_rep(self):
        post = Post(title = "A simple Test")
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "Zuri Internship")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.body}", "Instructors Are Moving Faster Than Their Shadow")

    def test_post_title_view(self):
        response =self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Zuri Internship')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('post/257')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Zuri Internship')
        self.assertTemplateUsed(response, 'view_post.html')