import requests
from iNaturalist.Common import convertToObservationResults

def get_all_observations_for_taxon(taxon_id):
    observations = []
    page_num = 1
    while True:
        url = 'https://api.inaturalist.org/v1/observations?taxon_id=' + str(taxon_id) + '&per_page=200&order=desc&order_by=created_at&page=' + str(page_num)

        json_results = requests.get(url).json()
        per_page = int(json_results["per_page"])
        num_results = len(json_results["results"])

        for observation in convertToObservationResults(json_results["results"]):
            observations.append(observation)

        if (per_page != num_results):
            return observations
        
        page_num += 1