
from django.urls import path, include
from .views import index

urlpatterns = [
    
    path('', index, name='home'),
    # path("<int:id>/delete", delete, name="delete")
    # 
]
