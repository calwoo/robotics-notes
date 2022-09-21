"""
Simple locomotive simulator to experiment with moving an object to a target
location by applying forces.

Author: Nathan Sprague
"""
import time
import math
import tkinter as tk


class Locomotive(object):
    def __init__(self, x, slope):
        self.x = x
        self.speed = 0
        self.mass = 7  # kilograms
        self.slope = slope  # degrees
        self.mu = .05  # friction coefficient
        self.time = 0  # total time since simulation started.
        self.total_fuel = 0

    def update(self, force, dt):

        f_g_down = self.mass * 9.8
        f_g_track = math.sin(self.slope / 180.0 * math.pi) * f_g_down

        f_friction = (-math.cos(self.slope / 180.0 * math.pi) *
                      f_g_down * self.mu)

        f_total_wo_friction = force - f_g_track
        acceleration_wo_friction = f_total_wo_friction / self.mass
        new_speed_wo_friction = self.speed + acceleration_wo_friction * dt

        if new_speed_wo_friction < 0:
            f_friction = -f_friction

        accel_friction = f_friction / self.mass
        new_speed_w_friction = new_speed_wo_friction + accel_friction * dt

        if (new_speed_wo_friction >= 0) != (new_speed_w_friction >= 0):
            self.speed = 0  # Signs differ, friction can't make you go backward
        else:
            self.speed = new_speed_w_friction

        self.x += self.speed * dt

        self.total_fuel += abs(force) * dt

        self.time += dt


class Animation:

    def __init__(self, force_func, initial_x=200, target_x=450):
        """
        Initialize a train simulation.

        :param force_func: User-provided function that will be called to
        determine the amount of force to apply.  Must have the signature
            def force_func(target_x: float, current_x: float) -> float
        where the return value is a signed force.

        :param initial_x:  Starting locomotive position.
        :param target_x:   Target locomotive position.
        """
        self.force_func = force_func
        self.target_x = target_x

        self.root = tk.Tk()
        self.root.title("Super Great Locomotive Simulator")

        width = 900
        height = 100
        self.canvas = tk.Canvas(self.root, bg='white', width=width,
                                height=height)

        self.text = tk.StringVar()
        label = tk.Label(self.root, textvariable=self.text)
        label.configure(font='TkFixedFont')
        label.pack()

        self.canvas.pack()
        self.image = tk.PhotoImage(file="train.png")
        self.canvas.create_image((initial_x, self.image.height() / 2 + 5),
                                 image=self.image, tags=("train",))

        self.canvas.create_line(target_x, self.image.height() + 35,
                                target_x, self.image.height() + 5,
                                arrow=tk.LAST)

        self.train = Locomotive(initial_x, 0)
        self.last_time = time.time()
        self.last_x = self.train.x

    def _update_animation(self):
        cur_time = time.time()
        force = self.force_func(self.target_x, self.train.x)
        self.train.update(force, cur_time - self.last_time)
        self.canvas.move("train", self.train.x - self.last_x, 0)
        format_str = "position: {: 8.2f} \t speed: {: 8.2f} \t force: {: " \
                      "8.2f} \t total fuel: {: >8.2f}"
        self.text.set(format_str.format(self.train.x,
                                        self.train.speed, force,
                                        self.train.total_fuel))

        self.last_time = cur_time
        self.last_x = self.train.x
        self.canvas.after(20, self._update_animation)

    def run(self):
        """
        Start the simulation.
        """
        self._update_animation()
        self.root.mainloop()