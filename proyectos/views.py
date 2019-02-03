from django.shortcuts import render,redirect
from .models import proyecto,progreso
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from django.forms import inlineformset_factory,modelformset_factory,formset_factory


@login_required(login_url="/usuarios/login/")
def vista_proyectos(request):
    dataGrafica = []
    Pheader = ['Folio','Tomo', 'Enajenante','Adquirente','Fecha','Tipo']
    proyectos = proyecto.objects.all().filter(autor=request.user).order_by('fecha')
    numProyectos = len(proyectos)
    NumProgresosTerminados = len(progreso.objects.filter(estado=True))
    NumTotalProgreso = len(progreso.objects.all())
    progresos = progreso.objects.all().filter()

    for i in range(0,len(proyectos)):
        if len(progreso.objects.all().filter(estado=True)):
            dataGrafica.append(len(progreso.objects.all().filter(id_proyecto=proyectos[i].folio,estado=True)))
        else:
            dataGrafica.append(0)
    return render(request, 'proyectos/vista_general.html',{'proyectos': proyectos, 'Pheader':Pheader,'numProyectos':numProyectos,'dataGrafica':dataGrafica})
@login_required(login_url="/usuarios/login/")
def vista_detalle_proyecto(request,slug):
    proyect = proyecto.objects.get(slug=slug)
    #Progreso Todal de actividades con con ID del proyecto actual
    progeT =  len(progreso.objects.filter(id_proyecto=proyect.folio))
    #Cantidad de progreso terminado donde su estado sea Falso es decir no esta terminado
    NoTerminado = len(progreso.objects.filter(id_proyecto=proyect.folio,estado=False))
    a = progeT
    pro =  progreso.objects.filter(id_proyecto=proyect.folio)
    terminados = len(progreso.objects.filter(id_proyecto=proyect.folio,estado=True))
    form = modelformset_factory(progreso,fields=('estado',))
    formset = form(queryset=progreso.objects.filter(id_proyecto=proyect.folio,estado=False))
    return render(request,'proyectos/proyecto_detalles.html',{
    'proyect':proyect,'progress':a,'pro':pro,'NoTerminado':NoTerminado,
    'terminados':terminados,'formset':formset,'rango':range(NoTerminado)})

@login_required(login_url="/usuarios/login/")
def vista_proyectos_actuales(request):
        return render(request, 'proyectos/lista_proyectos.html')
        
@login_required(login_url="/usuarios/login/")
def vista_agregar_proyecto(request):
    if request.method == 'POST':
        form = forms.CrearProyecto(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autor = request.user;
            instance.save()
            return redirect('proyecto:actuales')
    else:
        form = forms.CrearProyecto()
        return render(request, 'proyectos/agregar_proyecto.html',{"form":form})
@login_required(login_url="/usuarios/login/")
def vista_agregar_progreso(request):
    if request.method == 'POST':
        formset = forms.AgregarProgreso(request.POST,user=request.user)
        if formset.is_valid():
            formset.save()
            return redirect('proyecto:actuales')
    else:
        form = forms.AgregarProgreso(user=request.user)
        return render(request,'proyectos/agregar_progreso.html',{'form':form})
@login_required(login_url="/usuarios/login/")
def agregar_progreso(request,id):
    if id:
        instance = progreso.objects.get(idProgreso=id)
        state = instance.estado
        proyecto_id = instance.id_proyecto_id
        p = proyecto.objects.get(folio=proyecto_id)
        slug = p.slug
        if state:
            state = False
            instance.estado = state
            instance.save()
            #return HttpResponse(proyecto_id)
            return redirect('/proyectos/%s' % slug)
        else:
            state = True
            instance.estado = state
            instance.save()
            #return HttpResponse(proyecto_id)
            return redirect('/proyectos/%s' % slug)
@login_required(login_url="/usuarios/login/")
def busqueda(request):
    query = request.GET.get('b')
    Pheader = ['Folio','Tomo', 'Enajenante', 'Adquirente','Proyectista','Fecha','Tipo']
    results = proyecto.objects.all().filter(enajenante=query)
    if not results:
        results = proyecto.objects.all().filter(adquirente=query)
    return render(request, 'proyectos/lista_proyectos_query.html',{'results':results,'Pheader':Pheader})
@login_required(login_url="/usuarios/login/")
def editar(request,id= None):
    proyect = proyecto.objects.get(folio=id)
    if request.method == 'POST':
        form = forms.CrearProyecto(request.POST,instance=proyect)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.autor = request.user;
            instance.save()
            return redirect('proyecto:actuales')
    else:
        form = forms.CrearProyecto(instance=proyect)
        return render(request, 'proyectos/editar.html', {"form":form})
