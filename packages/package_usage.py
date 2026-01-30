from converters.temperature.celsius import to_fahrenheit, from_fahrenheit

print(f'celsius - 37, fahrenheit - {to_fahrenheit(37): .1f}')
print(f'fahrenheit - 98.6, celsius - {from_fahrenheit(98.6):.0f}')

# imports all submodules referenced by "__all__" variable in the temperature "__init__.py" file. If there is no
# "__all__" variable defined then it only loads any defined functions/variables (e.g., "dummy_var") in the
# temperature "__init__.py" file.
from converters.temperature import *

print(f'celsius - 37, fahrenheit - {celsius.to_fahrenheit(37): .1f}')
print(f'fahrenheit - 98.6, celsius - {celsius.from_fahrenheit(98.6):.0f}')
