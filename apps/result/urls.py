from django.urls import path
# from django.contrib import admin


from .views import ResultListView, create_result, edit_results

urlpatterns = [
    # path('adminresult/', admin.site.urls),

    path("create/", create_result, name="create-result"),
    path("edit-results/", edit_results, name="edit-results"),
    path("view/all", ResultListView.as_view(), name="view-results"),
]
