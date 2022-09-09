class Solution:
    def __init__(self, api):
        self.api = api
        # You can initiate and calculate things here

    def get_total_number_of_employees(self):
        """
        Return the total number of employees in the organization.


        :rtype: int
        """
        # Write your code here
        total_employees = 1
        for key, value in self.api.items():
            if key > 0:
                total_employees += len(value)

        return total_employees

    def get_number_of_employees_at_level(self, level):
        """
        Given a level in the hierarchy return the total number of employees on
        that level.

        :type level: int

        :rtype: int
        """
        # Write your code here
        # employees_per_level = 1
        # for key, value in self.api:
        #     if key == level:
        #         employees_per_level += str(len(value)) ","

        return 1 if level == 0 else len(self.api[level])

    def update_employee(self, level, *args):
        if level == 0:
            self.api[level] = args[0]
        else:
            employee_list = [arg for arg in args]

            self.api[level] = employee_list


solution = Solution({})
solution.update_employee(0, "Dovie")
solution.update_employee(1, "Estella", "Clinton")
solution.update_employee(2, "luvenia")
solution.update_employee(3, "saf","asf","sag")
print(solution.get_total_number_of_employees())
print(solution.get_number_of_employees_at_level(2))
print(solution.get_number_of_employees_at_level(1))
print(solution.get_number_of_employees_at_level(3))
print(solution.get_number_of_employees_at_level(0))





