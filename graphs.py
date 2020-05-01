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

# Resumen
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
    ], autopct='%1.1f%%', startangle=90, 
    colors=[red, blue, yellow, green])
    
    ax.legend(wedges, [
        'Diagnosticados: ' + str(data['total_diagnosticados']) + ' - ' + str(round(data['total_diagnosticados']/total*100, 1)) + '%',
        'Recuperados: ' + str(data['total_recuperados']) + ' - ' + str(round(data['total_recuperados']/total*100, 1)) + '%', 
        'Evacuados: ' + str(data['total_evacuados']) + ' - ' + str(round(data['total_evacuados']/total*100, 1)) + '%', 
        'Fallecidos: ' + str(data['total_fallecidos']) + ' - ' + str(round(data['total_fallecidos']/total*100, 1)) + '%',
    ], loc='lower center', bbox_to_anchor=(0.9,0,0.5,1))

    ax.set_title('Resumen', fontsize=18)

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/summary_graph'
    watermark_text(filename, filename, apiurl, (0,0))

    return filename

# Evolucion de casos por días
def evolution_graph(data):
    filename = 'evolution_graph.png'

    fig = Figure(figsize=(18, 10))

    ax = fig.add_subplot(1, 1, 1)

    xss = [str(i) for i in range(1,len(data['diagnosticados_acc'])+1)]
    xs = range(0,len(data['diagnosticados_acc']))

    ax.plot(xss, data['diagnosticados_acc'], 'o-', label='Casos acumulados', color=red, alpha=0.5)
    ax.plot(xss, data['activos_acc'], 'o-', label='Casos activos', color=red)
    ax.plot(xss, data['diagnosticados'], 'o-', label='Casos en el día', color=cyan)

    for x, y in zip(xs, data['diagnosticados_acc']):
        label = "{}".format(y)

        ax.annotate(label,
                     (x,y),
                      textcoords='offset points',
                      xytext=(0,10),
                      ha='center')

    for x, y in zip(xs, data['activos_acc']):
        label = "{}".format(y)

        ax.annotate(label,
                     (x,y),
                      textcoords='offset points',
                      xytext=(0,10),
                      ha='center')

    for x, y in zip(xs, data['diagnosticados']):
        label = "{}".format(y)

        ax.annotate(label,
                     (x,y),
                      textcoords='offset points',
                      xytext=(0,-17),
                      ha='center')

    ax.set_title('Evolución de casos por días', fontsize=18)
    fig.legend(frameon=True, fontsize=12)

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/evolution_graph'
    watermark_text(filename, filename, apiurl, (0,0))

    return filename

# Evolucion de altas por días
def evolution_recuperados_graph(data):
    filename = 'evolution_recuperados_graph.png'

    fig = Figure(figsize=(18, 10))

    ax = fig.add_subplot(1, 1, 1)

    xss = [str(i) for i in range(1,len(data['recuperados_acc'])+1)]
    xs = range(0,len(data['recuperados_acc']))

    ax.plot(xss, data['recuperados_acc'], 'o-',label='Altas acumuladas', color=blue)
    ax.plot(xss, data['recuperados'], 'o-',label='Altas en el día', color=cyan)

    for x, y in zip(xs, data['recuperados_acc']):
        label = "{}".format(y)

        ax.annotate(label,
                     (x,y),
                      textcoords='offset points',
                      xytext=(0,10),
                      ha='center')

    for x, y in zip(xs, data['recuperados']):
        label = "{}".format(y)

        ax.annotate(label,
                     (x,y),
                      textcoords='offset points',
                      xytext=(0,-15),
                      ha='center')
    
    ax.set_title('Evolución de altas por días', fontsize=15)
    fig.legend(frameon=True, fontsize=12)

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/evolution_recuperados_graph'
    watermark_text(filename, filename, apiurl, (0,0))

    return filename

# Evolucion de fallecidos por días
def evolution_fallecidos_graph(data):
    filename = 'evolution_fallecidos_graph.png'

    fig = Figure(figsize=(18, 10))

    ax = fig.add_subplot(1, 1, 1)

    xss = [str(i) for i in range(1,len(data['fallecidos_acc'])+1)]
    xs = range(0,len(data['fallecidos_acc']))

    ax.plot(xss, data['fallecidos_acc'], 'o-',label='Fallecimientos acumulados', color=black)
    ax.plot(xss, data['fallecidos'], 'o-',label='Fallecimientos en el día', color=cyan)

    for x, y in zip(xs, data['fallecidos_acc']):
        label = "{}".format(y)

        ax.annotate(label,
                     (x,y),
                      textcoords='offset points',
                      xytext=(0,10),
                      ha='center')

    for x, y in zip(xs, data['fallecidos']):
        label = "{}".format(y)

        ax.annotate(label,
                     (x,y),
                      textcoords='offset points',
                      xytext=(0,-15),
                      ha='center')
    
    ax.set_title('Evolución de fallecimientos por días', fontsize=15)
    fig.legend(frameon=True, fontsize=12)

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/evolution_fallecidos_graph'
    watermark_text(filename, filename, apiurl, (0,0))

    return filename

