class Person:
    def __init__(self, name) -> None:
        self.name = name

class Employee(Person):
    def __init__(self, name, position, boss) -> None:
        super().__init__(name)
        self.position = position
        self.isBusy = False
        self.boss = boss

class Department:
    def __init__(self) -> None:
        self.director = Employee("Director", "Director", None)
        self.manager = Employee("Manager", "Manager", self.director)
        self.respondent = Employee("Responder", "Responder", self.manager)

    def dispatchCall(self, employee) -> None:

        # OBJECTIVE: Assign call to the next available person

        # If employee doesn't have a boss, exit function
        # NOTE: Directors don't have bosses to pass the call
        if employee is None:
            print("All employees are busy")
            return

        # If employee is busy, pass call to employee's boss. If not, update boolean variable
        if employee.isBusy:
            self.dispatchCall(employee.boss)
        else:
            employee.isBusy = True
            print("{} took the call".format(employee.name))

    def dropCall(self, employee):

        # OBJECTIVE: After a call ends, set employee's status to not busy
        employee.isBusy = False
        print("{} dropped a call".format(employee.name))

def main():

    # Create a department
    it = Department()

    # Add employees to department
    anthony = Employee("Anthony", "Director", None)
    bob = Employee("Bob", "Manager", anthony)
    charlie = Employee("Charlie", "Respondent", bob)

    # Pass call to anthony
    it.dispatchCall(charlie)
    it.dispatchCall(charlie)
    it.dispatchCall(charlie)
    it.dispatchCall(charlie)
    it.dropCall(bob)
    it.dispatchCall(charlie)

main()