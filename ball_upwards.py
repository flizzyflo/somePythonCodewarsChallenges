"""
You throw a ball vertically upwards with an initial speed v (in km per hour). The height h of the ball at each time t is given by h = v*t - 0.5*g*t*t where g is Earth's gravity (g ~ 9.81 m/s**2). 
A device is recording at every tenth of second the height of the ball. For example with v = 15 km/h the device gets something of the following form: (0, 0.0), (1, 0.367...), (2, 0.637...), (3, 0.808...), (4, 0.881..) ... 
where the first number is the time in tenth of second and the second number the height in meter.

Task
Write a function max_ball with parameter v (in km per hour) that returns the time in tenth of second of the maximum height recorded by the device.

Examples:
max_ball(15) should return 4
max_ball(25) should return 7

Notes
Remember to convert the velocity from km/h to m/s or from m/s in km/h when necessary.
The maximum height recorded by the device is not necessarily the maximum height reached by the ball.

"""


def max_ball(v0: float) -> int:
    
    # v0 in kmh
    current_velocity = v0 / 60 / 60 * 1000   # converts km/h to m/s
    gravity = 9.81                  # m/s

    time_elapsed = 0.0
    height = current_velocity * time_elapsed - 0.5 * gravity * time_elapsed * time_elapsed
    result: set[tuple[int, float]] = set()

    while height >= 0:
        height = current_velocity * time_elapsed - 0.5 * gravity * time_elapsed * time_elapsed
        result.add(((round(time_elapsed, 1) * 10), float(format(height, "00.4f"))))
        time_elapsed += 0.1

    return int(sorted(result, key= get_height, reverse= True)[0][0])

def get_height(result_set: set[int, float]) -> float:
    
    """Function to sort for keys."""
    
    return result_set[1]
