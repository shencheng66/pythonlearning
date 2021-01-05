test = {
  'name': 'Problem 8',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '846ee8e35ba6b7a71285553d2b6eb865',
          'choices': [
            'Ant',
            'ThrowerAnt',
            'NinjaAnt',
            'The WallAnt class does not inherit from any class'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What class does WallAnt inherit from?'
        },
        {
          'answer': '3560f5c897e42f3744228f370b181d78',
          'choices': [
            'A WallAnt takes no action each turn',
            'A WallAnt increases its own armor by 1 each turn',
            'A WallAnt reduces its own armor by 1 each turn',
            'A WallAnt attacks all the Bees in its place each turn'
          ],
          'hidden': False,
          'locked': True,
          'question': "What is a WallAnt's action?"
        },
        {
          'answer': 'efe758bb607265f51ff5c0c8fffafca4',
          'choices': [
            'Ant subclasses inherit the action method from the Insect class',
            'Ant subclasses inherit the action method from the Ant class',
            'Ant subclasses do not inherit the action method from any class'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Where do Ant subclasses inherit the action method from?'
        },
        {
          'answer': '40d207151baf8f4364ce09eb3b7d86da',
          'choices': [
            'Nothing',
            'Throw a leaf at the nearest Bee',
            'Move to the next place',
            'Reduce the armor of all Bees in its place'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          If a subclass of Ant does not override the action method, what is the
          default action?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing WallAnt parameters
          >>> wall = WallAnt()
          >>> wall.armor
          5d2dcf69388c48f6f6885e4efff23a30
          # locked
          >>> # `armor` should not be a class attribute
          >>> not hasattr(WallAnt, 'armor')
          154afc22815a37701b5fa71e532da526
          # locked
          >>> WallAnt.food_cost
          5d2dcf69388c48f6f6885e4efff23a30
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing WallAnt holds strong
          >>> beehive, layout = Hive(AssaultPlan()), dry_layout
          >>> colony = AntColony(None, beehive, ant_types(), layout, (1, 9))
          >>> place = colony.places['tunnel_0_4']
          >>> wall = WallAnt()
          >>> bee = Bee(1000)
          >>> place.add_insect(wall)
          >>> place.add_insect(bee)
          >>> for i in range(3):
          ...     bee.action(colony)
          ...     wall.action(colony)   # WallAnt does nothing
          >>> wall.armor
          1
          >>> bee.armor
          1000
          >>> wall.place is place
          True
          >>> bee.place is place
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
