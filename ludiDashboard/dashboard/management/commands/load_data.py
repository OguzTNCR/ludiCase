import json
from django.core.management.base import BaseCommand
from dashboard.models import Company, Simulation, User
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "Load data from a JSON file into the database"

    def handle(self, *args, **kwargs):
        with open("dashboard/data/users.json") as user_file:
            users_data = json.load(user_file)["users"]

        with open("dashboard/data/simulations.json") as simulation_file:
            simulations_data = json.load(simulation_file)["simulations"]

        companies = {}
        simulations = {}

        for sim in simulations_data:
            company_id = sim["company_id"]
            if company_id not in companies:
                company = Company(
                    company_id=company_id, company_name=sim["company_name"]
                )
                company.save()
                companies[company_id] = company

            simulation = Simulation(
                simulation_id=sim["simulation_id"],
                simulation_name=sim["simulation_name"],
                company=companies[company_id],
            )
            simulation.save()
            simulations[sim["simulation_id"]] = simulation


        for user in users_data:
            simulation = simulations[user["simulation_id"]]
            signup_datetime = datetime(1899, 12, 30) + timedelta(days=user["signup_datetime"])
            user = User(
                user_id=user["user_id"],
                user_name=user["user_name"],
                user_surname=user["user_surname"],
                simulation=simulation,
                signup_datetime=signup_datetime,
                progress_percent=user["progress_percent"],
            )
            user.save()
