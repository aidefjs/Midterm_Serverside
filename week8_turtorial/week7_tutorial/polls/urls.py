from django.urls import path

from polls.view import IndexView,PollView,VoteView

urlpatterns = [
    # ex: /polls/
    path("", IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", PollView.as_view(), name="detail"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", VoteView.as_view(), name="vote"),
]