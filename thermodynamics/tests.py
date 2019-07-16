import unittest

from molmass import Formula, FormulaError

from thermodynamics.formula_wrapper import FormulaWrapper
from thermodynamics.oswaldt_calculations import Fuel, OslwaldtCalculations


class TestMolmass(unittest.TestCase):
    def test_amount_of_H_atoms(self):
        f = Formula('(H)20 O10 H20')
        self.assertEqual(40, f._elements.get("H")[0])

    def test_from_string(self):
        string = "H2O"
        f = Formula(string)
        self.assertEqual("H2O", f.formula)

    def test_not_chemically_correct_formula_mass(self):
        f = Formula("HHHH")
        self.assertEqual(4.03176, f.mass)

    def test_float_numbers(self):
        f = Formula("H0.5")
        with self.assertRaises(FormulaError):
            m = f.mass


class TestFormulaWrapper(unittest.TestCase):

    def test_get_item(self):
        f = FormulaWrapper("HHHH")
        self.assertEqual(4, f["H"])

    def test_get_mass_percentage(self):
        f = FormulaWrapper("H2O")
        self.assertEqual(0.11189834407236524, f.percentage_mass("H"))


class TestFuelClass(unittest.TestCase):
    def test_init_with_formula(self):
        f = FormulaWrapper("(CH4)958 (C2H4)8 (CO)4 (O2)2 (CO2)6 (N2)22")
        fuel = Fuel(f)
        self.assertEqual(0.709843217460471, fuel.c)


class TestOslwaldtCalculationsClass(unittest.TestCase):

    def test_kmax2(self):
        form = FormulaWrapper("(CH4)958 (C2H4)8 (CO)4 (O2)2 (CO2)6 (N2)22")
        f = Fuel(form)
        ocal = OslwaldtCalculations(f, 6, 2)
        self.assertEqual(11.71, round(ocal.kmax,2))

    def test_kmax(self):
        f = Fuel(c=0.7, h=0.043, o=0.0075, n=0.013)
        ocal = OslwaldtCalculations(f, 6, 2)
        self.assertEqual(18.25, round(ocal.kmax, 2))
