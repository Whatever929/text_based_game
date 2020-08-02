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

    def test_basic_action(self):
        self.assertEqual(p.parser("attack"), ("action", "attack"))
        self.assertEqual(p.parser("flee"), ("action", "flee"))

    def test_otherAction_action(self):
        self.assertEqual(p.parser("run"), ("action", "flee"))

if __name__ == "__main__":
    unittest.main()