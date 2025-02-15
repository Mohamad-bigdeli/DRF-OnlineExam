import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import Category, FavoriteCategory

User = get_user_model()

@pytest.fixture
def common_user():
    user = User.objects.create_user(phone="09123456789", first_name="test",
                                    last_name="testy", role="student", password="test10@test")
    return user

@pytest.fixture
def superuser():
    user = User.objects.create_superuser(phone="09123456789", first_name="test",
                            last_name="testy", password="test10@test")
    return user

@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.mark.django_db
class TestCategoryApi:
    
    def test_get_list_category_response_200_status(self, api_client):
        url = reverse("exam:api-v1:categories-list")
        response = api_client.get(url)
        assert response.status_code == 200 
    
    def test_create_category_response_401_status(self, api_client):
        url = reverse("exam:api-v1:categories-list")
        data = {
            "title":"test-title"
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_category_response_403_status(self, api_client, common_user):
        url = reverse("exam:api-v1:categories-list")
        data = {
            "title":"test-title"
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_create_category_response_201_status(self, api_client, superuser):
        url = reverse("exam:api-v1:categories-list")
        data = {
            "title":"test-title"
        }
        api_client.force_authenticate(user=superuser)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_get_detail_category_response_status_200(self, api_client):
        category = Category.objects.create(title="test-title")
        url = reverse("exam:api-v1:categories-detail", kwargs={"pk":category.id})
        response = api_client.get(url)
        assert response.status_code == 200
    
    def test_put_category_response_status_200(self, api_client, superuser):
        category = Category.objects.create(title="OldTitle")
        url = reverse("exam:api-v1:categories-detail", kwargs={"pk":category.id})
        updated_data = {
            "title":"NewTitle"
        }
        api_client.force_authenticate(user=superuser)
        response = api_client.put(url, updated_data)
        assert response.status_code == 200

    def test_put_category_response_status_401(self, api_client):
        category = Category.objects.create(title="OldTitle")
        url = reverse("exam:api-v1:categories-detail", kwargs={"pk":category.id})
        updated_data = {
            "title":"NewTitle"
        }
        response = api_client.put(url, updated_data)
        assert response.status_code == 401

    def test_put_category_response_status_403(self, api_client, common_user):
        category = Category.objects.create(title="OldTitle")
        url = reverse("exam:api-v1:categories-detail", kwargs={"pk":category.id})
        updated_data = {
            "title":"NewTitle"
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.put(url, updated_data)
        assert response.status_code == 403

    def test_delete_category_response_status_204(self, api_client, superuser):
        category = Category.objects.create(title="test-title")
        url = reverse("exam:api-v1:categories-detail", kwargs={"pk":category.id})
        api_client.force_authenticate(user=superuser)
        response = api_client.delete(url)
        assert response.status_code == 204

@pytest.mark.django_db
class TestFavoriteCategoryApi:
    
    def test_get_favorite_category_response_status_code_200(self, api_client, common_user):
        url = reverse("exam:api-v1:favorite-categories-list")
        api_client.force_authenticate(user=common_user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_favorite_category_response_status_code_201(self, api_client, common_user):
        category = Category.objects.create(title="test-title")
        url = reverse("exam:api-v1:favorite-categories-list")
        api_client.force_authenticate(user=common_user)
        data = {
            "category":category.id
        }
        response = api_client.post(url, data)
        assert response.status_code == 201 

    def test_get_detail_favorite_category_response_status_code_200(self, api_client, common_user):
        category = Category.objects.create(title="test-title")
        favorite_category = FavoriteCategory.objects.create(category=category, student=common_user)
        url = reverse("exam:api-v1:favorite-categories-detail", kwargs={"pk":favorite_category.id})
        api_client.force_authenticate(user=common_user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_delete_favorite_category_response_status_code_204(self, api_client, common_user):
        category = Category.objects.create(title="test-title")
        favorite_category = FavoriteCategory.objects.create(category=category, student=common_user)
        url = reverse("exam:api-v1:favorite-categories-detail", kwargs={"pk":favorite_category.id})
        api_client.force_authenticate(user=common_user)
        response = api_client.delete(url)
        assert response.status_code == 204

