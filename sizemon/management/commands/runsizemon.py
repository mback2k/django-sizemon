from django.core.management.base import BaseCommand, CommandError
from sizemon.models import Snapshot, Path
import subprocess

class Command(BaseCommand):
    help = 'Runs the du programm to measure the size of all file system paths'

    def handle(self, *args, **kwargs):
        process = subprocess.Popen(['du', '--exclude=/proc/*', '/'], shell=False, stdout=subprocess.PIPE)

        stdout, stderr = process.communicate()

        snapshot = Snapshot.objects.create()

        for line in stdout.split('\n'):
            if '\t' in line:
                size, path = line.split('\t', 2)

                Path.objects.create(snapshot=snapshot, path=path, size=size)
