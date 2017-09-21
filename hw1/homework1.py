#!/usr/bin/env python3


a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

if a % b == c:
    print('a даёт остаток c при делении на b')
else:
    print('a не даёт остаток c при делении на b')

if a * c + b == 0:
    print('c является решением линейного уравнения ax + b = 0')
else:
    print('c не является решением линейного уравнения ax + b = 0')
