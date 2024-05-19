from django.shortcuts import render
from dashboard.models import Company, User
from django.db.models import Count
import json
from datetime import datetime, timedelta
from django.utils.timezone import make_naive


# Create your views here.


def company_users(request):
    companies = Company.objects.annotate(num_users=Count("simulation__user")).order_by("num_users")
    return render(request, "company_users.html", {"companies": companies})


def user_growth(request):
    oldest_signup = User.objects.order_by("signup_datetime").first().signup_datetime
    oldest_signup = make_naive(oldest_signup)
    newest_signup = User.objects.order_by("-signup_datetime").first().signup_datetime
    newest_signup = make_naive(newest_signup)
    date_range = [oldest_signup + timedelta(days=i) for i in range((newest_signup - oldest_signup).days + 1)]

    user_counts = []

    for date in date_range:
        user_count = User.objects.filter(signup_datetime__lte=date).count()
        user_counts.append({"date": date.strftime('%Y-%m-%d'), "user_count": user_count})


    return render(request, "user_growth.html", {"user_counts": json.dumps(user_counts)})

