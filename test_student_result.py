import unittest

from student_result import calculate_average, calculate_grade, student_result


class TestStudentResult(unittest.TestCase):

    def test_average(self):
        marks = [80, 90, 70]
        self.assertEqual(calculate_average(marks), 80)

    def test_grade_A(self):
        self.assertEqual(calculate_grade(85), "A")

    def test_grade_A_plus(self):
        self.assertEqual(calculate_grade(95), "A+")

    def test_grade_F(self):
        self.assertEqual(calculate_grade(40), "F")

    def test_student_result(self):
        result = student_result("Ankita", [80, 90, 70])

        self.assertEqual(result["name"], "Ankita")
        self.assertEqual(result["average"], 80)
        self.assertEqual(result["grade"], "A")


if __name__ == "__main__":
    unittest.main()