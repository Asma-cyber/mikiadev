from django.shortcuts import render
from .models import Testimonial
from .forms import TestimonialForm

def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    form = TestimonialForm()
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        'testimonials': testimonials,
        'form': form,
    }
    return render(request, 'testimonial.html', context)
