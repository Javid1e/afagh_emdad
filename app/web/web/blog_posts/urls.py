# blog_posts/urls.py
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, CommentViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'blog-posts', BlogPostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = router.urls
