import cv2
import numpy as np
import os
        
##
#Class to represent a group of contours
##
class cont_group(object):
        
    def __init__(self, contours):
        self.contours = contours
        self.n_per_clust = 0
        self.makeHierarchies(len(contours) - 1);
    
    def makeHierarchies(self, num_holes):
        self.hierarchies = []
        if num_holes == 0:
            self.hierarchies.append(np.array([-1, -1, -1, -1]))
        else:
            self.hierarchies.append(np.array([-1, -1, 1, -1]))
            firstElem = 0
            secondElem = 0
            for i in range(1, num_holes+1):
                if i == num_holes:
                    firstElem = -1
                else:
                    firstElem = i + 1
                if i == 1:
                    secondElem = -1
                else:
                    secondElem = i - 1
                self.hierarchies.append(np.array([firstElem, secondElem, -1, 0]))
        self.hierarchies = np.array(self.hierarchies)
