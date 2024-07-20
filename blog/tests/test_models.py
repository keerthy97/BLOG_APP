from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post.')
        self.assertEqual(self.post.author.username, 'testuser')

    def test_total_likes(self):
        self.assertEqual(self.post.total_likes(), 0)
        self.post.likes.add(self.user)
        self.assertEqual(self.post.total_likes(), 1)

class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author='Commenter',
            text='This is a test comment.'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.author, 'Commenter')
        self.assertEqual(self.comment.text, 'This is a test comment.')
        self.assertEqual(self.comment.post.title, 'Test Post')
