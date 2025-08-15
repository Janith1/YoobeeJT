class Employee_Information:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary

    def display_info(self):
        print("\nEmployee Name:", self.name)
        print("Title:", self.title)
        print("Salary:", format(self.salary,","))

    def increment_info(self, increment):
        print(f"\nIncrement amount of Employee ({self.name}) :{format(increment,',')}")
        self.salary += increment
        print(f"Updated Salary :{format(self.salary,",")}")


def main():
    employee1_info = Employee_Information("Janith","QA Engineer",10000)
    employee2_info = Employee_Information("John", "Software Engineer", 12000)

    employee1_info.display_info()
    employee2_info.display_info()

    employee1_info.increment_info(1000)
    employee2_info.increment_info(1500)


if __name__ == '__main__':
    main()

