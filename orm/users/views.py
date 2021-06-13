from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from expanse.models import SpaceShips, Pilot


@login_required
def profile(request):
    user = request.user
    # user.get_full_name()
    # user.get_short_name()
    # user.set_unusable_password()
    # user.email_user(subject, message, from_email=None)

    # pilot = Pilot.objects.get(human=user)
    # pilot = Pilot.objects.get(human=1)
    pilot = Pilot.objects.get(human='James')

    ships = pilot.space_ships.all()

    # объекты пользователей сравниваем напрямую,
    # а не по username.
    # if pilot.human != request.user:
    #     return redirect('login')

    return render(request, "profile.html", {"pilot": pilot, "ships": ships})