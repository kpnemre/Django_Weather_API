
from django.urls import path, include
from .views import index,delete

urlpatterns = [
    
    path('', index, name='home'),
    path("delete/<int:id>", delete, name="delete")
    
]
