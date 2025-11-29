from django.urls import path # helps us import the method path for our endpoints
from .import views # import veiws from the current root directory

    # endpoints + target view functions
urlpatterns = [
        path('home', views.home, name='home'), # endpoint for home page
        path('create-Shoe', views.createShoe, name='createShoe'),
        path('shoes',views.readShoe,name='readShoe'),
        path('shoe/<int:pk>/', views.shoe_detail, name='shoe_detail'),
        path('update-one-shoe/<str:pk>', views.updateShoe, name='updateShoe'),
        path('delete-shoe/<str:pk>', views.deleteShoe, name='deleteShoe'),
    ]