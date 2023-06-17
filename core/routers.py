from rest_framework_nested import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets import RefreshViewSet
from core.blog.comment.viewsets import CommentViewSet
from core.blog.post.viewsets import PostViewSet


router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
router.register(r'blog/post', PostViewSet, basename='post')

posts_router = routers.NestedSimpleRouter(router, r'blog/post', lookup='post')
posts_router.register(r'comment', CommentViewSet, basename='post-comment')

urlpatterns = [
    *router.urls,
    *posts_router.urls
]