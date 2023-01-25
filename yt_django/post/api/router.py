from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet  #la vista que creamos en el view

router_posts = DefaultRouter()

router_posts.register(prefix='post',basename='post',viewset=PostApiViewSet)
