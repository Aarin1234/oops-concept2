class students:
    name = input("Enter your name: ")
    age = 12
    schoolyear = 6
    teacher = "Priya"

    #creating a func
    def show_Details(self):
        print("\n\nThe details of the student are:")
        print("name :", self.name)
        print(f'school year : {self.schoolyear}')
        print(f'age : {self.age}')
        print(f'teacher : {self.teacher}')


    #changing the details usin the function
    def change_details(self):
        print("please update your age: ")
        self.age = int(input())
        print("please update the name of the student: ")
        self.name = input()
        print('\n details updated')

#creating object

student1 = students()
student2 = students()


print(f'\nName of the student: {student1.name}')
print(f'\n Age of the student: {student1.age}')
print(f'\n Name of the teacher:{student1.teacher}')

student2.show_Details()

#calling function to change the details
print("change students details")
student1.change_details()

print('\n')
student1.show_Details()