def sexo_graph(data):

    filename = 'sexo.png'

    fig = Figure(figsize=(8.5, 6))

    ax = fig.add_subplot(1, 1, 1)

    wedges, _, _  = ax.pie(
        [data['mujeres'], data['hombres'], data['desconocido']], 
        autopct='%1.1f%%', startangle=90, colors=[red, blue, yellow]
    )

    ax.set_title('Casos por sexo', fontsize=18)
    ax.legend(wedges, [
        'Mujeres ' + str(data['mujeres']), 
        'Hombres ' + str(data['hombres']), 
        'Desconocido ' + str(data['desconocido'])
    ], loc='lower center', bbox_to_anchor=(0.9,0,0.5,0.5))

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/sexo_graph'
    watermark_text(filename, filename, apiurl, (0,0))

    return filename

def modo_graph(data):

    filename = 'modo.png'

    fig = Figure(figsize=(8.5, 6))

    ax = fig.add_subplot(1, 1, 1)

    wedges, _, _  = ax.pie(data.values(), 
    autopct='%1.1f%%', startangle=90, colors=[blue, red, yellow, green])

    ax.set_title('Casos por modo de contagio', fontsize=18)
    ax.legend(wedges, [i.capitalize() + ' ' + str(data[i]) for i in data.keys()], loc='lower center', bbox_to_anchor=(0.9,0,0.5,0.5))

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/modo_graph'
    watermark_text(filename, filename, apiurl, (0,0))

    return filename

def pais_graph(data):

    filename = 'paises.png'

    fig = Figure(figsize=(8.5, 6))

    ax = fig.add_subplot(1, 1, 1)

    ax.bar([str(k) for k in data.keys()], [v for v in data.values()], color=red)

    ax.set_title('Distribución por nacionalidad casos extranjeros', fontsize=18)

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/casos_extranjeros_graph'
    watermark_text(filename, filename, apiurl, (0,0))

    return filename

def nacionalidad_graph(data):

    filename = 'nacionalidad.png'

    fig = Figure(figsize=(8.5, 6))

    ax = fig.add_subplot(1, 1, 1)

    wedges, _, _  = ax.pie([data['cubanos'], data['extranjeros']], 
    autopct='%1.1f%%', startangle=90, colors=[blue, red])
    ax.legend(wedges, ['Cubanos', 'Extranjeros'], loc='lower center', bbox_to_anchor=(0.9,0,0.5,1))

    ax.set_title('Casos por nacionalidad', fontsize=18)

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/nacionalidad_graph'
    watermark_text(filename, filename, apiurl, (0,0))

    return filename

def edad_graph(data):

    filename = 'edad.png'

    fig = Figure(figsize=(8.5, 6))

    ax = fig.add_subplot(1, 1, 1)

    ax.bar([str(k) for k in data.keys()], [v for v in data.values()], color=red)

    for x, y in enumerate(data.values()):
        label = "{}".format(y)

        ax.annotate(label,
                     (x,y),
                      textcoords='offset points',
                      xytext=(0,4),
                      ha='center')

    ax.set_title('Distribución por grupos etarios', fontsize=18)

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/edad_graph'
    watermark_text(filename, filename, apiurl, (0,0))

    return filename

def tests_graph(data):

    filename = 'tests.png'

    fig = Figure(figsize=(14, 12))

    (ax1, ax2) = fig.subplots(2, 1)

    # Test realizados
    xss = [str(k) for k in range(12, len(data['tests'])+12)]
    xs = range(0, len(data['tests'])+12)

    ax1.bar(xss, data['tests'], color=red)
    ax1.bar(xss, data['detectados'], color=yellow)

    for x, y in zip(xs, data['tests']):
        label = "{}".format(y)

        ax1.annotate(label,
                     (x,y),
                      textcoords='offset points',
                      xytext=(0,4),
                      ha='center')

    ax1.set_title('Tests acumulados por día')

    # Proporción entre casos confirmados y test realizados
    ax2.bar([str(k) for k in range(12, len(data['tests'])+12)], data['proporcion'], color=red) 

    ax2.set_title('Proporción detectados/tests realizados')

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/tests_graph'
    watermark_text(filename, filename, apiurl, (0,0))


    return filename

def provincias_graph(data):
    
    filename = 'provincias.png'

    fig = Figure(figsize=(16, 6))

    ax = fig.add_subplot(1, 1, 1)

    data_bar = sorted(zip(data.keys(), data.values()), key=lambda x: x[1])
    
    ax.barh([i[0] for i in data_bar], [i[1] for i in data_bar],color=red)
    
    ax.set_title('Casos detectados por provincias',fontsize = 18)

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/provincias_graph'
    watermark_text(filename, filename, apiurl, (0,0))


    return filename

def municipios_graph(data):
    
    filename = 'municipios.png'

    fig = Figure(figsize=(16, 6))

    ax = fig.add_subplot(1, 1, 1)

    data_bar = sorted(zip(data.keys(), data.values()), key=lambda x: x[1])
    
    ax.barh([i[0] for i in data_bar[-10:]], [i[1] for i in data_bar[-10:]],color=red)
    
    ax.set_title('Casos detectados por municipios (top 10)',fontsize = 18)

    FigureCanvasAgg(fig).print_png(filename)

    apiurl = config.SERVER_URI + '/municipios_graph'
    watermark_text(filename, filename, apiurl, (0,0))


    return filename