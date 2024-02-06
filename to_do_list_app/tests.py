from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import ToDoItems


class ToDoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """This function creates user and the first instance"""

        """cls.user creates user"""
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        """cls.todo creates the first instance and 
        the first instance creates data base"""
        cls.todo = ToDoItems.objects.create(
            title="Test To-Do",
            description="What to do",
            due_date="2024-01-13",
            completion_status=False,
        )

    def testCreateView(self):
        response_post = self.client.post(
            reverse("new"),
            {
                "title": "Good title",
                "description": "Good description",
                "due_date": "2024-05-23",
                "completion_status": False,
            },
        )
        self.assertEqual(response_post.status_code, 302)
        response_get = self.client.get(reverse("new"))
        self.assertEqual(response_get.status_code, 200)
        new_todo = ToDoItems.objects.last()
        self.assertEqual(new_todo.completion_status, False)

    def testUpdateView(self):
        last_item = ToDoItems.objects.last()
        response = self.client.get(reverse("edit", args=[last_item.pk]))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse("edit", args=[last_item.pk]),
            {
                "title": "Updated title",
                "description": "Updated description",
                "due_date": "2024-12-10",
            },
        )
        self.assertEqual(response.status_code, 302)

    def testDeleteView(self):
        page_exists = self.client.get(
            reverse("delete", args=[ToDoItems.objects.last().pk])
        )
        self.assertEqual(page_exists.status_code, 200)
        self.assertContains(page_exists, 'type="submit" value="Confirm"')

        response = self.client.post(
            reverse("delete", args=[ToDoItems.objects.last().pk])
        )
        self.assertFalse(ToDoItems.objects.filter(pk=ToDoItems.objects.last()).exists())
        self.assertEqual(response.status_code, 302)
