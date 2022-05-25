from django.db import models


class PredResults(models.Model):

    mass_2 = models.FloatField()
    mass_zeta_potential = models.FloatField()
    mass_concentration = models.FloatField()
    mass_ev = models.FloatField()
    concentration_2 = models.FloatField()
    zeta_potential_2 = models.FloatField()
    zeta_potential_concentration = models.FloatField()
    concentration_toxicity = models.FloatField()
    zeta_potential_toxicity = models.FloatField()
    mass = models.FloatField()
    energy_source = models.FloatField()
    shape_Janus = models.FloatField()
    concentration_ev = models.FloatField()
    toxicity = models.FloatField()
    bioapplicable = models.FloatField()

    def __float__(self):
        return self.bioapplicable
