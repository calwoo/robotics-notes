""" Command-line simulator for a simple 2D robot.

https://w3.cs.jmu.edu/spragunr/CS354_F16/labs/python_pa/pa0.shtml
"""
import sys

class RobotSim(object):
    """Simulation of a simple 2D robot. """

    def __init__(self):
        """ The robot always begins at (0,0). """
        self.x = 0
        self.y = 0

    def execute_program(self, file_name):
        """ Read and execute the program stored in the indicated file.
        The robots x and y positions will be updated.

        No return value.
        """
        with open(file_name, "r") as f:
            program = f.readlines()

        instructions = self.interpret_program(program)
        for direction, value in instructions:
            if direction == "NORTH":
                self.y += value
            elif direction == "SOUTH":
                self.y -= value
            elif direction == "WEST":
                self.x -= value
            elif direction == "EAST":
                self.x += value

    def interpret_program(self, program):
        instructions = []
        function_defs = {}
        program_counter = 0

        while program_counter < len(program):
            line = program[program_counter].strip()
            # function definition
            if line.startswith("def"):
                function_name = line.split()[1]
                function = []
                program_counter += 1
                while True:
                    line = program[program_counter].strip()
                    if line == "end":
                        break
                    if line in function_defs:
                        function += function_defs[line]
                    else:
                        function.append(tuple(line.split()))
                    program_counter += 1
                function_defs[function_name] = function
            elif line in function_defs:
                instructions += function_defs[line]
            else:
                instructions.append(tuple(line.split()))
            program_counter += 1

        # clean instructions
        instructions = [(n, int(v)) for n, v in instructions]
        return instructions
                
    def get_location(self):
        """ Return the robot's current location as an (x, y) tuple. """
        return self.x, self.y


def main():
    """ Simulate the execution of the robot on a program.

    usage: robot_sim.py PROGRAM_FILE_NAME

    """
    robot = RobotSim()
    robot.execute_program(sys.argv[1])
    print("ROBOT FINAL POSITION: {}".format(robot.get_location()))

if __name__ == "__main__":
    main()
