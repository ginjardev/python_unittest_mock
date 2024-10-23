#!/usr/bin/env python3

from unittest.mock import MagicMock, Mock


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f'<Animal: {self.name}>'
    
#     def sound(self, a_sound):
#         self.a_sound = a_sound
#         return self.a_sound
    

# cat = Animal('pink')

# cat.sound = MagicMock(return_value = 'meow')
# print(cat.sound('brr'))

# cat.sound.assert_called_with('brr')
mock = Mock()
mm = MagicMock()

# values = {'a': 1, 'b': 2, 'c': 3}
# def side_effect(arg):
#     return values[arg]

# mock.side_effect = side_effect
# print(mock('a')), mock('b'), mock('c')
print(">>>>")
mock.side_effect = [5, 4, 3, 2, 1]
print(mock()), print(mock()), print(mock()), print(mock()), print(mock())