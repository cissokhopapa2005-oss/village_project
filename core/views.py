from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Actualite, Histoire


def home(request):
    actualites = Actualite.objects.order_by('-date_publication')[:3]
    histoire = Histoire.objects.order_by('id').first()
    if not histoire:
        histoire = Histoire(
            titre='Histoire de notre village',
            contenu=(
                'Notre village a été fondé au cœur d’un paysage de collines et de champs '
                'ouverts. Au fil des générations, il a conservé son identité, ses traditions '
                'et la chaleur de ses habitants. Aujourd’hui, il continue de vivre en harmonie '
                'entre patrimoine, nature et modernité.'
            )
        )
    return render(request, 'core/home.html', {'actualites': actualites, 'histoire': histoire})


def histoire_view(request):
    histoire = Histoire.objects.order_by('id').first()
    if not histoire:
        histoire = Histoire(
            titre='Histoire de notre village',
            contenu=(
                'Autrefois village de paysans et d’artisans, notre commune s’est développée '
                'autour de son église, de son marché et de ses chemins de randonnée. Ses habitants '
                'ont toujours su préserver la convivialité et le respect du patrimoine local.'
            )
        )
    return render(request, 'core/histoire.html', {'histoire': histoire})


def actualites(request):
    actualites = Actualite.objects.order_by('-date_publication')
    if not actualites:
        actualites = [
            Actualite(
                titre='Fête du village',
                contenu='Une journée de rencontre, de musique et de gastronomie est organisée pour tous.',
            ),
            Actualite(
                titre='Nettoyage du sentier',
                contenu='Les habitants se mobilisent pour entretenir les chemins et les espaces verts.',
            ),
            Actualite(
                titre='Marché local',
                contenu='Les producteurs de la région proposent leurs produits frais chaque samedi matin.',
            ),
        ]
    return render(request, 'core/actualites.html', {'actualites': actualites})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a bien été envoyé. Nous vous répondrons très bientôt.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})
