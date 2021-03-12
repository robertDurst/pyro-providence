from iNaturalist.ApiRequests import get_all_observations_for_taxon
from iNaturalist.Constants import TAXON_ID_DICT, TIME_PRETTY_PRINT_DICT, MONTH_PRETTY_PRINT_DICT
from iNaturalist.Common import sortObservationsByHour, sortObservationsByMonth

def view_taxa_frequency_by_month_overall(taxa):
    taxon_id = TAXON_ID_DICT[taxa]
    if (taxon_id == None):
        print("Unrecognized taxa.")

    obs = get_all_observations_for_taxon(taxon_id)
    obsSortedByMonth = sortObservationsByMonth(obs)

    print("Per Month Frequencies of (" + taxa + "):")
    for hour, value in sorted(obsSortedByMonth.items()):
        print(MONTH_PRETTY_PRINT_DICT[hour] + ": " + str(len(value)))

def view_taxa_frequency_by_hour_overall(taxa):
    taxon_id = TAXON_ID_DICT[taxa]
    if (taxon_id == None):
        print("Unrecognized taxa.")

    obs = get_all_observations_for_taxon(taxon_id)
    obsSortedByHour = sortObservationsByHour(obs)

    print("Per Hour Frequencies of (" + taxa + "):")
    for hour, value in sorted(obsSortedByHour.items()):
        print(TIME_PRETTY_PRINT_DICT[hour] + ": " + str(len(value)))

def view_taxa_frequency_by_hour_for_month(taxa, month):
    taxon_id = TAXON_ID_DICT[taxa]
    if (taxon_id == None):
        print("Unrecognized taxa.")

    if (month < 1 or month > 12):
        print("Invalid month.")

    obs = get_all_observations_for_taxon(taxon_id)
    obsSortedByMonth = sortObservationsByMonth(obs)
    obsSortedByHourForMonth = sortObservationsByHour(obsSortedByMonth[month])

    print("Per Hour Frequencies of (" + taxa + ") during " + MONTH_PRETTY_PRINT_DICT[month]  + ":")
    for hour, value in sorted(obsSortedByHourForMonth.items()):
        print(TIME_PRETTY_PRINT_DICT[hour] + ": " + str(len(value)))
