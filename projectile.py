def update_state(t, x, v, a, dt=0.1):
    '''
    Update each parameter for the next time step.
    Args:
        t, x, v, a (float) : 
            time (s), position (m) and velocity (m/s) and acceleration (m/s2) value for this time step.
        dt (float) :
            time interval (s) for this small time step
    Returns:
        float, float, float : Updated values for t, h, v after this time step
    '''
    distance_moved = v*dt + (1/2)*a*(dt**2)
    v += a*dt
    t += dt

    x += distance_moved
    
    return t, x, v

def calculate_acceleration_y(v, k=0.0, mass=1.0, gravity=-9.81):
    '''
    Calculate the acceleration based on combined forces from gravity and 
    air resistance.
    Args:
        v (float) : 
            velocity (m/s) for this time step
        k (float) : 
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) : 
            Mass of the falling object. Needed if k > 0.
            Default = 1.0
        gravity (float) :
            Value for gravity to use when calculating gravitational force in m/s2.
            Default = -9.81
    Returns:
        float : accelaration calculated for this time step
    '''
    force_gravity = mass*gravity
    force_air = -sign(v)*k*v**2
    total_force = force_gravity + force_air
    a_y = total_force/mass
    
    return a_y

def calculate_acceleration_x(v, k=0.0, mass=1.0):
    '''
    Calculate the acceleration based on air resistance.
    Args:
        v (float) : 
            velocity (m/s) for this time step
        k (float) : 
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) : 
            Mass of the falling object. Needed if k > 0.
            Default = 1.0
    Returns:
       float : accelaration calculated for this time step
    '''
    force_air = -sign(v)*k*v**2
    a_x = total_air/mass
    
    return a_x


def flying_mass(initial_x_velocity, initial_y_velocity, k=0.0, mass=1.0, dt=0.1):
    '''
    Model a flying mass with separate x and y components of motion.
    
    Args:
        initial_x_velocity (float):
            Initial velocity in the x direction (m/s).
        initial_y_velocity (float):
            Initial velocity in the y direction (m/s).
        k (float) :
            Combined air resistance coefficient, based on F=-kv^2. 
            Should be positive.
            Default = 0.0  i.e. no air resistance
        mass (float) :
            Mass of the object. Only needed if k is not 0.
            Default = 1.0  (kg)
        dt (float, optional) : 
            Time interval for each time step in seconds.
            Default = 0.1
    
    Returns:
        tuple: (time, x position, y position, x velocity, y velocity)
    '''

    # Initial values for our parameters
    x_position = 0.0
    y_position = 0.0
    x_velocity = initial_x_velocity
    y_velocity = initial_y_velocity
    x_acceleration = 0.0
    y_acceleration = 0.0
    time = 0.0

    # Create empty lists which we will update
    x_positions = []
    y_positions = []
    x_velocities = []
    y_velocities = []
    times = []

    # Keep looping while the object is still in motion
    while y_position >= 0:
        # Calculate acceleration in x and y directions separately
        x_acceleration =calculate_acceleration_x(x_velocity,k,mass)
        y_acceleration =calculate_acceleration_y(y_velocity,k,mass)

        # Append values to lists
        x_positions.append(x_position)
        y_positions.append(y_position)
        x_velocities.append(x_velocity)
        y_velocities.append(y_velocity)
        times.append(time)

        # Update states by unpacking the tuple returned by update_state function
        new_x_state = update_state(x_position, x_velocity, x_acceleration, dt)
        new_y_state = update_state(y_position, y_velocity, y_acceleration, dt)

        # Update x state
        x_position, x_velocity = new_x_state[0,1]

        # Update y state
        y_position, y_velocity = new_y_state[0,1]

        time += dt  # Increment time

    return times, x_positions, y_positions, x_velocities, y_velocities

