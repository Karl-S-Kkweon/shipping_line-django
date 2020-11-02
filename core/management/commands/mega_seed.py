import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django_seed import Seed
from owners.models import Owner
from hulls.models import Hull


class Command(BaseCommand):

    help = "It seeds the DB with tons of stuff"

    def handle(self, *args, **options):
        owner_seeder = Seed.seeder()
        owner_seeder.add_entity(
            Owner,
            30,
            {
                "name": lambda x: owner_seeder.faker.name(),
                "is_supervisor": False,
            },
        )
        owner_seeder.execute()

        owners = Owner.objects.all()
        hull_seeder = Seed.seeder()
        hull_seeder.add_entity(
            Hull,
            150,
            {
                "name": lambda x: owner_seeder.faker.street_address(),
                "no": lambda x: random.randint(100, 10000),
                "price": lambda x: random.randint(10000, 100000),
                "delivery_date": lambda x: datetime.now(),
            },
        )
        hull_seeder.execute()
        created_hulls = Hull.objects.all()
        for hull in created_hulls:
            for i in range(random.randint(1, 5)):
                hull.owners.add(random.choice(owners))

        self.stdout.write(self.style.SUCCESS("Everything seeded"))
