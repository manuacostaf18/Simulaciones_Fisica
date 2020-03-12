import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math

class Particle:
  #m, t, x, y, vx, vy, force
  def __init__(self, m0=1., t0=0., x0=0., y0=0., v0=0., alpha0=0., name):
    self.m = m0
    self.t = t0
    self.x, self.y = x0, y0
    self.vx = v0 * np.cos(np.radians(alpha0))
    self.vy = v0 * np.sin(np.radians(alpha0))
    self.force = None
    self.name = name
    
  def __str__(self):
    #retornar nombre, posicion, tiempo, velocidad 
    title = "Particle state\n"
    nom = "Particle: {}".format(self.name)
    m_t = "m = {}, t = {}\n".format(self.m, self.t)
    pos = "r = ({:4f}, {:4f})\n".format(self.x, self.y)
    vel = "v = ({:4f}, {:4f})\n".format(self.vx, self.vy)
    string = title + m_t + pos + vel 
    return string

  def get_state(self):
    return self.x, self.y, self.vx, self.vy, self.t
    
  def get_force(self, netforce):
    self.force = netforce
  
