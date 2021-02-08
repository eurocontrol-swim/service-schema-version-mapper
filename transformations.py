from jsonize import Transformation


def service_categorisation_transform(service_categorisation):
    try:
        input_geospatial = service_categorisation['geospatialCategorisation']
    except KeyError:
        return service_categorisation

    aerodrome = input_geospatial.get('aerodromeICAOLocationIndicator', None)
    state = input_geospatial.get('stateICAONationalityLetters', None)
    fir = input_geospatial.get('firICAOLocationIndicator', None)
    geospatial_categorisation = {}
    if aerodrome:
        geospatial_categorisation['aerodrome'] = aerodrome
    if state:
        geospatial_categorisation['countryCode'] = state
    if fir:
        geospatial_categorisation['fir'] = fir
    if input_geospatial:
        service_categorisation['geospatialCategorisation'] = geospatial_categorisation
    return service_categorisation


def interface_transform(interfaces):
    transformed = []
    for interface in interfaces:
        interface.pop('behaviour')
        interface['interfaceProtocol'] = []
        transformed.append(interface)
    return transformed


def service_provision_transform(service_provision):
    service_provision.pop('dateInOperation')
    service_provision.pop('serviceSupport')
    return service_provision


def point_of_contact_transform(points_of_contact):
    for point_of_contact in points_of_contact:
        point_of_contact['role'] = point_of_contact.pop('description')
        point_of_contact['contactInformation'] = [{'type': 'EMAIL',
                                                   'address': point_of_contact['email']}]
        if point_of_contact['phoneNumber']:
            point_of_contact['contactInformation'].append({'type': 'PHONE',
                                                           'address': point_of_contact['phoneNumber']})
        point_of_contact.pop('email')
        point_of_contact.pop('phoneNumber')
    return points_of_contact


interface_transformation = Transformation("interface_transformation", interface_transform)
categorisation_transformation = Transformation("service_categorisation_transformation", service_categorisation_transform)
service_provision_transformation = Transformation("service_provision_transformation", service_provision_transform)
point_of_contact_transformation = Transformation("point_of_contact_transformation", point_of_contact_transform)

transformations = [interface_transformation, categorisation_transformation, service_provision_transformation, point_of_contact_transformation]