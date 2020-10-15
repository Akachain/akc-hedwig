from pyhelm.chartbuilder import ChartBuilder
from pyhelm.tiller import Tiller

tiller = Tiller(TILLER_HOST)
chart = ChartBuilder({"name": "nginx-ingress", "source": {"type": "repo", "location": "https://kubernetes-charts.storage.googleapis.com"}})
