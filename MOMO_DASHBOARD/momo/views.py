from django.shortcuts import render
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
