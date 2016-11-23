#!/usr/bin/env python
# By Jacek Zienkiewicz and Andrew Davison, Imperial College London, 2014
# Based on original C code by Adrien Angeli, 2009


import robolib as rb
import random
import os
import math


# Initialize bot
bot = rb.robolib()


# Location signature class: stores a signature characterizing one location
class LocationSignature:
    def __init__(self, no_bins = 360):
        self.sig = [0] * no_bins
        
    def print_signature(self):
        for i in range(len(self.sig)):
            print self.sig[i]

# --------------------- File management class ---------------
class SignatureContainer():
    def __init__(self, size = 5):
        self.size      = size; # max number of signatures that can be stored
        self.filenames = [];
        
        # Fills the filenames variable with names like loc_%%.dat 
        # where %% are 2 digits (00, 01, 02...) indicating the location number. 
        for i in range(self.size):
            self.filenames.append('loc_{0:02d}.dat'.format(i))

    # Get the index of a filename for the new signature. If all filenames are 
    # used, it returns -1;
    def get_free_index(self):
        n = 0
        while n < self.size:
            if (os.path.isfile(self.filenames[n]) == False):
                break
            n += 1
            
        if (n >= self.size):
            return -1;
        else:    
            return n;

    # Delete all loc_%%.dat files
    def delete_loc_files(self):
        print "STATUS:  All signature files removed."
        for n in range(self.size):
            if os.path.isfile(self.filenames[n]):
                os.remove(self.filenames[n])
            
    # Writes the signature to the file identified by index (e.g, if index is 1
    # it will be file loc_01.dat). If file already exists, it will be replaced.
    def save(self, signature, index):
        filename = self.filenames[index]
        if os.path.isfile(filename):
            os.remove(filename)
            
        f = open(filename, 'w')

        for i in range(len(signature.sig)):
            s = str(signature.sig[i]) + "\n"
            f.write(s)
        f.close();

    # Read signature file identified by index. If the file doesn't exist
    # it returns an empty signature.
    def read(self, index):
        ls = LocationSignature()
        filename = self.filenames[index]
        if os.path.isfile(filename):
            f = open(filename, 'r')
            for i in range(len(ls.sig)):
                s = f.readline()
                if (s != ''):
                    ls.sig[i] = float(s)
            f.close();
        else:
            print "WARNING: Signature does not exist."
        
        return ls
        

def characterize_location(ls):
    ls.sig = bot.turn_poll(3)

    #step = 360/len(ls.sig)
    #for i in range(len(ls.sig)):
    #    reading = sum([float(bot.readUltrasound()) for j in range(3)])/3
    #    ls.sig[i] = reading
    #    print "angle:", i*step, ",depth:", reading
    #    bot.turn_sonar(step)
    #bot.turn_sonar(-360)



def compare_signatures(ls1, ls2):
    counter = 0.0
    
    for x in range(len(ls1.sig)):
        d = ls1.sig[x] - ls2.sig[x]
        if abs(d) < 3:
            counter += 1 
    
    return counter/len(ls1.sig)

def get_hist(data, resolution):
    max = 255.0
    min = 0.0

    hist = [0.0] * (resolution + 1)

    for x in data:
        mapped = (x - min) / max
        slot = int(mapped * resolution)
        if slot < 0 or slot > resolution:
            print("SLOT OUT OF RANGE: %i, x is: %f" % (slot, x))
        else:
            hist[slot] += 1

    return hist

def match_hist(a, b):
    diffs = 0.0
    dcount = 0.0
    d2count = 0.0
    d3count = 0.0

    for x in range(len(a)):
        d = a[x] - b[x]

        if abs(d) <= a[x] * 0.2:
            dcount += 1.0
        if abs(d) <= a[x] * 0.1:
            d2count += 1.0
        if abs(d) <= a[x] * 0.05:
            d3count += 1.0
 
        #d3count += 1.0
        diffs += d**2

    rms_err = math.sqrt(diffs)

    pmatch = dcount / float(len(a))
    p2match = d2count / float(len(a))
    p3match = d3count / float(len(a))

    print(pmatch, p2match, p3match)

    return p2match


def determine_angle_diff(ls1, ls2):
    comps = []
    highest = (0, 0)
    for step in range(len(ls2)):
        ls2_ = ls2[step + 1:] + ls2[:step]
        matchfact = compare_signatures(ls1, ls2_)
        if matchfact > highest[0]:
            highest = (matchfact, step)
    
    return highest
        
    
def compare_angle_invariant(ls1, ls2):
    resolution = 20
    a = get_hist(ls1, resolution)
    b = get_hist(ls2, resolution)
    err = match_hist(a, b)
    return err
    

# This function characterizes the current location, and stores the obtained 
# signature into the next available file.
def learn_location():
    idx = signatures.get_free_index();
    if (idx == -1): # run out of signature files
        print "\nWARNING:"
        print "No signature file is available. NOTHING NEW will be learned and stored."
        print "Please remove some loc_%%.dat files.\n"
        return

    ls = LocationSignature(180)
    characterize_location(ls)
    signatures.save(ls,idx)
    print "STATUS:  Location " + str(idx) + " learned and saved."

# This function tries to recognize the current location.
# 1.   Characterize current location
# 2.   For every learned locations
# 2.1. Read signature of learned location from file
# 2.2. Compare signature to signature coming from actual characterization
# 3.   Retain the learned location whose minimum distance with
#      actual characterization is the smallest.
# 4.   Display the index of the recognized location on the screen
def recognize_location():
    ls_obs = LocationSignature(180);
    characterize_location(ls_obs);

    # FILL IN: COMPARE ls_read with ls_obs and find the best match
    for idx in range(signatures.size):
        print "STATUS:  Comparing signature " + str(idx) + " with the observed signature."
        ls_read = signatures.read(idx);

        print("Angle diff: ", determine_angle_diff(ls_obs.sig, ls_read.sig))
        
        match = compare_signatures(ls_obs, ls_read)
        #match = compare_angle_invariant(ls_obs.sig, ls_read.sig)
        
        if match > 0.85:
            print "Location: waypoint", idx+1, "recognized"
        print "percent match within 3cm: %0.2f" % (match)


# Prior to starting learning the locations, it should delete files from previous
# learning either manually or by calling signatures.delete_loc_files(). 
# Then, either learn a location, until all the locations are learned, or try to
# recognize one of them, if locations have already been learned.

signatures = SignatureContainer(10);
#signatures.delete_loc_files()
'''
for i in range(5):
    print "learning location"
    learn_location();
'''
    
    
#recognize_location();































