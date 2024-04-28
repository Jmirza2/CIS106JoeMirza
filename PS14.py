class Employee:

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'


  def bonus(self, rate):
    b = float(rate) * float(self.pay)
    return b


emp11 = Employee('Joe', 'Mirza', 100000)

print(emp11.email)
print(emp11.first)
print(emp11.last)
print(emp11.pay)
print(emp11.bonus(0.10))
print(emp11.bonus(0.20))


class Student:
  
  def __init__(self, first, last, district, enrolled_credits):
    self.first = first
    self.last = last
    self.district = district
    self.enrolled_credits = enrolled_credits

  def compute_tuition_owed(self):
      if self.district == 'I':
          tuition_rate = 250.00
      else:
          tuition_rate = 500.00
      return self.enrolled_credits * tuition_rate

# Test the class
student1 = Student("Dan", "Lee", "I", 14)
student2 = Student("Mike", "Smith", "O", 5)

print("Student 1 Tuition Owed:", student1.compute_tuition_owed())
print("Student 2 Tuition Owed:", student2.compute_tuition_owed())
