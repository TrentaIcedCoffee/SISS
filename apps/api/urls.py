from utils.routes import *

from . import links, kuali_entries, sunapsis_entries

urlpatterns = [
    path('links/', links.index),
    path('kuali_entries/', kuali_entries.index),
    path('kuali_entries/<int:ke_id>/', kuali_entries.id),
    path('sunapsis_entries/', sunapsis_entries.index),
    path('sunapsis_entries/<int:se_id>/', sunapsis_entries.id),
]
