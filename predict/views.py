from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults


def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        mass_2 = float(request.POST.get('mass_2'))
        mass_zeta_potential = float(request.POST.get('mass_zeta_potential'))
        mass_concentration = float(request.POST.get('mass_concentration'))
        mass_ev = float(request.POST.get('mass_ev'))
        concentration_2 = float(request.POST.get('concentration_2'))
        zeta_potential_2 = float(request.POST.get('zeta_potential_2'))
        zeta_potential_concentration = float(
            request.POST.get('zeta_potential_concentration'))
        concentration_toxicity = float(
            request.POST.get('concentration_toxicity'))
        zeta_potential_toxicity = float(
            request.POST.get('zeta_potential_toxicity'))
        mass = float(request.POST.get('mass'))
        energy_source = float(request.POST.get('energy_source'))
        shape_Janus = float(request.POST.get('shape_Janus'))
        concentration_ev = float(request.POST.get('concentration_ev'))
        toxicity = float(request.POST.get('toxicity'))

        # Unpickle model
        model = pd.read_pickle(
            r"C:\Users\ivano\Dissertation\Code\new_model.pickle")
        # Make prediction
        result = model.predict(
            [[mass_2, mass_zeta_potential, mass_concentration, mass_ev, concentration_2, zeta_potential_2,
              zeta_potential_concentration, concentration_toxicity, zeta_potential_toxicity,
              mass, energy_source, shape_Janus, concentration_ev, toxicity]])

        bioapplicable = result[0]

        PredResults.objects.create(mass_2=mass_2, mass_zeta_potential=mass_zeta_potential,
                                   mass_concentration=mass_concentration, mass_ev=mass_ev, concentration_2=concentration_2,
                                   zeta_potential_2=zeta_potential_2, zeta_potential_concentration=zeta_potential_concentration,
                                   concentration_toxicity=concentration_toxicity, zeta_potential_toxicity=zeta_potential_toxicity,
                                   mass=mass, energy_source=energy_source, shape_Janus=shape_Janus, concentration_ev=concentration_ev,
                                   toxicity=toxicity, bioapplicable=bioapplicable)

        return JsonResponse({'result': bioapplicable, 'mass_2': mass_2, 'mass_zeta_potential': mass_zeta_potential,
                             'mass_concentration': mass_concentration, 'mass_ev': mass_ev, 'concentration_2': concentration_2,
                             'zeta_potential_2': zeta_potential_2, 'zeta_potential_concentration': zeta_potential_concentration,
                             'concentration_toxicity': concentration_toxicity, 'zeta_potential_toxicity': zeta_potential_toxicity,
                             'mass': mass, 'energy_source': energy_source, 'shape_Janus': shape_Janus,
                             'concentration_ev': concentration_ev, 'toxicity': toxicity},
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
