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
Suite 3

    >>> from ants import *

	Case 2
	    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
		>>> dimensions = (1, 9)
		>>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
		>>> bodyguard = BodyguardAnt()
		>>> thrower = ThrowerAnt()
		>>> bee = Bee(2)
		>>> colony.places["tunnel_0_0"].add_insect(bodyguard)
		>>> colony.places["tunnel_0_0"].add_insect(thrower)
		>>> colony.places["tunnel_0_3"].add_insect(bee)
		>>> bodyguard.action(colony)
		>>> bee.armor
		1


Suite 3

    >>> from ants import *

	Case 3
	    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
		>>> dimensions = (1, 9)
		>>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
		>>> bodyguard = BodyguardAnt()
		>>> thrower = ThrowerAnt()
		>>> bee = Bee(2)
		>>> colony.places["tunnel_0_0"].add_insect(thrower)
		>>> colony.places["tunnel_0_0"].add_insect(bodyguard)
		>>> colony.places["tunnel_0_3"].add_insect(bee)
		>>> bodyguard.action(colony)
		>>> bee.armor
		1


Suite 4
    >>> from ants import *
	Case 3
	    >>> beehive, layout = Hive(AssaultPlan()), dry_layout
		>>> dimensions = (1, 9)
		>>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
		>>> tank = TankAnt()
		>>> thrower = ThrowerAnt()
		>>> place = colony.places['tunnel_0_1']
		>>> place.add_insect(thrower)
		>>> place.add_insect(tank)
		>>> place.ant is tank
		True
		>>> bee = Bee(3)
		>>> place.add_insect(bee)
		>>> tank.action(colony)
		>>> bee.armor
		1

Suite 13
    >>> from ants import *
	Case 1
	    >>> import ants, importlib
		>>> beehive, layout = Hive(AssaultPlan()), dry_layout
		>>> dimensions = (2, 9)
		>>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
		>>> ants.bees_win = lambda: None
		>>> queen = ants.QueenAnt()
		>>> impostor = ants.QueenAnt ()
		>>> front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
		>>> tunnel = [colony.places['tunnel_0_{0}'.format(i)] for i in range(9)]
		>>> tunnel[1].add_insect(back_ant)
		>>> tunnel[7].add_insect(front_ant)
		>>> tunnel[4].add_insect(impostor)
		>>> impostor.action(colony)
		>>> impostor.armor
		0
		>>> tunnel[4].add_insect(queen)
		>>> queen.action(colony)

