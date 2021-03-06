flu_url = 'https://data.cityofchicago.org/api/views/rfdj-hdmf/rows.csv?accessType=DOWNLOAD'
flu_path = 'Flu_Shot_Clinic_Locations_-_2013.csv'

flu_shot_meta = {
    'dataset_name': u'flu_shot_clinics',
    'human_name': u'Flu Shot Clinic Locations',
    'attribution': u'foo',
    'description': u'bar',
    'url': flu_url,
    'update_freq': 'yearly',
    'business_key': u'event',
    'observed_date': u'date',
    'latitude': u'latitude',
    'longitude': u'longitude',
    'location': None,
    'contributor_name': u'Carlos',
    'contributor_organization': u'StrexCorp',
    'contributor_email': u'foo@bar.edu',
    'contributed_data_types': None,
    'approved_status': 'true',
    'is_socrata_source': False,
    'column_names': {"date": "DATE", "start_time": "VARCHAR", "end_time": "VARCHAR", "facility_name": "VARCHAR",
                     "facility_type": "VARCHAR", "street_1": "VARCHAR", "city": "VARCHAR", "state": "VARCHAR",
                     "zip": "INTEGER", "phone": "VARCHAR", "latitude": "DOUBLE PRECISION",
                     "longitude": "DOUBLE PRECISION", "day": "VARCHAR", "event": "VARCHAR", "event_type": "VARCHAR",
                     "ward": "INTEGER", "location": "VARCHAR"}
}

landmarks_url = 'https://data.cityofchicago.org/api/views/tdab-kixi/rows.csv?accessType=DOWNLOAD'
landmarks_path = 'Individual_Landmarks.csv'

landmarks_meta = {
    'dataset_name': u'landmarks',
    'human_name': u'Chicago Landmark Locations',
    'attribution': u'foo',
    'description': u'bar',
    'url': landmarks_url,
    'update_freq': 'yearly',
    'business_key': u'id',
    'observed_date': u'landmark_designation_date',
    'latitude': u'latitude',
    'longitude': u'longitude',
    'location': u'location',
    'contributor_name': u'Cecil Palmer',
    'contributor_organization': u'StrexCorp',
    'contributor_email': u'foo@bar.edu',
    'contributed_data_types': None,
    'approved_status': 'true',
    'is_socrata_source': False,
    'column_names': {"foo": "bar"}
}

crime_url = 'http://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD'
crime_path = 'crime_sample.csv'

crime_meta = {
    'dataset_name': u'crimes',
    'human_name': u'Crimes',
    'attribution': u'foo',
    'description': u'bar',
    'url': crime_url,
    'update_freq': 'yearly',
    'business_key': u'id',
    'observed_date': u'date',
    'latitude': u'latitude',
    'longitude': u'longitude',
    'location': u'location',
    'contributor_name': u'Dana Cardinal',
    'contributor_organization': u'City of Nightvale',
    'contributor_email': u'foo@bar.edu',
    'contributed_data_types': None,
    'approved_status': 'true',
    'is_socrata_source': False,
    'column_names': {"foo": "bar"}
}
