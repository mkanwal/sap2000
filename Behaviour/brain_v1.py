# Python default libraries
from random import *
from math import *
import pdb
from abc import ABCMeta, abstractmethod

# Local imports
from Helpers import helpers
# constants for simulation
from variables import BEAM, ROBOT,PROGRAM, VISUALIZATION
# constants for construction
from construction import HOME,CONSTRUCTION
# constants for behaviour
from Behaviour import constants as BConstants

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Implementation of robot brain. 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class BaseBrain:
  __metaclass__=ABCMeta
  @abstractmethod
  def __init__(self, Robot):
    # access to the robot body; functions are detailed in the documentation file
    # Code for the robot can be found in /World/robot.py

  @abstractmethod
  def performDecision(self):
    '''
    This function is called during the simulation before the act function is called.
    The brain should perform the task of deciding what actions to perform next.

    In particular, note that self.Body.addToMemory(key,value) allows for storing 
    information in the Body. 
    '''
    pass

  @abstractmethod
  def performAction(self):
    '''
    Perform the action that should occur after each timestep. This actions should be 
    based on the information currently stored in memory, as the robot has to access
    to data from the structure. DO NOT ATTEMPT to access the SAP 2000 API; there
    are no results.
    '''
    pass


class Brain(BaseBrain):
  def __init__(self, Robot):
    super().__init__(Robot)
    self.Body = Robot
    self.addToMemory('decision',None)
    self.addToMemory('location',self.Body.getLocation())
    self.addToMemory('construction_angle',90)

  def performDecision(self):
    #pdb.set_trace()
    self.decide()

  def performAction(self):
    #pdb.set_trace()
    self.act()

  ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  Brain Helper functions
  '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

  def decide(self):
    pass

  def act(self):
    if self.Body.num_beams == 0 and self.Body.getLocation()[2] == 0:
      self.pick_up_beam()
    else:
      direction = 90 if int(random()*2)==0 else 270
      move(direction)

  def move(self, angle):
    rad = radians(angle)
    direction = helpers.make_vector((0,0,0),(cos(rad),sin(rad),0))
    new_location = helpers.sum_vectors(self.Body.getLocation(), helpers.scale( \
      self.Body.step, helpers.make_unit(direction)))
    self.Body.changeLocalLocation(new_location)

  # Called whenever robot does not have a beam.
  def pick_up_beam(self, num_beams = ROBOT['beam_capacity']):
    if self.Body.num_beams != 0:
      self.goHome()
      self.Body.pickUpBeams(numBeams)

  def go_home(self):
    direction_home = helpers.make_vector(self.Body.getLocation(), HOME['center'])
    new_location = helpers.sum_vectors(self.Body.getLocation(), helpers.scale( \
      self.Body.step, helpers.make_unit(direction_home)))
    self.Body.changeLocalLocation(new_location)





















