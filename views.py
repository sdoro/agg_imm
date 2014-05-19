
from django.http import HttpResponse



def helloworld(request):
    return HttpResponse("Hello world")



from age_imm.models import *

def q1(request):
    elenco = ""
    for a in agenzia.objects.all().order_by('nomeAG'):
        elenco += "'%s' in %s, telefono: %s<br>" % (a.nomeAG,
            a.citta, a.telefono)
    return HttpResponse(elenco)



def ann(request, id):
    try:
        a = annuncio.objects.get(pk=id)
        return HttpResponse("data_a: %s, nomeAG: %s" % (a.data_a, a.nomeAG))
    except annuncio.DoesNotExist:
        return HttpResponse("Codice %s errato" % id)



def data_ann(request, mese, anno):
    a = annuncio.objects.filter(data_a__year=int(anno))
    a = a.filter(data_a__month=int(mese))
    elenco = ""
    for d in a.order_by('data_a'):
        elenco += "%s, %s,<br>" % (d.data_a, d.nomeAG)
        if elenco == "":
            elenco = "Nessun libro"
        return HttpResponse(elenco)


