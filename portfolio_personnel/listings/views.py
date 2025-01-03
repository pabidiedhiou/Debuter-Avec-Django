from django.http import HttpResponse
from listings.models import Groupe
from listings.forms import ContactUsForm, GroupeForm
from django.core.mail import send_mail
from django.shortcuts import render,redirect

def contactUs(request):
    if request.method == 'POST':
        form= ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f' Message de {form.cleaned_data["nom"] or "anonyme"} via Merchex',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz']
            )
            return redirect('groupes-list')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form':form})



def groupes_list(request):
    groupes = Groupe.objects.all()
    return render(request, "listings/groupe_list.html", {'groupes': groupes} )

def groupe_detail(request, groupe_id):
    groupe = Groupe.objects.get(id=groupe_id)
    return render(request, "listings/groupe_detail.html", {"groupe": groupe})

def listings(request):
    return HttpResponse("<h1>Liste des annonces pour les articles</h1>")

def creer_groupe(request):
    if request.method == 'POST':
        form = GroupeForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Groupe » et la sauvegarder dans la BD
            groupe = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('groupe-detail', groupe.id)
    else:
        form = GroupeForm()
    
    return render(request, 'listings/creer_groupe.html', {"form": form})

def modifie_groupe(request, groupe_id):
    groupe = Groupe.objects.get(id=groupe_id)
    if request.method == 'POST':
        form = GroupeForm(request.POST, instance=groupe)
        if form.is_valid():
            form.save()
            return redirect('groupe-detail', groupe.id)
    else:
        form = GroupeForm(instance=groupe)
    return render(request, 'listings/modifie_groupe.html',{'form':form})

def supprime_groupe(request, groupe_id):
    groupe = Groupe.objects.get(id=groupe_id)
    if request.method == "POST":
        groupe.delete()
        return redirect("groupes-list")
    return render(request, 'listings/supprime_groupe.html', {'groupe': groupe})
