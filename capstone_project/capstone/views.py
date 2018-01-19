from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import AccessData, MapData, CorrelationData

import pandas as pd


def index2(request):
    mapdata = MapData.objects.all()
    context = {'mapdata': mapdata}
    return render(request, 'capstone/index2.html', context)


def get_attribute(variable_name, data_row):
    if variable_name == 'Access 2010':
        return data_row.pct_access_2010
    elif variable_name == 'Access 2015':
        return data_row.pct_access_2015
    elif variable_name == 'Diabetes 2008':
        return data_row.pct_diabetes_2008
    elif variable_name == 'Diabetes 2013':
        return data_row.pct_diabetes_2013
    elif variable_name == 'Obese 2008':
        return data_row.pct_obese_2008
    elif variable_name == 'Obese 2013':
        return data_row.pct_obese_2013
    elif variable_name == 'Grocery 2009':
        return data_row.grocery_2009
    elif variable_name == 'Grocery 2014':
        return data_row.grocery_2014
    elif variable_name == 'Supercenter 2009':
        return data_row.supercenter_2009
    elif variable_name == 'Supercenter 2014':
        return data_row.supercenter_2014
    elif variable_name == 'Convenience 2009':
        return data_row.convenience_2009
    elif variable_name == 'Convenience 2014':
        return data_row.convenience_2014
    elif variable_name == 'White 2010':
        return data_row.white_2010
    elif variable_name == 'African American 2010':
        return data_row.black_2010
    elif variable_name == 'Hispanic 2010':
        return data_row.hispanic_2010
    elif variable_name == 'Asian 2010':
        return data_row.asian_2010
    elif variable_name == 'American Indian 2010':
        return data_row.amerindian_2010
    elif variable_name == 'Hawaiian 2010':
        return data_row.hawaiian_2010
    return None


def getdata(request):

    user_choice = request.GET.get('graph_name')

    data_set = AccessData.objects.all()
    json_data_set = []
    for data in data_set:
        data_row = {}
        data_row['county_id'] = data.county_id
        data_row['state'] = data.state
        data_row['county'] = data.county
        data_row['data_value'] = get_attribute(user_choice, data)
        json_data_set.append(data_row)
    return JsonResponse({'all_data': json_data_set})


def getmetadata(request):
    graph_name = request.GET.get('graph_name')
    map_data = MapData.objects.get(variable=graph_name)
    d = {'variable': map_data.variable,
         'header_text': map_data.header_text,
         'legend_text': map_data.legend_text,
         'upper_bound': map_data.upper_bound,
         'lower_bound': map_data.lower_bound}
    return JsonResponse(d)


def get_correlation(variable1, variable2):
    correlation_data = CorrelationData.objects.get(variable1=variable1, variable2=variable2)
    return correlation_data.correlation


def find_t(min_value, max_value, value):
    return (value - min_value) / (max_value - min_value)


def interpolate(a, b, t):
    return (1-t)*a + t*b


def interpolate_colors(color_a, color_b, t):
    return (interpolate(color_a[0], color_b[0], t),
            interpolate(color_a[1], color_b[1], t),
            interpolate(color_a[2], color_b[2], t))


def render_color(c):
    return f'rgb({int(c[0])},{int(c[1])},{int(c[2])})'


def find_color(min_value, max_value, value):

    orange = (255, 194, 102)
    blue = (0, 0, 255)
    white = (255, 255, 255)

    if value < 0:
        t = find_t(min_value, 0, value)
        return render_color(interpolate_colors(orange, white, t))
    else:
        t = find_t(0, max_value, value)
        return render_color(interpolate_colors(white, blue, t))


def render_correlation_matrix():
    mapdata = MapData.objects.all()
    variables = [md.variable for md in mapdata]

    correlations = [cd.correlation for cd in CorrelationData.objects.all()]
    min_value = min(correlations)
    max_value = max(correlations)

    t = '<table>'

    t += '<tr>'
    t += '<th></th>'
    for variable in variables:
        t += '<th>'+variable+'</th>'
    t += '</tr>'

    for variable1 in variables:
        t += '<tr><td>'+variable1+'</td>'
        for variable2 in variables:
            corr = get_correlation(variable1, variable2)
            t += '<td style="background-color:'+find_color(min_value, max_value, corr)+';text-align:center">'
            t += str(round(corr, 2))+'</td>'
        t += '</tr>'

    t += '</table>'
    return t


def correlation(request):
    mapdata = MapData.objects.all()

    user_choice1 = request.GET.get('v1')
    user_choice2 = request.GET.get('v2')

    correlation = ''

    if user_choice1 is not None and user_choice2 is not None:
        data_column1 = []
        data_column2 = []
        for data_row in AccessData.objects.all():
            datum1 = get_attribute(user_choice1, data_row)
            datum2 = get_attribute(user_choice2, data_row)
            if datum1 is not None and datum2 is not None:
                data_column1.append(float(datum1))
                data_column2.append(float(datum2))

        df = pd.DataFrame({'datum1': data_column1, 'datum2':data_column2})
        correlation = user_choice1+' x '+user_choice2+': '+str(df['datum1'].corr(df['datum2'], method='spearman'))

    context = {'mapdata': mapdata, 'correlation': correlation, 'table': render_correlation_matrix()}
    return render(request, 'capstone/correlation.html', context)


def scatterplot_data(request):
    user_choice1 = request.GET.get('v1')
    user_choice2 = request.GET.get('v2')

    data_set = AccessData.objects.all()
    json_data_set = []
    for data in data_set:
        data_row = {}
        data_row['county_id'] = data.county_id
        data_row['state'] = data.state
        data_row['county'] = data.county
        data_row['choice1'] = get_attribute(user_choice1, data)
        data_row['choice2'] = get_attribute(user_choice2, data)
        if data_row['choice1'] is not None and data_row['choice2'] is not None and data_row['choice1'] != 'nan' and data_row['choice2'] != 'nan':
            json_data_set.append(data_row)

    return JsonResponse({'all_data': json_data_set})


def scatterplot(request):
    mapdata = MapData.objects.all()
    context = {'mapdata': mapdata}

    return render(request, 'capstone/scatterplot.html', context)





