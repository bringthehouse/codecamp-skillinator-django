from django.views.generic import *
from django.http import JsonResponse, HttpResponse

from skillsmatrix.view import *
from skillsmatrix.models import *

import json

from django.views.decorators.csrf import csrf_exempt

class DeveloperListView(ListView):
    model = Developer

    # def get_queryset(self):
    #     q = super(DeveloperListView,self).get_queryset()
    #     return q.select_related('user')




    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(dict(developer_list=list(context['developer_list'].values())))



# def function(request, pk):
#     developer = get_object_or_404(Developer, id=pk)
#     return render(...)

class DeveloperDetailView(DetailView):
    model = Developer

    def get_queryset(self):
        q = super(DeveloperDetailView,self).get_queryset()
        return q.filter(user_id=1)






    def render_to_response(self, context, **response_kwargs):
        return JsonResponse({
            'id': self.object.id,
            'manager': self.object.manager,
            'user_id': self.object.user_id,
            'extra_credit_tokens': self.object.extra_credit_tokens,
        })


class SkillListView(ListView):
    model = Skill

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(dict(skill_list=list(context['skill_list'].values())))




class SkillCreateView(CreateView):
    model = Skill
    fields = ['name', 'difficulty', 'family']

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'difficulty': self.object.difficulty,
            'family': self.object.family
        })

    def form_invalid(self, form):
        if form.errors:
            return JsonResponse(form.errors, status=400)
        else:
            return JsonResponse({'error': True, 'message': 'Error creating skill!'})

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(SkillCreateView,self).dispatch(request, *args, **kwargs)

class DeveloperUpdateView(UpdateView):
    model = Developer
    fields = ['extra_credit_tokens', 'manager', 'title']

    def get_queryset(self):
        q = super(DeveloperUpdateView,self).get_queryset()
        return q.filter(user_id=1)

    def form_valid(self, form):
        form.instance.user = self.request.user

        self.object = form.save()
        return JsonResponse({
            'id': self.object.id,
            'title': self.object.title,
            'manager': self.object.manager,
            'extra_credit_tokens': self.object.extra_credit_tokens
        })

    def form_invalid(self, form):
        if form.errors:
            return JsonResponse(form.errors, status=400)
        else:
            return JsonResponse({'error': True, 'message': 'Error creating skill!'})

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(DeveloperUpdateView,self).dispatch(request, *args, **kwargs)
