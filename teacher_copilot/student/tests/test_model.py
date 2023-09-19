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


class StudentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(**user)

        valid_guardian_mock = {
            "first_name": "Ed",
            "last_name": "Rocha",
            "email": "ed@gmail.com",
            "phone_number": "219933737",
            "notes": "baixo demais",
            "created_by": self.user,
        }

        self.valid_guardian_01 = Guardian.objects.create(**valid_guardian_mock)

        self.valid_student_01 = Student.objects.create(**valid_student_mock)

        self.valid_student_01.guardians.add(self.valid_guardian_01)
        self.valid_student_01.teacher.add(self.user)

    def tests_if_given_a_valid_student_it_creates_a_correct_obj(self):
        valid_student = Student.objects.get(email=valid_student_mock["email"])

        self.assertEqual(valid_student.email, valid_student_mock["email"])
        self.assertEqual(valid_student.first_name, valid_student_mock["first_name"])
        self.assertEqual(valid_student.last_name, valid_student_mock["last_name"])
        self.assertEqual(valid_student.phone_number, valid_student_mock["phone_number"])
        self.assertEqual(valid_student.notes, valid_student_mock["notes"])
        self.assertEqual(valid_student.birthday, valid_student_mock["birthday"])
        self.assertEqual(valid_student.instagram, valid_student_mock["instagram"])
        self.assertEqual(
            valid_student.football_team, valid_student_mock["football_team"]
        )
        self.assertEqual(valid_student.grade, valid_student_mock["grade"])
        self.assertEqual(valid_student.school, valid_student_mock["school"])
        self.assertEqual(
            valid_student.favorite_subject, valid_student_mock["favorite_subject"]
        )

        self.assertIn(self.user, valid_student.teacher.all())

        self.assertIn(self.valid_guardian_01, valid_student.guardians.all())

        self.assertTrue(valid_student.is_active)
