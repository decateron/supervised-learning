from math import sqrt


def  manhattan(x, z):
    # Also known as taxicab metric, rectilinear distance, snake distance
    # city block distance.
    if len(x) != len(z):
        raise ValueError("len(x) != len(z). To compute the Manhattan Distance the length of objects must be the same")

    total = 0

    for i in range(len(x)):
        total += abs(x[i] - z[i])

    distance = total
    return distance



def eucledean(x, z):
    if len(x) != len(z):
        raise ValueError("len(x) != len(z). To compute the Eucledean Distance the length of objects must be the same")

    total = 0

    for i in range(len(x)):
        total += pow(x[i] - z[i], 2)
    
    distance = sqrt(total)
    return distance  



def minkowski(x, z, p=3):
    if len(x) != len(z):
        raise ValueError("len(x) != len(z). To compute the Minkowski Distance the length of objects must be the same")

    total = 0

    for i in range(len(x)):
        total += abs(pow(x[i] - z[i], p))

    distance = pow(total, 1/p)  # sqrt(total, p)
    return distance



def discrete(x, z):
    if len(x) != len(z):
        raise ValueError("len(a) != len(b). To compute the Discrete Distance the length of objects must be the same")

    total = 0

    for i in range(len(x)):  
        if x[i] == x[i]:    # if a[i] != b[i]:
            total += 0      #   total += 1
        else:
            total += 1
    
    distance = total
    return distance

def chebyshev(x, z):
    if len(x) != len(z):
        raise ValueError("len(x) != len(z). To compute the Chebyshev Distance the length of objects must be the same")

    feature_max_dist = -1
    for i in range(len(x)):
        feature_dist = abs(x[i] - z[i])
        
        if feature_dist > feature_max_dist:
            feature_max_dist = feature_dist
    
    distance = feature_max_dist
    return distance

chessboard = chebyshev


        

        

