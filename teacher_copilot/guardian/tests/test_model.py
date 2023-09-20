from django.test import TestCase
from student.models import Student
from django.contrib.auth.models import User
from datetime import date

# from django.utils import timezone
from guardian.models import Guardian

valid_student_mock = {
    "first_name": "joao",
    "last_name": "espanha",
    "email": "espanha@gmail.com",
    "phone_number": "219983737",
    "notes": "forte demais",
    "birthday": date(2000, 4, 15),
    "instagram": "@olaaola",
    "football_team": "flamengo",
    "grade": "sexto ano",
    "school": "pentagono",
    "favorite_subject": "Matematica",
}
user = {
    "username": "renata",
    "email": "prof@gmail.com",
    "password": "219933737",
}


class GuardianModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(**user)

        self.valid_guardian = {
            "first_name": "Ed",
            "last_name": "Rocha",
            "email": "ed@gmail.com",
            "phone_number": "219933737",
            "notes": "baixo demais",
            "created_by": self.user,
        }

        Guardian.objects.create(**self.valid_guardian)

        self.guardian = Guardian.objects.get(email=self.valid_guardian["email"])

    def tests_if_guardian_info_is_created_correctly_when_given_a_valid_guardian(self):
        self.assertEqual(self.guardian.first_name, self.valid_guardian["first_name"])
        self.assertEqual(self.guardian.last_name, self.valid_guardian["last_name"])
        self.assertEqual(self.guardian.email, self.valid_guardian["email"])
        self.assertEqual(
            self.guardian.phone_number, self.valid_guardian["phone_number"]
        )
        self.assertEqual(self.guardian.notes, self.valid_guardian["notes"])

    def tests_if_the_guardian_student_relation_is_correct(self):
        self.student = Student.objects.create(**valid_student_mock)

        self.guardian.students.add(self.student)

        self.assertIn(self.student, self.guardian.students.all())
