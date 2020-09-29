from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests
import json
from jobs.models import Job
from scraping.management.commands.helpers import weworkremotey_jobs, remoteok_jobs, employremotely_jobs, github_jobs, hackerrank_jobs, pythonorg_jobs, remoteco_jobs, remotive_jobs, stackoverflow_jobs
class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command
    def handle(self, *args, **options):
        weworkremotey_jobs()
        remoteco_jobs()
        remoteok_jobs()
        # remotive_jobs()
        employremotely_jobs()
        stackoverflow_jobs()
        hackerrank_jobs()
        github_jobs()
        pythonorg_jobs()

        self.stdout.write( '\n................\njob scraping completed' )
    

    