# Graphics
import seaborn as sns
sns.set_style('darkgrid')

from imagemark import watermark_text

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

### COLOR
red = '#f44336'
blue = '#2196f3'
yellow = '#ffeb3b'
green = '#4caf50'
cyan = '#00577b'
black='#1c1340'

import config

def summary_graph(data):
    filename = 'summary_graph.png'

    fig = Figure(figsize=(9, 6))

    ax = fig.add_subplot(1, 1, 1)

    total = \
        data['total_diagnosticados'] + \
        data['total_recuperados'] + \
        data['total_evacuados'] + \
        data['total_fallecidos']

    wedges, _, _  = ax.pie([
        data['total_diagnosticados'], 
        data['total_recuperados'], 
        data['total_evacuados'], 
        data['total_fallecidos']
    ], autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.95), 
    colors=[red, blue, yellow, green])
    
    ax.legend(wedges, [
        'Diagnosticados ' + str(round(data['total_diagnosticados']/total*100, 1)) + '%',
        'Recuperados ' + str(round(data['total_recuperados']/total*100, 1)) + '%', 
        'Evacuados ' + str(round(data['total_evacuados']/total*100, 1)) + '%', 
        'Fallecidos ' + str(round(data['total_fallecidos']/total*100, 1)) + '%',
    ], loc='lower center', bbox_to_anchor=(0.9,0,0.5,1))

    ax.set_title('Resumen', fontsize=20)

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/summary_graph'
    watermark_text(filename, filename, apiurl, (0,0))

    return filename