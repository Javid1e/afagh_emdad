# transactions/tasks.py
from celery import shared_task
from .models import Transaction
from ..users.models import User


@shared_task
def notify_transaction(user_id, transaction_id):
    user = User.objects.get(id=user_id)
    transaction = Transaction.objects.get(id=transaction_id)
    user.notify(
        _("Transaction {type} of amount {amount} has been completed.").format(type=transaction.transaction_type, amount=transaction.amount)
    )
