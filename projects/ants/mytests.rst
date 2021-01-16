This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

	>>> from ants import *

	Case Example
		>>> x = 5
		>>> x
		5

Suite 2

    >>> from ants import *

	Case 3
	    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
		>>> dimensions = (1, 9)
		>>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
		>>> ant = LongThrower()
		>>> out_of_range = Bee(2)
		>>> colony.places["tunnel_0_0"].add_insect(ant)
		>>> colony.places["tunnel_0_4"].add_insect(out_of_range)
		>>> ant.action(colony)
		>>> out_of_range.armor
		2

Suite 2

    >>> from ants import *

	Case 2
	    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
		>>> dimensions = (1, 9)
		>>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
		>>> place = colony.places['tunnel_0_4']
		>>> fire = FireAnt(armor=1)
		>>> place.add_insect(fire)
		>>> place.add_insect(Bee(3))
		>>> place.add_insect(Bee(5))
		>>> len(place.bees)
		2
		>>> place.bees[0].action(colony)
		>>> fire.armor
		0
		>>> len(place.bees)
		1
	