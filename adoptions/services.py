from .models import AdoptionPreference, Cat, AdoptionMatch
from django.utils import timezone

def matching_for_user(user):
    user_preference = AdoptionPreference.objects.filter(user=user).exists()
    if user_preference:
        preference = AdoptionPreference.objects.get(user=user)
        cats = Cat.objects.all()

        if preference.preferred_breed:
            cats = cats.filter(breed = preference.preferred_breed)

        if preference.preferred_gender != 'A':
            cats = cats.filter(gender=preference.preferred_gender)

        cats = cats.filter(
            age__gte=preference.age_min,
            age__lte=preference.age_max
        )
        cats = cats[:5]
    else:
        cats = Cat.objects.order_by('id')[:5]


    AdoptionMatch.objects.filter(user=user).delete()


    matches = []
    for cat in cats:
        match = AdoptionMatch.objects.create(
            user=user,
            cat=cat,
            matched_at=timezone.now()
        )
        matches.append(match)


    return matches






