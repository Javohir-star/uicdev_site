from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Calls Javohir and if he does not answer, assumes he is working"

    def add_arguments(self, parser):
        parser.add_argument("work_name", nargs="+", type=str, default="")

    def handle(self, *args, **options):
        work_name = options["work_name"][0]
        import random

        javohir_response = random.choice([True, False])
        if javohir_response:
            self.stdout.write(self.style.SUCCESS("Javohir answered!"))
        else:
            self.stdout.write(self.style.WARNING(f"Javohir is {work_name}!"))