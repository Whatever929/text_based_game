import unittest
import src.parser as p

class InvalidParserTest(unittest.TestCase):	
	def test_noSpace_move(self):
		self.assertEqual(p.parser("moveright"), ("Invalid", ))		
		self.assertEqual(p.parser("moveLEFT"), ("Invalid",))
		self.assertEqual(p.parser("moveeast"), ("Invalid",))
		self.assertEqual(p.parser("moveup"), ("Invalid",))
		self.assertEqual(p.parser("movewest"), ("Invalid",))

	def test_noSpace_inspect(self):
		self.assertEqual(p.parser("inspectbag"), ("Invalid",))
		self.assertEqual(p.parser("checkbag"), ("Invalid",))
		self.assertEqual(p.parser("lookbag"), ("Invalid",))
		self.assertEqual(p.parser("lookinventory"), ("Invalid",))
		self.assertEqual(p.parser("inspectbag"), ("Invalid",))
		self.assertEqual(p.parser("inspectbag"), ("Invalid",))

	def test_spellError_move(self):
		self.assertEqual(p.parser("lft"), ("Invalid",))
		self.assertEqual(p.parser("rigt"), ("Invalid",))
		self.assertEqual(p.parser("mov right"), ("Invalid", ))
		self.assertEqual(p.parser("mve left"), ("Invalid", ))
		self.assertEqual(p.parser("move est"), ("Invalid", ))
		self.assertEqual(p.parser("westi"), ("Invalid",))
		self.assertEqual(p.parser("move upp"), ("Invalid", ))

	def test_spellError_inspect(self):
		self.assertEqual(p.parser("inspet inventory"), ("Invalid",))
		self.assertEqual(p.parser("inspect bg"), ("Invalid",))
		self.assertEqual(p.parser("inspect charater"), ("Invalid",))
		self.assertEqual(p.parser("check hro"), ("Invalid",))
		self.assertEqual(p.parser("chekc inventory"), ("Invalid",))
		self.assertEqual(p.parser("open inventry"), ("Invalid",))
		self.assertEqual(p.parser("loook bga"), ("Invalid",))
		self.assertEqual(p.parser("invntory"), ("Invalid",))
		self.assertEqual(p.parser("chracter"), ("Invalid",))
		
	def test_spellError_action(self):
		self.assertEqual(p.parser("attackk"), ("Invalid",))
		self.assertEqual(p.parser("runaway"), ("Invalid",))
		self.assertEqual(p.parser("run awy"), ("Invalid",))
		self.assertEqual(p.parser("fleee"), ("Invalid",))
		self.assertEqual(p.parser("hitt"), ("Invalid",))
		self.assertEqual(p.parser("kills"), ("Invalid",))

	def test_spellError_system(self):
		self.assertEqual(p.parser("objectiv"), ("Invalid",))
		self.assertEqual(p.parser("maap"), ("Invalid",))
		self.assertEqual(p.parser("saev"), ("Invalid",))
		self.assertEqual(p.parser("bakcup"), ("Invalid",))
		self.assertEqual(p.parser("locatino"), ("Invalid",))
		self.assertEqual(p.parser("mision"), ("Invalid",))

	def test_randomInput(self):
		self.assertEqual(p.parser("i want to kill you"), ("Invalid",))
		self.assertEqual(p.parser("teleport"), ("Invalid",))
		self.assertEqual(p.parser("walk"), ("Invalid",))
		self.assertEqual(p.parser("jfkajkdf"), ("Invalid",))
		self.assertEqual(p.parser("movekfjakldfjkal"), ("Invalid",))
		self.assertEqual(p.parser("dodge"), ("Invalid",))
		self.assertEqual(p.parser("stop"), ("Invalid",))
		self.assertEqual(p.parser("openadaf"), ("Invalid",))
		self.assertEqual(p.parser("rightwing"), ("Invalid",))
		self.assertEqual(p.parser("goroom"), ("Invalid",))
		self.assertEqual(p.parser("fuck"), ("Invalid",))
		self.assertEqual(p.parser("i want to check the map"), ("Invalid",))
		self.assertEqual(p.parser("how to win"), ("Invalid",))
		self.assertEqual(p.parser("Invalid"), ("Invalid",))
		self.assertEqual(p.parser("!!!"), ("Invalid",))
		self.assertEqual(p.parser("$$$"), ("Invalid",))
		self.assertEqual(p.parser("True"), ("Invalid",))
		self.assertEqual(p.parser("None"), ("Invalid",))
		self.assertEqual(p.parser("1=1"), ("Invalid",))
		self.assertEqual(p.parser("()"), ("Invalid",))
		self.assertEqual(p.parser("check_input"), ("Invalid",))
		self.assertEqual(p.parser("\"\""), ("Invalid",))
		self.assertEqual(p.parser("eval(true)"), ("Invalid",))
		self.assertEqual(p.parser("eval(print(hello_world))"), ("Invalid",))

if __name__ == "__main__":
	unittest.main()