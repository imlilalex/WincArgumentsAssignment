# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# part 1 of assignment - return a greeting

def greet(name, template = "Hello, <name>!"):

    greeting = template.replace("<name>", name)
    
    return greeting

print(greet("Alex", "What's up <name>!"))
    
# part 2 of assignment - return the force on a mass

def force(mass, body = "earth"):
    mass = float(mass)
    body = body.lower()
    bodies = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.8,
        "venus": 8.8,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    
    if body in bodies:
        result =  mass * bodies[body]
    else: 
        return "That's not a planet!"

    return result

print(force(1, "Sun"))

# part 3 of assignment - return gravitational pull of 2 objects

def pull(m1, m2, d):
    m1 = float(m1)
    m2 = float(m2)
    d = float(d)

    gravity = 6.674*(10**-11)
    total = gravity * ((m1*m2)/d**2)
    
    return total

print(pull(800, 1500, 3))