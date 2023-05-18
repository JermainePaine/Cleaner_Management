SELECT Service.Service_id, Service.name, Service.uom_id, Service.price_per_service, UOM.uom_name
FROM Service
INNER JOIN UOM on service.uom_id=uom.uom_id;