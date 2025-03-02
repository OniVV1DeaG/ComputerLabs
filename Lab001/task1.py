from pulp import LpVariable, LpProblem, LpMaximize, value
from cvxopt.modeling import variable, op
import time

def calculate_goal_function() -> tuple:
    start = time.time()
    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)
    x3 = LpVariable("x3", lowBound=0)
    x4 = LpVariable("x4", lowBound=0)
    problem = LpProblem("maximize-profit", LpMaximize)
    problem += 8*x1 + 3*x2 + 2*x3 + 1*x4, "Goal Function"
    problem += 2*x1 + 1*x2 + 1*x3 + 3*x4 <= 300, "1"
    problem += (1*x1 + 0*x2 + 2*x3 + 1*x4 <= 70, "2")
    problem += (1 * x1 + 2 * x2 + 1 * x3 + 0 * x4 <= 340, "3")
    problem.solve()
    print("result")
    variables = {}
    for variable in problem.variables():
        print(variable.name, "=", variable.varValue)
        variables[variable.name] = variable.varValue

    print("Profit: ", value(problem.objective))
    stop = time.time()
    print("Time: ", stop - start)
    return variables, value(problem.objective)

def calculate_cvxopt():
    start = time.time()
    x = variable(4, 'x')
    problem = -(8*x[0] + 3*x[1] + 2*x[2] + 1*x[3]) #goal
    mass1 = (2*x[0] + 1*x[1] + 1*x[2] + 3*x[3] <= 300)
    mass2 = (1*x[0] + 0*x[1] + 2*x[2] + 1*x[3] <= 70)
    mass3 = (1 * x[0] + 2 * x[1] + 1 * x[2] + 0 * x[3] <= 340)
    x_non_negative = (x >= 0)
    z = op(problem, [mass1, mass2, mass3, x_non_negative])
    z.solve(solver="glpk")
    z.status

    print("Profit:")
    print(abs(z.objective.value()[0]))
    print("Result:")
    print(x.value)
    stop = time.time()
    print("Time:")
    print(stop - start)

if __name__ == "__main__":
    calculate_cvxopt()