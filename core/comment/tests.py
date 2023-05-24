import pytest

from core.fixtures.post import post
from core.fixtures.user import user
from core.comment.models import Comment


@pytest.mark.django_db
def test_create_comment(user, post):
    comment = Comment.objects.create(
        author=user,
        body="Test Comment body",
        post=post
    )
    assert comment.author == user
    assert comment.body == "Test Comment body"
    assert comment.post == post
