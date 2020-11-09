
from typing import List
import numpy as np

# Class that represent an agent which has a 'values' variable as a list,
# so that the index of the list represents the option i and the value in this index is the value of the agent in this option
class Agent:

    # Argument constructor that gets a list of values and assign it to the agent
    def __init__(self, values:List[float]):
        self.values = values

    # A function that gets an option number and return the value of the agent for this option
    def value(self,option:int)->float:
        return self.values[option]

# A function that gets list of agents and 2 option numbers and return True if the first option is Pareto Improvement
def isParetoImprovement(agents:List[Agent], option1:int, option2:int)->bool:
    # For each agent: if at least once his first option value is less than his second option value - return False,
    # Otherwise - return True
    for i in range(0,len(agents)):
        if agents[i].value(option1)<agents[i].value(option2):
            return False

    return True

# A function that gets list of agents, an option number and list of all the options
# and return True if the specific option number is Pareto Optimal
def isParetoOptimal(agents:List[Agent], option:int, allOptions:List[int])->bool:
    # temp matrix that receive values of 0 and 1 and with its help
    # we will check whether the current option is Pareto Optimal
    check_matrix = np.ones((len(agents),len(allOptions)))
    for i in range(0, len(allOptions)):
        for j in range(0,len(agents)):
            if i!=option:
                if agents[j].value(option)<=agents[j].value(allOptions[i]):
                    check_matrix[j][i] = 0

    # Go over the whole temp matrix: if there is one column that is all with zeros - that means this option is Pareto Optimal,
    # Otherwise - if there is no column full of zeros - necessarily this option is Pareto Optimal
    for j in range(0,len(check_matrix[0])):
        for i in range(0,len(check_matrix)):
            if j!=option:
                if check_matrix[i][j] == 1:
                    break
                if i == len(check_matrix)-1 and check_matrix[i][j] == 0:
                    return False
    return True

def main():
    example = [[1,2,3,4,5],[3,1,2,5,4],[3,5,5,1,1]] # Each row represents the values of each person
    # and each column in the row represents the i option out of all the options
    agents = [Agent(example[0]),Agent(example[1]),Agent(example[2])] # construct all agents to a list
    options = [0,1,2,3,4] # all options as a list

    # test for isParetoImprovement function
    print("isParetoImprovement test:")
    print("option 1 is Pareto Improvement of option 2?", isParetoImprovement(agents, 0, 1))
    print("option 4 is Pareto Improvement of option 5?", isParetoImprovement(agents, 3, 4))
    print("option 3 is Pareto Improvement of option 2?", isParetoImprovement(agents, 2, 1))

    # test for isParetoOptimal function
    print("\nisParetoOptimal test:")
    print("option 1 is Pareto Optimal?", isParetoOptimal(agents, 0, options))
    print("option 2 is Pareto Optimal?", isParetoOptimal(agents, 1, options))
    print("option 3 is Pareto Optimal?", isParetoOptimal(agents, 2, options))
    print("option 4 is Pareto Optimal?", isParetoOptimal(agents, 3, options))
    print("option 5 is Pareto Optimal?", isParetoOptimal(agents, 4, options))


if __name__ == '__main__':
    main()