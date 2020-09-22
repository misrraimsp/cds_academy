#!/usr/bin/python3

def max(x = 0, y = 0):
  "function that takes as argument two numbers and returns the largest of them"
  if x > y: return x
  return y


print("El mayor entre 1 y 2 es: ", max(1,2))
print("El mayor entre 1 y 1 es: ", max(1,1))
print("El mayor es: ", max())
print("El mayor entre -1 y 2 es: ", max(-1,2))
print("El mayor entre -1 y -2 es: ", max(-1,-2))
print("El mayor entre -1 y 0 es: ", max(-1))
print("El mayor entre 1 y 0 es: ", max(1))
