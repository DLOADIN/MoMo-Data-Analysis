from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from datetime import datetime
from .models import (
    AirtimePayments,
    MoneyRecieved,
    TransfersToMomo,
    BankDeposits,
    PaymentToCode,
    CashPowerPayments,
    Withdrawals,
    PaymentsToThirdParties,
    BundlesAndPacks,
)


# Create your views here.
def home(request):
    return render(request, "momo/index.html")


def airtime(request):
    return render(
        request, "momo/data.html", {"airtime": AirtimePayments.objects.all()}
    )


def transfers_to_momo(request):
    return render(
        request, "momo/momotransfer.html", {"momotransfers": TransfersToMomo.objects.all()}
    )


def bankdeposits(request):
    return render(request, "momo/bankdepo.html", {"bankdepo": BankDeposits.objects.all()})


def payment_to_code(request):
    return render(
        request, "momo/paymenttocode.html", {"paymenttocode": PaymentToCode.objects.all()}
    )


def cashpower_payments(request):
    return render(
        request, "momo/cashpower.html", {"cashpower": CashPowerPayments.objects.all()}
    )


def payments_to_third_parties(request):
    return render(
        request, "momo/transactions.html", {"transactions": PaymentsToThirdParties.objects.all()}
    )


def withdrawals(request):
    return render(request, "momo/withdrawals.html", {"withdrawals": Withdrawals.objects.all()})


def bundles_and_packs(request):
    return render(
        request, "momo/data.html", {"data": BundlesAndPacks.objects.all()}
    )


def moneyreceived(request):
    return render(
        request, "momo/incomingmoney.html", {"moneyrecieved": MoneyRecieved.objects.all()}
    )

# working on bar charts
def data_chart(request):

    # total transactions volume by type
    transactions_data = {
        "Airtime Payments": AirtimePayments.objects.aggregate(total=Sum("amount"))["total"] or 0,
        "Bank Deposits": BankDeposits.objects.aggregate(total=Sum("amount"))["total"] or 0,
        "Bundles & Packs": BundlesAndPacks.objects.aggregate(total=Sum("amount"))["total"] or 0,
        "Cash Power Payments": CashPowerPayments.objects.aggregate(total=Sum("amount"))["total"] or 0,
        "Money Received": MoneyRecieved.objects.aggregate(total=Sum("amount"))["total"] or 0,
        "Payments to Code": PaymentToCode.objects.aggregate(total=Sum("amount"))["total"] or 0,
        "Third Party Payments": PaymentsToThirdParties.objects.aggregate(total=Sum("amount"))["total"] or 0,
        "Transfers to Momo": TransfersToMomo.objects.aggregate(total=Sum("amount"))["total"] or 0,
        "Withdrawals": Withdrawals.objects.aggregate(total=Sum("amount"))["total"] or 0,
    }

    def get_monthly_data(model):
        return (
            model.objects.extra(select={'month': "strftime('%%Y-%%m', date)"})
            .values("month")
            .annotate(total=Sum("amount"))
            .order_by("month")
        )

    monthly_summary = []
    for model in [AirtimePayments, BankDeposits, BundlesAndPacks, CashPowerPayments, MoneyRecieved, PaymentsToThirdParties, PaymentToCode, TransfersToMomo, Withdrawals]:
        monthly_summary.extend(get_monthly_data(model))

    # Aggregate by month
    monthly_aggregated = {}
    for entry in monthly_summary:
        month = entry["month"]
        if month in monthly_aggregated:
            monthly_aggregated[month] += entry["total"]
        else:
            monthly_aggregated[month] = entry["total"]

    data = {
        "transactions_summary": transactions_data,
        "monthly_summary": [{"month": k, "total": v} for k, v in sorted(monthly_aggregated.items())],
    }
    
    return JsonResponse(data)

def dashboard(request):
    return render(request, "momo/dashboard.html")