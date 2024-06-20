from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import ObtainAuthToken

from api import views




router=DefaultRouter()

router.register('register',views.SignUpView,basename='users')

router.register('expenses',views.ExpenseViewSet,basename='expenses')

router.register('incomes',views.IncomeViewSet,basename='incomes')


urlpatterns = [
    
    path('token/',ObtainAuthToken.as_view()),
    path('expenses/summary/',views.ExpenseSummaryView.as_view(),name="summary"),
    path('incomes/summary/',views.IncomeSummaryView.as_view())
    
]+router.urls