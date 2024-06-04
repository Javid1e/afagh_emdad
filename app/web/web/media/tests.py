# media/tests.py
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from users.models import User
from .models import Media


class MediaModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', phone_number='09123456789',
                                             password='password123')

    def test_create_media(self):
        content_type = ContentType.objects.get_for_model(User)
        media = Media.objects.create(associated_model=content_type, object_id=self.user.id,
                                     file_url='http://example.com/file.jpg', file_type='image/jpeg')
        self.assertEqual(media.associated_model, content_type)
        self.assertEqual(media.object_id, self.user.id)
        self.assertEqual(media.file_url, 'http://example.com/file.jpg')
        self.assertEqual(media.file_type, 'image/jpeg')
