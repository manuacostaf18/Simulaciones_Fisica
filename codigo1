import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math


class Projectile:
    # class variables for simulation time and number of time slices
    sim_time, time_slices = None, None
    
    def __init__(self, x0, y0, v0, alpha0):
        # projectile initial position and velocity
        self.x, self.y = x0,y0
        self.vx = v0*np.cos(np.radians(alpha0))
        self.vy = v0*np.sin(np.radians(alpha0))
        self.angle = alpha0
        
        # time interval to be simulated
        self.t = np.linspace(0., self.sim_time, self.time_slices)

        # maximum distance and height, time of flight to ground
        self.t_max = 2. * v0 * math.sin(math.radians(alpha0)) / grav_
        self.x_max = v0 ** 2 * math.sin(2. * math.radians(alpha0)) / grav_
        self.y_max = (v0 * math.sin(math.radians(alpha0))) ** 2 / (2. * grav_)

        # rounding up
        self.x_max, self.y_max = math.ceil(self.x_max), math.ceil(self.y_max)

    def kinematics(self, ax, ay):
        # kinematic equations: position and velocity
        self.x += (self.vx * self.t) + (1/2)*ax*(self.t*self.t)
        self.y += (self.vy* self.t) + (1/2)*ay*(self.t*self.t)
        
        self.vx += ax*self.t
        self.vy += ay*self.t
    
    # def get_xtrajectory(self):
    #     # returns values of x(t) and y(t)
    #     return self.x
    #
    # def get_ytrajectory(self):
    #     # returns values of x(t) and y(t)
    #     return self.y

    def get_xmax(self):
        return self.x_max

    def get_ymax(self):
        return self.y_max

    def get_trajectory(self):
        # returns values of x(t) and y(t)
        return self.x, self.y

    def get_time(self):
    	return self.t

    def get_angle(self):
    	return self.angle


class Animator:
    # choose your favorite colors!
    cls = ['green', 'red', 'blue', 'cyan', 'magenta', 'black','orange','grey','yellow','pink']
    
    def __init__(self, objs):
        # objects to be animated and its total number
        self.artists = objs
        self.number = len(self.artists)
        
        # instance variables to None; properly set in set_animation
        self.fig = self.ax = self.line = self.point = None
        self.time_template = self.time_text = None
        self.xdata = self.ydata = None
    
    def set_animation(self):
        # plot setup: axis, labels, title, grid, etc.

        xmax = max([self.artists[i].get_xmax() for i in range(self.number)])
        ymax = max([self.artists[i].get_ymax() for i in range(self.number)])


        self.fig = plt.figure()
        self.ax = plt.axes(autoscale_on=False, xlim=(-1, xmax+1), ylim=(-1, ymax+1))
        self.ax.set(xlabel='x position', ylabel='y position', title='Projectile motion')
        # ax.set_aspect('equal')
        self.ax.grid()

        # line points setup, time template, points on top of axes

        self.point = [self.ax.plot([], [], 'o-', c=self.cls[i], lw=0) for i in range(self.number)]
        self.line = [self.ax.plot([], [], ls='--', lw=2, c=self.cls[i]) for i in range(self.number)]

        angles = []
        for i in range(self.number):
            artist = self.artists[i]
            angles.append(artist.get_angle())
        self.ax.legend(["Angle = " + str(i) for i in angles])
        # line points setup, time template, points on top of axes



    def init(self):
        return self.line, self.time_text
    
    def animate(self, idx):

        for i in range(self.number):
            artist = self.artists[i]
            self.xdata, self.ydata = artist.get_trajectory()
            if self.ydata[idx] >= 0.:
                self.line[i][0].set_data([self.xdata[0:idx]], [self.ydata[0:idx]])
                self.point[i][0].set_data([self.xdata[idx]], [self.ydata[idx]])
        return self.line, self.point, self.time_text
    
    
    def run_animation(self, inval=10, rep=True):
        # set up to perform animation
        ani = animation.FuncAnimation(self.fig, self.animate,
                                      range(len(self.artists[0].y)),
                                      repeat=rep, interval=inval,
                                      init_func=self.init)
        plt.show()



# physical constants (in arbitrary units)
grav_ = 1
drag_ = .0 * grav_
params = [val for val in range(15, 91, 15)]


# initial position and velocity; acceleration
x0, y0 = 0., 0.
v0, alpha0 = 5, params
ax, ay = -drag_, -drag_ - grav_
print("parameters =", params)


# calculate simulation time and set time slices
sim_time_max = max(2. * np.array(v0) * np.sin(np.radians(alpha0)) / grav_)
print("sim time =", sim_time_max)

Projectile.sim_time = sim_time_max
Projectile.time_slices = 160
print("time slices =", Projectile.time_slices)


# create all projectiles to animate
balls = [Projectile(x0, y0, v0, val) for val in alpha0]

# generate their respective trajectories
[ball.kinematics(ax, ay) for ball in balls]

# print some relevant values to check correctenessanimate
#[print(ball.get_maxes()) for ball in balls]
#[print(ball.get_trajectory()) for ball in balls]


# create animator handle object for animation
framer = Animator(balls)

# set up animation
framer.set_animation()

# carry out animation (default parameters)
framer.run_animation(inval=1000*Projectile.sim_time/Projectile.time_slices)

# print some relevant values to check correcteness
#[print(ball.get_maxes()) for ball in balls]
#[print(ball.get_trajectory()) for ball in balls]
