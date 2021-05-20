# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name = 'jeff', greet = 'Hello, <name>!'):
    x = greet.replace('<name>', name)
    return x

def force(mass = 0.1, body = 'earth'):
    masses_dict = {'sun': 274, 'jupiter': 24.9, 'neptune': 11.2, 'saturn': 10.4, 'earth': 9.8, 'uranus': 8.9, 'venus': 8.9, 'mars': 3.7, 'mercury': 3.7, 'moon': 1.6, 'pluto': 0.6}
    x = round(mass * masses_dict[body])
    return x

def pull(m1 = 1.0, m2 = 2.0, d = 3.0):
    x = (6.674*(10**-11)) * ((m1 * m2) / (d*d))
    return x
