from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()
