from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import User, Profile
from .tasks import send_email_task, send_sms_task, send_push_notification_task
from django.utils.translation import gettext_lazy as _


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Handle logic for when a user is created
        print(_("A new user was created: {}").format(instance.username))

        # Create user profile
        Profile.objects.create(user=instance)

        # Send notifications
        send_email_task.delay(
            _('Welcome to Afagh Emdad'),
            _('Dear {},\n\nWelcome to Afagh Emdad! We are glad to have you.').format(instance.name),
            [instance.email]
        )
        send_sms_task.delay(
            instance.phone_number,
            _('Welcome to Afagh Emdad, {}!').format(instance.name)
        )
        send_push_notification_task.delay(
            instance.id,
            _('Welcome to Afagh Emdad'),
            _('Welcome to Afagh Emdad, {}!').format(instance.name)
        )
    else:
        # Handle logic for when a user is updated
        print(_("User profile updated: {}").format(instance.username))

        # Notify the user about profile update via email
        send_email_task.delay(
            _('Profile Updated'),
            _('Dear {},\n\nYour profile has been updated successfully.').format(instance.name),
            [instance.email]
        )
        send_push_notification_task.delay(
            instance.id,
            _('Profile Updated'),
            _('Your profile has been updated successfully, {}.').format(instance.name)
        )


@receiver(pre_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    # Handle logic for when a user is deleted
    print(_("User deleted: {}").format(instance.username))

    # Notify the user about account deletion via email
    send_email_task.delay(
        _('Account Deletion'),
        _('Dear {},\n\nYour account has been deleted as per your request.').format(instance.name),
        [instance.email]
    )
    send_sms_task.delay(
        instance.phone_number,
        _('Your account has been deleted, {}.').format(instance.name)
    )
    send_push_notification_task.delay(
        instance.id,
        _('Account Deletion'),
        _('Your account has been deleted, {}.').format(instance.name)
    )
