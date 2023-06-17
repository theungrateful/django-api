from rest_framework import status

from core.fixtures.user import user
from core.fixtures.post import post


class TestUserViewSet:
    endpoint = '/api/user/'
    
    def test_list(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_retrieve(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(user.public_id) + '/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == user.public_id.hex
    
    def test_create(self, client, user):
        client.force_authenticate(user=user)
        data = {
            "username": "test_user_1",
            "email": "test_user_1@example.com",
            "first_name": "Test_1",
            "last_name": "User_1",
            "password": "test_password"
        }
        response = client.post(self.endpoint, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["username"] == data['username']
        assert response.data["email"] == data['email']
        assert response.data["first_name"] == data['first_name']
        assert response.data["last_name"] == data['last_name']

    def test_update(self, client, user):
        client.force_authenticate(user=user)
        data = {
            "first_name": "Test_01",
        }
        response = client.patch(self.endpoint + str(user.public_id) + '/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['first_name'] == data['first_name']

        