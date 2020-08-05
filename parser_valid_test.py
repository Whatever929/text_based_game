import unittest
import src.parser as p

class ValidParserTest(unittest.TestCase):
	def test_basic_move(self):
		self.assertEqual(p.parser("Move right"), ("move", "right"))
		self.assertEqual(p.parser("Move left"),("move", "left"))
		self.assertEqual(p.parser("Move up"), ("move", "up"))
		self.assertEqual(p.parser("Move down"), ("move", "down"))

	def test_compass_move(self):
		self.assertEqual(p.parser("Move north"), ("move", "up"))
		self.assertEqual(p.parser("Move south"), ("move", "down"))
		self.assertEqual(p.parser("Move west"), ("move", "left"))
		self.assertEqual(p.parser("Move east"), ("move", "right"))

	def test_randomCase_move(self):
		self.assertEqual(p.parser("mOve riGHT"), ("move", "right"))
		self.assertEqual(p.parser("MOVE EAST"), ("move", "right"))
		self.assertEqual(p.parser("MOVE north"), ("move", "up"))
		self.assertEqual(p.parser("move DOwn"), ("move", "down"))
		self.assertEqual(p.parser("move lefT"), ("move", "left"))

	def test_noMove_move(self):
		self.assertEqual(p.parser("right"), ("move", "right"))
		self.assertEqual(p.parser("left"), ("move", "left"))
		self.assertEqual(p.parser("up"), ("move", "up"))
		self.assertEqual(p.parser("east"), ("move", "right"))
		self.assertEqual(p.parser("west"), ("move", "left"))

	def test_noMoveRandomCase_move(self):
		self.assertEqual(p.parser("RIGht"), ("move", "right"))
		self.assertEqual(p.parser("eaST"), ("move", "right"))
		self.assertEqual(p.parser("Up"), ("move", "up"))
		self.assertEqual(p.parser("NOrTH"), ("move", "up"))
		self.assertEqual(p.parser("SoutH"), ("move", "down"))

	def test_basic_inspect(self):
		self.assertEqual(p.parser("inspect inventory"), ("inspect", "bag"))
		self.assertEqual(p.parser("inspect bag"), ("inspect","bag"))
		self.assertEqual(p.parser("inspect character"), ("inspect","character"))
		self.assertEqual(p.parser("inspect hero"), ("inspect","character"))

	def test_otherInspect_inspect(self):
		self.assertEqual(p.parser("check hero"), ("inspect","hero"))
		self.assertEqual(p.parser("check inventory"), ("inspect","bag"))
		self.assertEqual(p.parser("open bag"), ("inspect","bag"))
		self.assertEqual(p.parser("open inventory"), ("inspect","bag"))
		self.assertEqual(p.parser("look inventory"), ("inspect","bag"))

	def test_oneWord_inspect(self):
		self.assertEqual(p.parser("inventory"), ("inspect","bag"))
		self.assertEqual(p.parser("bag"), ("inspect","bag"))
		self.assertEqual(p.parser("character"), ("inspect","character"))
		self.assertEqual(p.parser("hero"), ("inspect","characters"))

	def test_basic_action(self):
		self.assertEqual(p.parser("attack"), ("action", "attack"))
		self.assertEqual(p.parser("flee"), ("action", "flee"))

	def test_otherAction_action(self):
		self.assertEqual(p.parser("run"), ("action", "flee"))
		self.assertEqual(p.parser("kill"), ("action", "attack"))
		self.assertEqual(p.parser("hit"), ("action", "attack"))
		self.assertEqual(p.parser("run away"), ("action", "flee"))

	def test_randomCase_action(self):
		self.assertEqual(p.parser("kiLL"), ("action", "attack"))
		self.assertEqual(p.parser("HIT"), ("action", "attack"))
		self.assertEqual(p.parser("flEE"), ("action", "flee"))

	def test_basic_system(self):
		self.assertEqual(p.parser("objective"), ("system", "objective"))
		self.assertEqual(p.parser("map"), ("system", "map"))
		self.assertEqual(p.parser("save"), ("system", "save"))
		self.assertEqual(p.parser("help"), ("system", "help"))

	def test_other_system(self):
		self.assertEqual(p.parser("mission"), ("system", "objective"))
		self.assertEqual(p.parser("goal"), ("system", "objective"))
		self.assertEqual(p.parser("backup"), ("system", "save"))
		self.assertEqual(p.parser("?"), ("system", "help"))
		self.assertEqual(p.parser("location"), ("system", "map"))
		
	def test_randomCase_system(self):
		self.assertEqual(p.parser("MISSion"), ("system", "objective"))
		self.assertEqual(p.parser("Map"), ("system", "map"))
		self.assertEqual(p.parser("baCKup"), ("system", "save"))
		self.assertEqual(p.parser("GOAL"), ("system", "objective"))
