#Agentframework.py

#Import libraries
import random

# Class agent definition with a variation
# Agent() properties; move, eat, share
class Agent():
    
    #creates the location of the agent
    def __init__ (self, environment, agents):
        '''creates the _init_ using the random import'''
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents
      
    #moves the agent by 1
    def move(self):
        '''Takes in self agent, and moves it'''
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
    
    #defines the eat function 
    def eat(self): 
        '''Takes in self agent, as an eat function'''
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
   
    # Shares inofmration with local agents
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents: 
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                 average = (self.store + agent.store) / 2
                 self.store = average
                 agent.store = average
    # Distance between the agents
    def distance_between(self, agent):
        '''Defines the distance between the agents and returns as pythag sum'''
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
                 

    print(__init__.__doc__)
    print(move.__doc__)
    print(eat.__doc__)
    print(distance_between.__doc__)
    
    
            

    
 
        
        

        
    
    