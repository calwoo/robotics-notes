""" CS354 HW1 Python Exercises

Author: Nathan Sprague & 
Version: 9/17/2020
"""

import numpy as np
from transforms import trans, rot_x, rot_y, rot_z

# Configure numpy for prettier printing
np.set_printoptions(precision=6, suppress=True)

class PhantomKinematics:
    """ Handle forward kinematics for the PhantomX gripper arm. """

    def __init__(self, theta_s, theta_e):
        """ Initialize all coordinate transforms. """

        # Naming convention: F_g_e indicates the transformation matrix
        # F_g^e that aligns coordinate frame g with coordinate frame
        # e.

        self.theta_s = theta_s  # These are actually calling the
        self.theta_e = theta_e  # setters below!
        self.F_g_e = trans(0, 0, -0.18)
        self.F_e_g = trans(0, 0, 0.18)

    @property
    def theta_s(self):
        return self._theta_s

    @theta_s.setter
    def theta_s(self, theta_s):
        self._theta_s = theta_s
        self.F_s_b = rot_z(-self._theta_s) @ trans(0, 0, -0.08)
        self.F_b_s = trans(0, 0, 0.08) @ rot_z(self._theta_s)


    @property
    def theta_e(self):
        return self._theta_e

    @theta_e.setter
    def theta_e(self, theta_e):
        self._theta_e = theta_e
        self.F_e_s = rot_y(-self._theta_e) @ trans(0, 0, -0.15)
        self.F_s_e = trans(0, 0, 0.15) @ rot_y(self._theta_e)

    def gripper_to_base(self, point):
        """Convert the indicated point from gripper coordinates to base
           coordinates given the current joint angles (in radians).

        Arguments:
          point - length-three numpy array containing the coordinates
                  of a point in the gripper coordinate frame.

        Returns:
          A length-three numpy array representing the position of the
          point in the base coordinate frame.

        """
        # YOUR CODE HERE
        # np.append may be useful for converting to homegenous coordinates. 
        point_homogenous = np.append(point, [1.0])
        T_g_b = self.F_b_s @ self.F_s_e @ self.F_e_g
        base_homogenous = T_g_b @ point_homogenous
        return base_homogenous[:3]

    def base_to_gripper(self, point):
        """Convert the indicated point from gripper coordinates to base
        coordinates given the indicated joint angles (in radians).

        Arguments:
          point - length-three numpy array containing the coordinates
                  of a point in the gripper coordinate frame.

        Returns:
          A length-three numpy array representing the position of the
          point in the base coordinate frame.

        """
        # YOUR CODE HERE
        # np.append may be useful for converting to homegenous coordinates. 
        point_homogenous = np.append(point, [1.0])
        T_b_g = self.F_g_e @ self.F_e_s @ self.F_s_b
        gripper_homogenous = T_b_g @ point_homogenous
        return gripper_homogenous[:3]


def tests():
    """ Recalculate the results from the homework. """
    ph = PhantomKinematics(0, 0)

    print("theta_s = 0, theta_e = 0")
    print("(0, 0, 0)_g in base coordinates: ")
    result = ph.gripper_to_base(np.array([0, 0, 0]))
    print(result)
    assert result.size == 3
    print("(0, 0, 0)_b in gripper coordinates: ")
    result = ph.base_to_gripper(np.array([0, 0, 0]))
    print(result)
    assert result.size == 3

    ph.theta_s = np.pi/2.0
    ph.theta_e = 0
    print("\ntheta_s = 90 degrees, theta_e = 0")
    print("(0, 0, 0)_g in base coordinates: ")
    print(ph.gripper_to_base(np.array([0, 0, 0])))
    print("(0, 0, 0)_b in gripper coordinates: ")
    print(ph.base_to_gripper(np.array([0, 0, 0])))

    ph.theta_s = np.pi/2.0
    ph.theta_e = np.pi/2.0
    print("\ntheta_s = 90 degrees, theta_e = 90 degrees")
    print("(0, 0, 0)_g in base coordinates: ")
    print(ph.gripper_to_base(np.array([0, 0, 0])))
    print("(0, 0, 0)_b in gripper coordinates: ")
    print(ph.base_to_gripper(np.array([0, 0, 0])))
    print("(.4, 0, 0)_g in base coordinates: ")
    print(ph.gripper_to_base(np.array([.4, 0, 0])))
    print("(.4, 0, 0)_b in gripper coordinates: ")
    print(ph.base_to_gripper(np.array([.4, 0, 0])))

if __name__ == "__main__":
    tests()
