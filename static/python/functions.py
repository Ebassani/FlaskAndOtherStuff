import io

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def create_figure():
    fig = Figure()
    data2 = range(10)
    data = (1, 9, 3, 4, 5, 6, 7, 8, 9, 10)

    chart = fig.add_subplot()
    chart.plot(data2, data)

    return fig
