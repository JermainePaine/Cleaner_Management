import mysql.connector

def get_all_services():
    cnx = mysql.connector.connect(user='root', password='r00tr00t',
                                  host='127.0.0.1',
                                  database='cleaner_management')

    cursor = cnx.cursor()

    query = ("SELECT service.service_id, service.name, Service.uom_id, Service.price_per_service, uom.uom_name FROM Service INNER JOIN uom on service.uom_id = uom.uom_id")

    cursor.execute(query,)

    response = []

    for (service_id, name, uom_id, price_per_service, uom_name) in cursor:
        response.append(
            {
                'service_id': service_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_service': price_per_service,
                'uom_name': uom_name
            }

        )

        
    cnx.close()

    return response

if __name__ == '__main__':
    print(get_all_services())

    #remove