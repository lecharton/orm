from django.db import models
from django.db.models import UniqueConstraint

from django.utils.translation import gettext as _

from django.contrib.auth import get_user_model

User = get_user_model()


class Pilot(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birth_date = models.DateField()

    human = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    UniqueConstraint(fields=['name', 'surname'], name='name_surname')

    # def __str__(self):
    #     return f"{self.name} {self.surname}"


class SpaceShips(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
    )
    ship_class = models.CharField(
        max_length=200,
        verbose_name='Class',
    )
    description = models.TextField()

    class ShipTypes(models.TextChoices):
        FRIGATE = 'FR', _('Frigate')
        RACING_SHIP = 'RA', _('Racing ship')

    ship_types = models.CharField(
        max_length=2,
        choices=ShipTypes.choices,
        default=ShipTypes.FRIGATE,
        verbose_name='Type'
    )

    pilot = models.ForeignKey(Pilot,
        on_delete=models.SET_NULL,
        related_name="space_ships",
        # related_name='+', - чтобы у пилота не создавалось обратное поле
        blank=True,
        null=True
    )

    is_broken = models.BooleanField(default=False)

    class Meta:
        ordering = ("-name",)
        # abstract = True
        # db_table = 'spaceships'

    def __str__(self):
        return self.name

# python manage.py shell
# from expanse.models import SpaceShips, Pilot
# pilot = Pilot(name='James', surname='Holden', birth_date='2010-07-09')
# Pilot.objects.all().query
# pilot.save()
# ship = SpaceShips(name='Rocinante', ship_class='Corvette', description='Roci', ship_types='FR')
# ship.save()
# ship.pilot = pilot
# ship.save()
# pilot = Pilot.objects.get(name='James')
# pilot.space_ships.all()
# roci = SpaceShips.objects.get(name='Rocinante')
# roci.ship_types
# roci.get_ship_types_display()
# ship = SpaceShips(name='Razorback', ship_class='Racing Pinnace', description='Proserpina Starworks Sunflare', ship_types='RA')
# ship = SpaceShips(name='Anubis', ship_class='Amun-Ra-class stealth', description='Amun-Ra-class stealth frigate', ship_types='FR')
# order?
# Pilot.objects.filter(name__contains='J')
# Pilot.objects.filter(birth_date__gt='2000-01-01')
# Pilot.objects.filter(birth_date__year=2010)