from django.http import HttpResponse
from django.shortcuts import render
import json

def index(request):
    return HttpResponse("Hello, world!")


def indexRender(request):
    return render(request, 'index.html', {})


def universityInfo(request):
    file = open("./templates/json_data.json", "r").read()
    data = json.loads(file)
    f_sum = 0
    c_sum = 0
    s_num = 0
    s = 0
    for i in data["scientific"]["mega_faculties"]:
        f_sum += len(i["faculties"])
        for j in i["faculties"]:
            c_sum += len(j['cathedras'])
            for k in j['cathedras']:
                for a in k['educational_programs']:
                    for b in a['years']['groups']:
                        s_num += len(b['students'])

    s = f_sum + c_sum + len(data["scientific"]["mega_faculties"])

    return render(request, 'universityInfo.html', {"data": data, 'f_num': f_sum, 'c_num': c_sum,
        'admin_num': len(data["administrative"].keys()),
        'science_num': s, 'mf_num': len(data["scientific"]['mega_faculties']),
        'stud_num': s_num})


def disciplineInfo(request):
    file = open("./templates/json_data.json", "r").read()
    data = json.loads(file)
    educ_prog = data['scientific']['mega_faculties'][0]['faculties'][0]['cathedras'][0]['educational_programs'][0]
    return render(request, 'disciplineInfo.html', {'prog_name': educ_prog['program_name'],
           'prog_num': educ_prog['program_number'], 'prog_discipline': educ_prog['discipline'],
           'year': educ_prog['years']['year'], 'group_num': len(educ_prog['years']['groups'])})


def groupsInfo(request):
    file = open("./templates/json_data.json", "r").read()
    data = json.loads(file)
    groups = data['scientific']['mega_faculties'][0]['faculties'][0]['cathedras'][0]['educational_programs'][0]['years']['groups']
    return render(request, 'groupsInfo.html', {'mf': data['scientific']['mega_faculties']})


def departmentsInfo(request):
    file = open("./templates/json_data.json", "r").read()
    data = json.loads(file)
    return render(request, 'departmentsInfo.html', {'mf': data['scientific']['mega_faculties']})


def universityStructureInfo(request):
    file = open("./templates/json_data.json", "r").read()
    data = json.loads(file)
    return render(request, 'universityStructure.html', {'data': data, 'rectorate': data['administrative']['rectorate'], 'bookkeeping': data['administrative']['bookkeeping'],
        'mf': data['scientific']['mega_faculties']})
