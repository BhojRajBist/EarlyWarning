# # urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('analyze/<int:floodextent_id>/', views.analyze_flood_extent, name='analyze_flood_extent'),
#     # Add other URLs as needed
# ]



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('flood-zones-map/', views.flood_zones_map, name='flood_zones_map'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('analyze/<int:floodextent_id>/', views.analyze_flood_extent, name='analyze_flood_extent'),
    path('map/<int:floodextent_id>/', views.flood_zones_map, name='flood_zones_map'),
]
