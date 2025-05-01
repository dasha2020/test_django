from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
from albums.forms import ForgotForm
import smtplib
from email.mime.text import MIMEText
import random
import string

me = 'dariia.d57@gmail.com'
you = 'user@example.com'
password = 'rwbk cvsv zvpv ajzk'




class ForgotPassView(FormView):
    template_name = 'forgot_pass.html'
    form_class = ForgotForm
    success_url = reverse_lazy('check_email')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        new_password1 = []
        for i in range(8):
            new_password = random.choice(string.digits)
            new_password1.append(new_password)
        message = ''.join(new_password1)
        root = '\nFollow this root -> http://127.0.0.1:8000/change_pass'
        message += root
        you = email
        msg = MIMEText(message)
        msg['Subject'] = 'New password'
        msg['From'] = me
        msg['To'] = you

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(me, password)
            server.sendmail(me, [you], msg.as_string())
        
        self.request.session['email_for_pass_change'] = email
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)