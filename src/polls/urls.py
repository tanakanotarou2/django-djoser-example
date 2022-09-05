from rest_framework.routers import SimpleRouter

from polls import views

router = SimpleRouter()
router.register("questions", views.QuestionViewSet)

urlpatterns = router.urls
