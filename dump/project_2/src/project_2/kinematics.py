import math

def forward(p, a, rd):
  (x,y,theta) = p
  (vl,vr,t) = a
  (axle_length, wheel_radius, max_speed) = rd

  return 0, 0, 0

def inverse(p0, p1, rd):
  (x0,y0,theta0) = p0
  (x1,y1,theta1) = p1
  (axle_length, wheel_radius, max_speed) = rd
    
  return []
