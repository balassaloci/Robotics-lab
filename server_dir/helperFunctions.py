
from math import sin, cos, acos, radians, exp, sqrt, pi


# CONSTANTS TO CALCULATE PROBABILITY
MAX_EST_DIST = 300
K = 0.01
def SONAR_VAR(dist):
    return dist*5/40 #0.2777777778/40 
THRESH = 0.20

####################################

def frontalDistance(A, B, R):

    top = (B[1]-A[1])*(A[0]-R[0]) - (B[0]-A[0])*(A[1]-R[1])
    bottom = (B[1]-A[1])*cos(R[2]) - (B[0]-A[0])*sin(R[2])

    try:
        return top/bottom
    except ZeroDivisionError:
        pass
    
def intersection(R, m):
    x = R[0] + m * cos(R[2])
    y = R[1] + m * sin(R[2])

    return x, y

def valBetween(a, b, x):
    if a <= x <= b:
            return True
    elif a >= x >= b:
            return True

    return False

def isOnWall(A, B, intsect):
    return valBetween(A[0], B[0], intsect[0]) and \
            valBetween (A[1], B[1], intsect[1])

def wallInFront(A, B, intsect, m):
    return isOnWall(A, B, intsect) and m >= 0

def likelihood(z, m):
    p = (-(z-m)**2)/(2*0.527**2)
    return exp(p)


def calcEstTruth(x,y,t, map_list):
    dist_list = []
    for wall in map_list:
        
        try:
            Ax,Ay,Bx,By = wall
            #formula directly from slide 18 of lecture 5
            m = ((By-Ay)*(Ax-x)-(Bx-Ax)*(Ay-y)) / ((By-Ay)*cos(radians(t))-(Bx-Ax)*sin(radians(t)))
            
            b = acos( (cos(radians(t))*(Ay-By)+sin(radians(t))*(Bx-Ax)) / sqrt((Ay-By)**2 + (Bx-Ax)**2) )
            
            if m > 0 and m < MAX_EST_DIST: # and b <= THETA_THRES and b >= -THETA_THRES :
                new_pos = (x+m*cos(radians(t)), y+m*sin(radians(t)), t)

                withinX = ((new_pos[0] <= Bx+THRESH) and (new_pos[0] >= Ax-THRESH)) or ((new_pos[0] <= Ax+THRESH) and (new_pos[0] >= Bx-THRESH))
                withinY = ((new_pos[1] <= By+THRESH) and (new_pos[1] >= Ay-THRESH)) or ((new_pos[1] <= Ay+THRESH) and (new_pos[1] >= By-THRESH))

                if withinX and withinY:
                    dist_list.append(m)
        except ZeroDivisionError:
            pass
        
    return min(dist_list)

def calculate_likelihood(est_dist, z):    
    if est_dist is not None:
        exponent = ((z-est_dist)**2)/(2*SONAR_VAR(est_dist))
        p = exp(-exponent)/sqrt(2*pi*SONAR_VAR(est_dist)) + K
        return p
    return 0
    
