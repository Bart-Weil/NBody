import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

from PIL import Image, ImageDraw
imgx = 1000
imgy = 1000
image = Image.new("RGB", (imgx, imgy))
draw = ImageDraw.Draw(image)

G = 6.6743*10**(-11)

fig, ax = plt.subplots()

def NGrav(m1, m2, pos1, pos2):

    maglist = []

    for dim in range(len(pos1)):

        maglist.append((pos1[dim]-pos2[dim])**2)

    r = (sum(maglist))**(1/2)

    return (G*m1*m2)/r**2

bodieslist = []

class Body:

    def __init__(self, pos, vel, mass):

        self.pos = pos
        self.vel = vel
        self.mass = mass

        self.force = []
        self.accel = []

        bodieslist.append(self)

    def update(self):

        self.force = []
        self.accel = []

        rlist = []
        rlistunit = []
        forcelist = []

        dimension = len(self.vel)

        for bodies in bodieslist:

            if bodies != self:

                rlistbody = []

                for component in range(len(bodies.pos)):

                    rlistbody.append(bodies.pos[component]-self.pos[component])

                rlist.append(rlistbody)

            else:

                rlist.append(None)

        for bodies in bodieslist:

            if bodies != self:

                maglist = []
                runit = []

                for component in range(len(bodies.pos)):

                    maglist.append((self.pos[component] - bodies.pos[component])**2)

                mag = (sum(maglist))**(1/2)

                for component in range(len(bodies.pos)):

                    runit.append(rlist[bodieslist.index(bodies)][component]/mag)

                rlistunit.append(runit)

            else:

                rlistunit.append(None)

        for bodies in range(len(bodieslist)):

            if bodieslist[bodies] != self:

                forcebody = []

                for component in rlistunit[bodies]:

                    forcebody.append(component * NGrav(self.mass, bodieslist[bodies].mass, self.pos, bodieslist[bodies].pos))

                forcelist.append(forcebody)

            else:

                forcelist.append(None)

        for dim in range(dimension):

            resforcelist = []

            for body in forcelist:

                if body != None:

                    resforcelist.append(body[dim])

            self.force.append(sum(resforcelist))

        for component in self.force:

            self.accel.append(component/self.mass)

    def pos_vel_update(self, timestep):

        vprime = []

        for component in range(len(self.accel)):

            vprime.append(self.vel[component]+self.accel[component]*timestep)

        for component in range(len(self.vel)):

            self.pos[component] += 1/2 * (self.vel[component] + vprime[component]) * timestep

        self.vel = vprime

step = 50000


p1 = Body([0, 0], [0, 0], 1*10**24)
p2 = Body([100000, 100000], [-0.1, 0], 1*10**24)
p3 = Body([200000, 0], [0, 0], 1*10**24)
p4 = Body([80000,50000], [0,0], 1*10**10)

for i in range(500):

    #p1.update()
    #p2.update()
    #p3.update()
    p4.update()

    #p1.pos_vel_update(step)
    #p2.pos_vel_update(step)
    #p3.pos_vel_update(step)
    p4.pos_vel_update(step)


    plt.plot(p1.pos[0], p1.pos[1], 'r.')
    plt.plot(p2.pos[0], p2.pos[1], 'r.')
    plt.plot(p3.pos[0], p3.pos[1], 'r.')
    plt.plot(p4.pos[0], p4.pos[1], 'b.')

    dig = '0'*(len(str(7500))-len(str(i)))+str(i)

    print(dig)

plt.show()



'''angle1 = (math.atan(p1.pos[1]/p1.pos[0])*(360/math.pi))%360
angle2 = (math.atan(p2.pos[1]/p2.pos[0])*(360/math.pi))%360

posarr[initangle1].append([angle1, angle2])'''

'''del p1
del p2'''

    #print(posarr)

'''for coorx in range(len(posarr)):
    for coory in range(len(posarr[coorx])):

        angle1 = posarr[coorx][coory][0]
        angle1 = posarr[coorx][coory][1]

        image.putpixel((coorx, coory), (0, int((angle1 / 360) * 255), int((angle2 / 360) * 255)))


#image.putpixel((0, 0), (0, int((angle1/360)*255), int((angle2/360)*255)))
image.show()'''

