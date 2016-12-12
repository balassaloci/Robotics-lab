def getStraightLine(bot_pos, dist):
    old_x, old_y, old_theta = bot_pos
    x = old_x + (dist + random.gauss(0.0, 0.1)) * cos(radians(old_theta))
    y = old_y + (dist + random.gauss(0.0, 0.1)) * sin(radians(old_theta))
    theta = old_theta + random.gauss(0.0, 0.1)
    return x, y, theta

def getRotation(bot_pos, angle):
    old_x, old_y, old_theta = bot_pos
    x = old_x
    y = old_y
    theta = old_theta - angle + random.gauss(0.0, 0.1)
    return x, y, theta

def bunchOfEndpoints(bot_pos):
    all_particles = []
    starting_pos = bot_pos
    for _ in range(20):
        bot_pos = starting_pos
        all_particles.append(starting_pos)
        for _ in range(5):
            bot_pos = getStraightLine(bot_pos, 10)
            all_particles.append(bot_pos)
        bot_pos = getRotation(bot_pos, -90)
        all_particles.append(bot_pos)

    print("drawParticles:"  + str(all_particles))