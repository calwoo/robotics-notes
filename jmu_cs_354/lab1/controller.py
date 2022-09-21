"""
Controller Exercise: Modify get_force to move the locomotive to the target
location using minimum fuel and time.
"""

import locomotive_sim


def get_force(target_x, cur_x):
    """
    Control a locomotive by determining the amount of force to apply given
    the current location and the goal location.

    :param target_x:  Goal location
    :param cur_x: Current location
    :return: Amount of (signed) force to apply
    """

    # MODIFY THIS CODE!

    # if cur_x < target_x:
    #     force = 100
    # else:
    #     force = 0

    kp = 0.1

    error = target_x - cur_x
    force = kp * error
    return force


if __name__ == "__main__":
    sim = locomotive_sim.Animation(get_force)
    sim.run()