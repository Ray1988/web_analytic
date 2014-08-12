from django.shortcuts import HttpResponseRedirect, render, render_to_response, RequestContext
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.
def home(request):
    form=SignUpForm(request.POST or None)
    top_views_stories=[{'s1':2}, {'s2':1}]
    top_reads_stories=[{'s1':2}, {'s2':1}]
    top_recs_stories=[{'s1':2}, {'s2':1}]
   
    if form.is_valid():
        save_it=form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thanks')
        return HttpResponseRedirect('/thank-you/')
        
    return render_to_response('views_reads_recs.html',
                              locals(),
                              context_instance=RequestContext(request))
def thankyou(request):
    
        
    return render_to_response('thankyou.html',
                              locals(),
                              context_instance=RequestContext(request))