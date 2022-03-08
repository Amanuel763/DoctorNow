from django.shortcuts import get_object_or_404, render
from .models import Doc
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def doctor(request):
    all_docs = Doc.objects.order_by('-created_date')
    paginator = Paginator(all_docs, 2)
    page = request.GET.get('page')
    paged_doctors = paginator.get_page(page)

    data = {
        'all_docs': paged_doctors,
    }

    return render(request, 'pages/findadoctor.html', data)

def doctor_detail(request, id):
    single_doc = get_object_or_404(Doc, pk=id)
    
    data = {
        'single_doc': single_doc,
    }

    return render(request, 'pages/doctor_detail.html', data)