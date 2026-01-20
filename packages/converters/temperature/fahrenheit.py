# Relative intra-package/module references
# from .celsius import to_fahrenheit
# from . import celsius


def from_celsius(celsius_temp):
    return celsius_temp * 1.8 + 32


def to_celsius(fahrenheit_temp):
    return (fahrenheit_temp - 32) / 1.8
