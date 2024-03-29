"""gnuhealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('health.urls')),
    path('health-account/', include('health_account.urls')),
    path('health-account-invoice/', include('health_account_invoice.urls')),
    path('health-account-invoice-stock/', include('health_account_invoice_stock.urls')),
    path('health-account-product/', include('health_account_product.urls')),
    path('health-archives/', include('health_archives.urls')),
    path('health-caldav/', include('health_caldav.urls')),
    path('health-calendar/', include('health_calendar.urls')),
    path('health-company/', include('health_company.urls')),
    path('health-country/', include('health_country.urls')),
    path('health-crypto/', include('health_crypto.urls')),
    path('health-crypto-lab/', include('health_crypto_lab.urls')),
    path('health-currency/', include('health_currency.urls')),
    path('health-disability/', include('health_disability.urls')),
    path('health-ems/', include('health_ems.urls')),
    path('health-federation/', include('health_federation.urls')),
    path('health-genetics/', include('health_genetics.urls')),
    path('health-genetics-uniprot/', include('health_genetics_uniprot.urls')),
    path('health-gyneco/', include('health_gyneco.urls')),
    path('health-history/', include('health_history.urls')),
    path('health-icd10/', include('health_icd10.urls')),
    path('health-icd10pcs/', include('health_icd10pcs.urls')),
    path('health-icd9procs/', include('health_icd9procs.urls')),
    path('health-icpm/', include('health_icpm.urls')),
    path('health-icu/', include('health_icu.urls')),
    path('health-imaging/', include('health_imaging.urls')),
    path('health-inpatient/', include('health_inpatient.urls')),
    path('health-inpatient-calendar/', include('health_inpatient_calendar.urls')),
    path('health-insurance/', include('health_insurance.urls')),
    path('health-iss/', include('health_iss.urls')),
    path('health-lab/', include('health_lab.urls')),
    path('health-lifestyle/', include('health_lifestyle.urls')),
    path('health-mdg6/', include('health_mdg6.urls')),
    path('health-ntd/', include('health_ntd.urls')),
    path('health-ntd-chagas/', include('health_ntd_chagas.urls')),
    path('health-ntd-dengue/', include('health_ntd_dengue.urls')),
    path('health-nursing/', include('health_nursing.urls')),
    path('health-ophthalmology/', include('health_ophthalmology.urls')),
    path('health-party/', include('health_party.urls')),
    path('health-pediatrics/', include('health_pediatrics.urls')),
    path('health-pediatrics-growth-charts/', include('health_pediatrics_growth_charts.urls')),
    path('health-pediatrics-growth-charts-who/', include('health_pediatrics_growth_charts_who.urls')),
    path('health-product/', include('health_product.urls')),
    path('health-profile/', include('health_profile.urls')),
    path('health-purchase/', include('health_purchase.urls')),
    path('health-purchase-request/', include('health_purchase_request.urls')),
    path('health-party/', include('health_party.urls')),
    path('health-nursing/', include('health_nursing.urls')),
    path('health-nursing/', include('health_nursing.urls')),
    path('health-nursing/', include('health_nursing.urls')),
    path('health-nursing/', include('health_nursing.urls')),
    
]
