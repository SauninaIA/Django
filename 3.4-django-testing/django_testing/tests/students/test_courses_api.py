import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_example():
    # Arrange
    client = APIClient()

    # Act
    response = client.get()

    assert False, "Just test example"
