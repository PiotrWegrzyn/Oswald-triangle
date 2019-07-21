from kivy.uix.floatlayout import FloatLayout

from gui.show_popup import show_popup
from models.ostwaldtriangle import OstwaldTriangle
from thermodynamics.ostwald_calculations import OstwaldCalculations, Composition


class OstwaldTriangleVisualization(FloatLayout):

    def __init__(self, **kwargs):
        fuel = kwargs.pop("fuel", None)
        measured_co2 = kwargs.pop("measured_co2", 0)
        measured_o2 = kwargs.pop("measured_o2", 0)
        super().__init__(**kwargs)
        fuels84 = Composition(("CH4", 0.958), ("C2H4", 0.008), ("CO", 0.004), ("O2", 0.002), ("CO2", 0.006), ("N2", 0.022))
        fuels79 = Composition(("C", 0.5921), ("H", 0.0377), ("S", 0.0211), ("O", 0.112), ("N", 0.0128))
        fuels75 = Composition(("C", 0.7), ("H", 0.043), ("O", 0.075), ("N", 0.013))
        if fuel:
            fuel = Composition(*fuel)
        else:
            fuel = fuels75
        try:
            osw_calc = OstwaldCalculations(fuel, measured_co2, measured_o2)
            self.ostwald_triangle_graph = OstwaldTriangle(osw_calc)
            self.ostwald_triangle_graph.draw(self.canvas)
        except:
            show_popup("Error", 'Please ensure that all chemicals are in'
                                '\n capital letters and are chemically valid.')

