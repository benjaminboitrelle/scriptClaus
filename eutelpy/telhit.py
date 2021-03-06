'''
Created on Jun 8, 2015

@author: kleinwrt
'''

## \file
# telescope event 

import numpy as np

## telescope hit.
class TelHit(object):
  
  ## constructor.
  #
  # @param[in] det      detector
  # @param[in] index    index
  # @param[in] planeID: plane ID
  # @param[in] pos      (local) position 
  # @param[in] cluster  cluster information (optional)
  #
  def __init__(self, det, index, planeID, pos, cluster):
    p = planeID
    #p = [3, 2, 0, 1, 4, 5][planeID%128] # run 680
    p = [128, 129, 0, 2, 3, 5][planeID%128] # run 680
    '''
    # get plane ID from Z position (for run 20904)
    if pos[2] < 75.:
      p = 0
    elif pos[2] < 225.:
      p = 1
    elif pos[2] < 300.:
      p = 2
    elif pos[2] < 370.:
      p = 3
    elif pos[2] < 470.:
      p = 4
    else:
      p = 5
      
    # get plane ID from Z position (for FEI4-tel run 266)
    if pos[2] < 10.:
      p = 0
    elif pos[2] < 185.:
      p = 1
    elif pos[2] < 360.:
      p = 2
    elif pos[2] < 695.:
      p = 6
    elif pos[2] < 715.:
      p = 7
    elif pos[2] < 835.:
      p = 3
    elif pos[2] < 1010.:
      p = 4      
    else:
      p = 5
    '''
    ## detector plane ID
    self.__id = p
    # local position
    locPos = np.array(pos)
    locPos[2] = 0.
    ## global position
    self.__pos = det[self.__id].transformLocalToGlobal(locPos).tolist()
    ## used flag 
    self.__used = False 
    ## matches
    self.__matches = 0
    ## GBL label
    self.__label = 0
    ## index (in input hit collection)
    self.__index = index
    ## cluster information
    self.__cluster = cluster
    #print " hit ", p, self.__pos[0], self.__pos[1]


  ## Set GBL label.
  #
  # @param[in] l  label
  #
  def setLabel(self, l):
    self.__label = l  

  ## Get GBL label.
  def getLabel(self):
    return self.__label  
 
  ## Get GBL label.
  def getIndex(self):
    return self.__index  
            
  ## Add match
  def addMatch(self):
    self.__matches += 1
    
  ## Get matches
  def getMatches(self):
    return self.__matches

  ## Set use flag.
  def setUsed(self):
    self.__used = True

  ## Get use flag.  
  def getUsed(self):
    return self.__used    
 
  ## Get X coordinate.
  def getX(self):
    return self.__pos[0]
  
  ## Get Y coordinate.
  def getY(self):
    return self.__pos[1]
    
  ## Get Z coordinate.
  def getZ(self):
    return self.__pos[2]

  ## Get coordinates.
  def getPos(self):
    return self.__pos
  
  ## Get plane.
  def getPlane(self):
    return self.__id
    
  ## Get cluster information
  def getCluster(self):
    return self.__cluster  
        
  ## Dump.
  def dump(self):
    print " id ", self.__id, " pos ", self.__pos
