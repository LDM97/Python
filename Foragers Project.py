
# coding: utf-8

# In[2]:

#Plants

class plant(object):
    def __init__(self, energy, x, y):
        self.energy=5.0
        self.growthrate=0.2
        self.maxenergy=10
        self.x=x
        self.y=y
    def growth(self):
        self.energy=self.energy+self.growthrate*self.energy*((self.maxenergy-self.energy)/self.maxenergy)
        return self.energy

#Forager

class forager(object):
    def __init__(self, energy, x, y, c):
        self.energy=50
        self.metabolism=2.0
        self.minenergy=0
        self.x=x
        self.y=y
        self.consumptionrate=c
    def life(self):
        self.energy=self.energy-self.metabolism

#Predator

class predator(object):
    def __init__(self,energy, x, y, c):
        self.energy=50
        self.metabolism=2.0
        self.minenergy=0
        self.x=x
        self.y=y
        self.consumptionrate=c
    def life(self):
        self.energy=self.energy-self.metabolism

from random import randrange
class world(object):
    
    def __init__(self, size = 25):
        self.size = size
        self.plants = list()
        for x in range (self.size):
            row = list()
            self.plants.append(row) 
            for y in range(self.size):
                column = list()
                row.append(column)
        
        for i in range(0,self.size):
            for j in range(0,self.size):
                self.plants[i][j]=plant(3, x, y)
                
        self.foragers = list()
        self.predators = list()
        
        self.positions1 = list()
        for x in range (self.size):
            row = list()
            self.positions1.append(row)
            for y in range(self.size):
                column = list()
                row.append(column)
                self.positions1[x][y] = False
                
        self.positions2 = list()
        for x in range (self.size):
            row = list()
            self.positions2.append(row)
            for y in range(self.size):
                column = list()
                row.append(column)
                self.positions2[x][y] = 2
                
    def addforagers(self, n, consumption_rate):        
        for _ in range(0,n):
            while(True):
                x = randrange(0,self.size)
                y = randrange(0,self.size)
                if self.positions1[x][y] == False:
                    break
            self.foragers.append(forager(50, x, y, consumption_rate))
            self.positions1[x][y] = True
            
    def addpredators(self, n, consumption_rate):
        for _ in range(0,n):
            while(1):
                x = randrange(0,self.size)
                y = randrange(0,self.size)
                if self.positions2[x][y] == 2:
                    break
            self.predators.append(predator(50, x, y, consumption_rate))
            self.positions2[x][y] = 1
            
    def movement(self):
        for f in self.foragers:
            x = f.x
            y = f.y
            
            # check that my neighbours are not all full
            count = 0
            for x in range(f.x-1,f.x+2):
                for y in range(f.y-1,f.y+2):
                    
                    if x < 0:
                        x = self.size-1
                    if x >= self.size:
                        x = 0
                        
                    if y < 0:
                        y = self.size-1
                    if y >= self.size:
                        y = 0
                        
                    
                    if self.positions1[x][y] == True:
                        count = count + 1
                        
            if count == 9:
                continue
           
            # let's move the forager to an empty cell
            
            # generate random neighbour x y coords
                     
            while(True):
                x = randrange(f.x-1, f.x+2)
                y = randrange(f.y-1, f.y+2)
                if x < 0:
                    x = self.size-1
                if x >= self.size:
                    x = 0
                        
                if y < 0:
                    y = self.size-1
                if y >= self.size:
                    y = 0
                if self.positions1[x][y] == False:
                    break
           
            # now have valid empty x y position
            # move the forager to this position
            self.positions1[f.x][f.y] =False
            f.x = x
            f.y = y            
            self.positions1[x][y]= True
            
    def predmovement(self):
        for p in self.predators:
            x = p.x
            y = p.y
            
            # check that my neighbours are not all full
            count = 0
            for x in range(p.x-1,p.x+2):
                for y in range(p.y-1,p.y+2):
                    
                    if x < 0:
                        x = self.size-1
                    if x >= self.size:
                        x = 0
                        
                    if y < 0:
                        y = self.size-1
                    if y >= self.size:
                        y = 0
                        
                    
                    if self.positions2[x][y] == 2:
                        count = count + 1
                        
            if count == 9:
                continue
           
            # let's move the forager to an empty cell
            
            # generate random neighbour x y coords
                     
            while(1):
                x = randrange(p.x-1, p.x+2)
                y = randrange(p.y-1, p.y+2)
                if x < 0:
                    x = self.size-1
                if x >= self.size:
                    x = 0
                        
                if y < 0:
                    y = self.size-1
                if y >= self.size:
                    y = 0
                if self.positions2[x][y] == 2:
                    break
           
            # now have valid empty x y position
            # move the forager to this position
            self.positions2[p.x][p.y] =2
            p.x = x
            p.y = y            
            self.positions2[x][y]= 1
    
    def metabolism(self):
        for f in self.foragers:
            x = f.x
            y = f.y
            f.life()
            if f.energy <0:
                self.foragers.remove(f)
                self.positions1[x][y]=False
                
    def predmetabolism(self):
        for p in self.predators:
            x = p.x
            y = p.y
            p.life()
            if p.energy <0:
                self.predators.remove(p)
                self.positions2[x][y]=2
            
    
    def eating(self):
        for f in self.foragers:
            x = f.x
            y = f.y
            f.energy += self.plants[x][y].energy * f.consumptionrate
            self.plants[x][y].energy=self.plants[x][y].energy * (1-f.consumptionrate)
            
    def predeating(self): 
        for p in self.predators:
            x = p.x
            y = p.y
            # if forager is on the same coordinate as the predator then the predator should eat the forager
            if self.positions1[x][y]==True:
                for f in self.foragers:
                    if f.x == p.x and f.y == p.y:
                        break
                        
                p.energy=f.energy+p.energy
                f.energy=0
            
    def reproduction(self):
        for f in self.foragers:
            if f.energy > 60:
                x = f.x
                y = f.y

                count = 0
                for x in range(f.x-1,f.x+2):
                    for y in range(f.y-1,f.y+2):

                        if x < 0:
                            x = self.size-1
                        if x >= self.size:
                            x = 0

                        if y < 0:
                            y = self.size-1
                        if y >= self.size:
                            y = 0


                        if self.positions1[x][y] == True:
                            count = count + 1

                if count == 9:
                    continue

                while(True):
                    x = randrange(f.x-1, f.x+2)
                    y = randrange(f.y-1, f.y+2)
                    if x < 0:
                        x = self.size-1
                    if x >= self.size:
                        x = 0

                    if y < 0:
                        y = self.size-1
                    if y >= self.size:
                        y = 0
                    if self.positions1[x][y] == False:
                        break

                energy = f.energy/2.0
                self.foragers.append(forager(energy,x, y, f.consumptionrate))
                f.energy = f.energy/2.0
                self.positions1[x][y] = True
                
    def predreproduction(self):
        for p in self.predators:
            if p.energy > 120:
                x = p.x
                y = p.y

                count = 0
                for x in range(p.x-1,p.x+2):
                    for y in range(p.y-1,p.y+2):

                        if x < 0:
                            x = self.size-1
                        if x >= self.size:
                            x = 0

                        if y < 0:
                            y = self.size-1
                        if y >= self.size:
                            y = 0


                        if self.positions2[x][y] == 1:
                            count = count + 1

                if count == 9:
                    continue

                while(True):
                    x = randrange(p.x-1, p.x+2)
                    y = randrange(p.y-1, p.y+2)
                    if x < 0:
                        x = self.size-1
                    if x >= self.size:
                        x = 0

                    if y < 0:
                        y = self.size-1
                    if y >= self.size:
                        y = 0
                    if self.positions2[x][y] == 2:
                        break

                energy = p.energy/2.0
                self.predators.append(predator(energy,x, y, p.consumptionrate))
                p.energy = p.energy/2.0
                self.positions2[x][y] = 1
                
    def update(self):
        for i in range(0,self.size):
            for j in range(0,self.size):
                self.plants[i][j].growth()
        self.eating()
        self.predeating()
        self.metabolism()
        self.predmetabolism()
        self.reproduction()
        self.predreproduction()
        self.movement()       
        self.predmovement()
        
