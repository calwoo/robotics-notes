import math


def forward(p, a, rd):
    # starting pose
    (x, y, theta) = p
    # action (velocity on wheels + time to spin)
    (v_left, v_right, t) = a
    # robot characteristics
    (axle_length, wheel_radius, max_speed) = rd

    if v_left == v_right:
        # here, v_left = v_right, so straight line motion
        dx = v_avg * math.cos(theta) * t
        dy = v_avg * math.sin(theta) * t
        return x + dx, y + dy, theta

    v_avg = wheel_radius * (v_left + v_right) / 2.0
    angular_v = wheel_radius * (v_right - v_left) / axle_length
    dist_to_icc = axle_length / 2.0 * (v_right + v_left) / (v_right - v_left)
    icc = (x - dist_to_icc * math.sin(theta), y + dist_to_icc * math.cos(theta))

    ### integration directly doesn't work as expected
    # dx = v_avg / angular_v * math.sin(angular_v * t)
    # dy = v_avg / angular_v * (1.0 - math.cos(angular_v * t))
    # dtheta = wheel_radius * (v_right - v_left) * t / axle_length

    # # ending pose
    # return x + dx, y + dy, theta + dtheta

    # precompute
    cos = math.cos(angular_v * t)
    sin = math.sin(angular_v * t)

    end_x = cos * (x - icc[0]) - sin * (y - icc[1]) + icc[0]
    end_y = sin * (x - icc[0]) + cos * (y - icc[1]) + icc[1]
    end_theta = theta + angular_v * t
    
    # ending pose
    return end_x, end_y, end_theta
