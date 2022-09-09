# Create a function called whoIsTheNearestCommonManager() that receives as
# input two employee instances, and returns the closest manager that manages both employees.

# https://bit.ly/37JmZMa

from __future__ import annotations

organisation = {"CEO": {
    "M1": {"S1": {"A": {}, "B": {}, "C": {}}, "S2": {"D": {}}, "S3": {}},
    "M2": {"T1": {"E": {}, "T2": {}, "T3": {}}
           }}}


class Employee:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
        self.employees = set()


def build_org(manager, employees, empls_dict):
    for emp_name, children in employees.items():
        employee = Employee(emp_name, manager)
        if manager:
            manager.employees.add(employee)
        empls_dict[emp_name] = employee
        if children:
            build_org(employee, children, empls_dict)


empls = dict()
build_org(None, organisation, empls)


def whoIsTheNearestCommonManager(e1, e2):
    if e1.manager == e2 and e1.manager is not None:
        return e2.manager if e2.manager is not None else e2
    elif e1 == e2.manager and e2.manager is not None:
        return e1.manager if e1.manager is not None else e1
    elif e1.manager == e2.manager:
        return e1.manager
    if e1.manager is not None:
        e1 = e1.manager
    if e2.manager is not None:
        e2 = e2.manager

    return whoIsTheNearestCommonManager(e1, e2)


A, B, E, D = empls['A'], empls['B'], empls['E'], empls['D']
S1, M1, CEO = empls['S1'], empls['M1'], empls['CEO']

assert whoIsTheNearestCommonManager(A, B) == S1
assert whoIsTheNearestCommonManager(A, D) == M1
assert whoIsTheNearestCommonManager(A, S1) == M1
assert whoIsTheNearestCommonManager(A, E) == CEO
assert whoIsTheNearestCommonManager(E, M1) == CEO
assert whoIsTheNearestCommonManager(B, M1) == CEO
assert whoIsTheNearestCommonManager(M1, A) == CEO

