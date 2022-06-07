from django.shortcuts import render
from django.shortcuts import redirect
from .models import Pacient, Special, Skill, Employes, Diagnosis, DateOf
from django.contrib import messages
import getpass


def index(request):
    # отображение главной страницы
    return render(request, 'index.html', {
        'title': 'Главная страница',
    })


def deletePpl(request):
    if request.method == 'POST':
        id_ppl = request.POST['id_ppl']
        Pacient.objects.filter(id=id_ppl).delete()
        return redirect('reg')
    return redirect('reg')


def createPpl(request):
    if request.method == 'POST':
        sname = request.POST['second_name']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        bday = request.POST['bday']
        if (bday != '') & (sname != '') & (fname != '') & (lname != ''):
            Pacient.objects.create(
            name=fname,
            second_name=sname,
            last_name=lname,
            date_b=bday,
        )
            messages.error(request, 'Пациент успешно зарегистрирован', extra_tags='safe')
            return redirect('reg')
        else :
            return redirect('reg')
    else:
        return redirect('reg')


def reg(request):
    # отображение страницы регистрации
    pacient_all = Pacient.objects.all()
    return render(request, 'reg.html', {
        'title': 'Регистрация',
        'pacient_all': pacient_all,
    })


def creatediag(request):
    if request.method == 'POST':
        dname = request.POST['dname']
        dcost = request.POST['dcost']

        if (dname != '') & (dcost != ''):
            Diagnosis.objects.create(
            name=dname,
            cost=dcost,
        )
            return redirect('diagspec')
        else :
            return redirect('diagspec')
    else:
        return redirect('diagspec')


def createspec(request):

    if request.method == 'POST':
        spname = request.POST['spname']
        if (spname != ''):
            Special.objects.create(
            name=spname,
        )
            return redirect('diagspec')
        else :
            return redirect('diagspec')
    else:
        return redirect('diagspec')


def deleteddd(request):
    if request.method == 'POST':
        id_ddd = request.POST['id_ddd']
        Diagnosis.objects.filter(id=id_ddd).delete()
        return redirect('diagspec')
    return redirect('diagspec')


def deletesss(request):
    if request.method == 'POST':
        id_sss = request.POST['id_sss']
        Special.objects.filter(id=id_sss).delete()
        return redirect('diagspec')
    return redirect('diagspec')


def doctorspecial(request):
    if request.method =='POST':
        pac = request.POST['pac']
        vrac = request.POST['vrac']
        diagn = request.POST['diagn']
        dday = request.POST['dday']
        pac_id = Pacient.objects.get(id=pac)
        pac_name = Pacient.objects.get(id=pac).name
        pac_sname = Pacient.objects.get(id=pac).second_name
        pac_lname = Pacient.objects.get(id=pac).last_name
        pac_bday = Pacient.objects.get(id=pac).date_b
        vrac_id = Employes.objects.get(id=vrac)
        vrac_name = Employes.objects.get(id=vrac).name
        vrac_sname = Employes.objects.get(id=vrac).second_name
        vrac_lname = Employes.objects.get(id=vrac).last_name
        diagn_id = Diagnosis.objects.get(id=diagn)
        diagn_name = Diagnosis.objects.get(id=diagn).name
        skill_id = Employes.objects.get(id=vrac).skill.id
        koef = Skill.objects.get(id=skill_id).koef
        cost = Diagnosis.objects.get(id=diagn).cost
        print(skill_id)
        print(koef)
        print(cost)
        fcost = float(koef) * int(cost)
        if (pac != '') & (vrac != '') & (diagn != '') & (dday != ''):
            DateOf.objects.create(
                pacient=pac_id,
                emp=vrac_id,
                diag=diagn_id,
                dateoft=dday,
                costh=float(koef)*int(cost)
            )
            f = open('c:/users/' + getpass.getuser() + '/Desktop/' + pac_sname + '_' + str(pac_bday) + '_' + 'Дата_Посещения' + '_' + str(dday) + '.doc', 'w')
            f.write(
                'Расчетная Счёт-квитанция на оплату услуг поликлиники' + '\n' + '\n' +
                'Пациент: ' + pac_sname + ' ' + pac_name + ' ' + pac_lname + ' ' + str(pac_bday) + '\n' + '\n' +
                'Лечащий врач: ' + vrac_sname + ' ' + vrac_name + ' ' + vrac_lname + '\n' + '\n' +
                'Установленный диагноз: ' + diagn_name + '\n' + '\n' +
                'Стоимость оплаты: ' + str(fcost) + ' ' + 'Рублей' + '\n' + '\n' +
                'Дата посещения: ' + str(dday)
            )
            f.close()
            return redirect('dateof')
        else :
            return redirect('dateof')
    return redirect('dateof')


def deletedate(request):
    if request.method == 'POST':
        id_dto = request.POST['id_dto']
        DateOf.objects.filter(id=id_dto).delete()
        return redirect('dateof')
    return redirect('dateof')


def dateof(request):
    # отображение страницы регистрации
    pacient_all = Pacient.objects.all()
    emp_all = Employes.objects.all()
    diag_all = Diagnosis.objects.all()
    dateof_all = DateOf.objects.all()
    return render(request, 'dateof.html', {
            'title': 'Дата обращения',
            'pacient_all': pacient_all,
            'emp_all': emp_all,
            'diag_all': diag_all,
            'dateof_all': dateof_all,
        })


def deleteEmp(request):
    if request.method == 'POST':
        id_emp = request.POST['id_emp']
        Employes.objects.get(id=id_emp).delete()
        return redirect('employes')
    return redirect('employes')


def createEmp(request):
    if request.method == 'POST':
        sname = request.POST['second_name']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        special = request.POST['special']
        skill = request.POST['skill']
        skill_id = Skill.objects.get(id=skill)
        special_id = Special.objects.get(id=special)
        if (special != '') & (skill != '') & (sname != '') & (fname != '') & (lname != ''):
            Employes.objects.create(
            name=fname,
            second_name=sname,
            last_name=lname,
            special=special_id,
            skill=skill_id,
        )
            messages.error(request, 'Сотрудник успешно зарегистрирован', extra_tags='safe')
            return redirect('employes')
        else :
            return redirect('employes')
    else:
        return redirect('employes')









