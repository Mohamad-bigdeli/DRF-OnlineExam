# import pytest
# from django.contrib.auth import get_user_model
# from rest_framework.test import APIClient
# from django.urls import reverse
# from ..models import Exam, Category

# User = get_user_model()


# @pytest.fixture
# def student():
#     user = User.objects.create_user(
#         phone="09123456789",
#         first_name="test",
#         last_name="testy",
#         role="student",
#         password="test10@test",
#     )
#     return user

# @pytest.fixture
# def instructor():
#     user = User.objects.create_user(
#         phone="09123456789",
#         first_name="test",
#         last_name="testy",
#         role="instructor",
#         password="test10@test",
#     )
#     return user

# @pytest.fixture
# def superuser():
#     user = User.objects.create_superuser(
#         phone="09123456789",
#         first_name="test",
#         last_name="testy",
#         password="test10@test",
#     )
#     return user

# @pytest.fixture
# def api_client():
#     client = APIClient()
#     return client

# @pytest.mark.django_db
# class TestExamApi:

# def test_get_list_exam_response_status_200(api_client):
#     url = reverse("exam:api-v1:exams-list")
#     response = api_client.get(url)
#     assert response.status_code == 200

# def test_get_create_exam_response_status_201(api_client, instructor):
#     url = reverse("exam:api-v1:exams-list")
#     category = Category.objects.create(title="test-title")
#     data = {
#         "title":"test-title",
#         "description":"test",
#         "category":category.id,
#         "duration":3000
#     }
#     api_client.force_authenticate(instructor)
#     response = api_client.post(url, data)
#     assert response.status_code == 201