import random
import tkinter as tk

class ForagerApp(tk.Frame):
    def __init__(self, size, generation_interval_ms = 300):
        self.generation_interval_ms = generation_interval_ms
        self.widgets = dict()
        self.root = tk.Tk()
        self.size = size
        tk.Frame.__init__(self, self.root)
        self.grid()
        self.world = world(size)
        self.world.addforagers(15, 0.4)
        self.world.addpredators(15, 0.25)
        self.foragercount = list()
        self.predatorcount = list()

        for x in range(0,self.size):
            for y in range(0,self.size):
                bg = "black"
                widget = tk.Label(height = 1, width = 2, bg = bg, relief = "ridge")
                widget.grid(column = x, row = y)
            
                p = self.world.plants[x][y].energy
                color = int(p/10.0*256)
                color = "#%02x%02x%02x" % (0,color,0)
                #widget[(x,y)].configure(bg = color)
                self.widgets[(x, y)] = widget
                
        for f in self.world.foragers:
            self.widgets[(f.x,f.y)].configure(bg = "blue")
            
        for p in self.world.predators:
            self.widgets[(p.x,p.y)].configure(bg = "red")

        self.root.after(self.generation_interval_ms, self.draw)

    def draw(self):
        """ Draws the new generation. """
        for x in range(0,self.size):
            for y in range(0,self.size):
                for f in self.world.foragers:
                    self.widgets[(f.x,f.y)].configure(bg = "blue")
                for p in self.world.predators:
                    self.widgets[(p.x,p.y)].configure(bg = "red")
                else:
                    p = self.world.plants[x][y].energy
                    color = int(p/10.0*256)
                    color = "#%02x%02x%02x" % (0,color,0)
                    self.widgets[(x,y)].configure(bg = color)
        
        self.foragercount.append(len(self.world.foragers))
        self.predatorcount.append(len(self.world.predators))
        self.world.update()
        self.root.after(self.generation_interval_ms, self.draw)

if __name__ == "__main__":

    app = ForagerApp(size=15)
    app.mainloop()


# In[3]:

app = ForagerApp(size = 15)
app.mainloop()


# In[ ]:



