import unittest
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student('John', 'Doe')

    def test_get_start_date(self):
        self.assertEqual(self.student.get_start_date(), date.today())

    def test_apply_extension(self):
        self.student.apply_extension(30)
        self.assertEqual(self.student.end_date, date.today() + timedelta(days=395))  # Ta hänsyn till skottår

    def test_has_extension(self):
        self.assertFalse(self.student.has_extension())  # Studenten borde inte ha en förlängning ännu
        self.student.apply_extension(30)
        self.assertTrue(self.student.has_extension())  # Studenten bör nu ha en förlängning

    def test_add_and_get_project_score(self):
        self.student.add_project_score('project1', 95)
        self.assertEqual(self.student.get_project_score('project1'), 95)
        self.assertIsNone(self.student.get_project_score('project2'))  # Projektbetyg saknas

if __name__ == '__main':
    unittest.main()
