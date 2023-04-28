import math 
print('Welcome to the velocity calculator. Please enter the following: ')
mass = float(input('Mass (in kg): '))
gravity = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
time = float(input('Time (in seconds): '))
density = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
cross = float(input('Cross sectional area (in m^2): '))
drag = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))
C = (1/2) * density * cross * drag
velocity = math.sqrt(mass * gravity / C) * (1 - math.exp(- math.sqrt(mass * gravity * C) / mass * time))
print(f'The inner value of c is: {C:.3f}')
print(f'The velocity after 10.0 seconds is: {velocity:.3f} m/s')
print()

