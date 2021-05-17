from djoser import email


class PasswordResetEmail(email.PasswordResetEmail):

    def get_context_data(self):
        # PasswordResetEmail can be deleted
        context = super().get_context_data()
        context["protocol"] = 'https'

        return context