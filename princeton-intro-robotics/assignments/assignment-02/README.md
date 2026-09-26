# Assignment 2 — RRT implementation and hardware deployment

> Course: Princeton ROB 345/549, Introduction to Robotics, Fall 2026
>
> Public release checked: 2026-09-26
>
> Course page: <https://irom-lab.princeton.edu/intro-to-robotics/>
>
> Coding repository: <https://github.com/Princeton-Introduction-to-Robotics/F2026>
>
> Official assignment link: <https://github.com/Princeton-Introduction-to-Robotics/F2026/blob/main/Lab2.ipynb>

## Downloaded material

- [Lab 2 notebook](Lab2.ipynb): the unmodified public notebook for RRT implementation and Crazyflie deployment.

The course page currently links Assignment 2 as a GitHub notebook rather than as a separate PDF. Check the upstream repository for revisions before beginning work.

## Scope

The notebook has four parts:

1. **Crazyflie setup:** connect to the drone, configure the radio channel, and verify the Crazyflie software stack.
2. **RRT implementation (60 points):** implement configuration and edge collision checks, random sampling, nearest-vertex search, `extend`, the main RRT loop, and parent-pointer backtracking.
3. **Environment measurement (10 points):** measure the current drone cage, represent its rectangular workspace and circular obstacles, inflate obstacles with a safety buffer, and plan a trajectory in the measured coordinates.
4. **Hardware implementation (30 points):** convert the RRT path into position setpoints and fly from the marked start to the marked goal as a team.

The obstacle layout changes between semesters and netted areas, so the notebook's placeholder measurements must be replaced with current measurements from the lab. Coordinates must be expressed in meters and in the Crazyflie's frame: positive $x$ is forward and positive $y$ is left when standing behind the drone.

## Local software and hardware notes

The Assignment 1 [`uv` environment](../assignment-01/UV_SETUP.md) contains the numerical and notebook packages needed for the algorithm portions. The official notebook additionally calls for Crazyflie packages such as `cflib`, `libusb`, and `cfclient`; follow its platform-specific installation instructions before attempting the hardware cells. A Crazyradio, compatible Crazyflie, and the course's required decks are needed for flight.

Do not run the radio or flight cells without the drone, netted area, safety glasses, and staff-approved lab procedure. The notebook's instructions are course material, not a substitute for current lab safety guidance.

## Submission reminder

The notebook says that one team member should submit the completed notebook and a video showing a successful flight to the Lab 2 Gradescope assignment. Keep submitted work original and follow the current syllabus or Canvas policy if it differs from this public snapshot.
