# Exec 16
import math
num = float(input('Enter a number: '))
print(f'The integer part of the number {num} is {math.trunc(num)}')

# Exec 17
import math
opposite_side = float(input('Enter the value of the opposite side: '))
adjacent_side = float(input('Enter the value of the adjacent side: '))
hypotenuse = math.hypot(opposite_side, adjacent_side)
print(f'The value of the hypotenuse is: {hypotenuse:.2f}.')

# Exec 18
import math
angle = float(input('Enter the angle value: '))
radians = math.radians(angle) # Convert angle to radians
print(f'Sine value: {math.sin(radians):.2f}.')
print(f'Cosine value: {math.cos(radians):.2f}.')
print(f'Tangent value: {math.tan(radians):.2f}.')

# Exec 19
import random
students = []
students.append(input('Enter the name of the first student: '))
students.append(input('Enter the name of the second student: '))
students.append(input('Enter the name of the third student: '))
students.append(input('Enter the name of the fourth student: '))
chosen = random.choice(students)
print(f'The chosen student was: {chosen}')

# Exec 20
import random
students = []
students.append(input('Enter the name of the first student: '))
students.append(input('Enter the name of the second student: '))
students.append(input('Enter the name of the third student: '))
students.append(input('Enter the name of the fourth student: '))
random.shuffle(students)
print(f'The presentation order will be:')
for i in range(4):
  print(f'{i+1}° - {students[i]}')

# Exec 21
import pygame
pygame.init() # Start pygame mixer
pygame.mixer.music.load('test.mp3')
pygame.mixer.music.play()
pygame.event.wait() # Wait for the music to end