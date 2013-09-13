from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from principal.models import Grados, Grupos
from principal.forms import GradoForm, GrupoForm

def inicio(request):
	return render_to_response('index.html',locals(),context_instance=RequestContext(request))

#Grados
def obtenerGrados():
	try:
		grados = Grados.objects.all()
	except Grados.DoesNotExist:
		grados = None
	return grados

def obtenerGradoPorID(id_grado):
	try:
		grado = Grados.objects.get(pk=id_grado)
	except Grados.DoesNotExist:
		grado = None
	return grado

def inicio_grados(request):
	grados = obtenerGrados()
	ctx ={
		"grados" : grados
	}
	return render_to_response("indexgrados.html", ctx)

def inicio_grupos(request):
	grupos = obtenerGrupos()
	ctx ={
		"grupos" : grupos
	}
	return render_to_response("indexgrupos.html", ctx)

def nuevoGrado(request):
	from principal.forms import GradoForm
	if request.method == "POST":
		form = GradoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/#agregado")
	else:
		form = GradoForm()
	ctx ={
		"formulario": form
	}
	return render_to_response("formgrados.html", ctx, context_instance=RequestContext(request))

def editarGrado(request, id_grado):
	grado = obtenerGradoPorID(id_grado)
	from principal.forms import GradoForm
	if request.method == "POST":
		form = GradoForm(request.POST, instance=grado)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/#editado")
	else:
		if grado:
			form = GradoForm(instance=grado)
		else:
			return HttpResponseRedirect("/#no-existe-ese-grado")
	ctx ={
		"formulario": form
	}
	return render_to_response("formgrados.html", ctx, context_instance=RequestContext(request))

def borrarGrado(request, id_grado):
	grado = obtenerGradoPorID(id_grado)
	if grado:
		grado.delete()
		return HttpResponseRedirect("/#eliminado")
	return HttpResponseRedirect("/#no-hay-grado-a-eliminar")

#Grupos
def obtenerGrupos():
	try:
		grupos = Grupos.objects.all()
	except Grupos.DoesNotExist:
		grupos = None
	return grupos

def obtenerGrupoPorID(id_grupo):
	try:
		grupo = Grupos.objects.get(pk=id_grupo)
	except Grupos.DoesNotExist:
		grupo = None
	return grupo

def nuevoGrupo(request):
	from principal.forms import GrupoForm
	if request.method == "POST":
		form = GrupoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/#agregado")
	else:
		form = GrupoForm()
	ctx ={
		"formulario": form
	}
	return render_to_response("formgrupos.html", ctx, context_instance=RequestContext(request))

def editarGrupo(request, id_grupo):
	grupo = obtenerGrupoPorID(id_grupo)
	from principal.forms import GrupoForm
	if request.method == "POST":
		form = GrupoForm(request.POST, instance=grupo)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/#editado")
	else:
		if grupo:
			form = GrupoForm(instance=grupo)
		else:
			return HttpResponseRedirect("/#no-existe-ese-grupo")
	ctx ={
		"formulario": form
	}
	return render_to_response("formgrupos.html", ctx, context_instance=RequestContext(request))

def borrarGrupo(request, id_grupo):
	grupo = obtenerGrupoPorID(id_grupo)
	if grupo:
		grupo.delete()
		return HttpResponseRedirect("/#eliminado")
	return HttpResponseRedirect("/#no-hay-grupo-a-eliminar")
