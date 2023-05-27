import pytest

from core.fixtures.post import Post
from core.fixtures.user import User

from core.blog.comment.models import Comment


@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post, body="Test Comment Body")
