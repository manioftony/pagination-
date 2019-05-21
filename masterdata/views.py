from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.list import ListView

# Create your views here.






class UserListView(ListView):
    model = User
    template_name = 'index.html'  # Default: <app_label>/<model_name>_list.html
    # context_object_name = 'users'  # Default: object_list
    paginate_by = 10
    # queryset = User.objects.all()  # Default: Model.objects.all()



    def get_queryset(self,*args, **kwargs):
        if  self.request.POST.get('username'):
            return User.objects.filter(email= self.request.POST.get('username'))
        elif self.request.GET.get('username'):
            return User.objects.filter(email= self.request.GET.get('username'))
        else:
            return User.objects.all()




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] =  self.request.POST.get('username','') or self.request.GET.get('username','')
        return context

    def post(self, request, *args, **kwargs):
        # self.queryset = self.filter(self.get_queryset())
        return super(UserListView, self).get(request, *args, **kwargs)







