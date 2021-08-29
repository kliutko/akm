from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)

    feedback = Feedback.objects.all()
    form = FeedbackForm()
    data = {
        'form' : form,
        'feedbacks' : feedback
    }
    return render(request, 'main/index.html', data)