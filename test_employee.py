import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        employee_1 = Employee('Martin','Stuwe', 1800)
        employee_2 = Employee('Elon','Musk', 5000000)

        self.assertEqual(employee_1.email, 'MartinStuwe@gmail.com')
        self.assertEqual(employee_2.email,'ElonMusk@gmail.com')

        employee_1.first = 'Marcin'
        employee_2.first = 'XAEA-XII'

        self.assertEqual(employee_1.email,'MarcinStuwe@gmail.com')
        self.assertEqual(employee_2.email,'XAEA-XIIMusk@gmail.com')


if __name__ == '__main__':
    unittest.main()