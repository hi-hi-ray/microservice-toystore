from models import ToyOrder


def create_order(id_toy_req, quantity_req):
    creation = ToyOrder.create(
        id_toy=id_toy_req,
        quantity=quantity_req)

    # syncer.send_to_sqs(creation.id,
    #                    creation.type_stop,
    #                    creation.id_stop,
    #                    'creation', creation.timestamp)

    if creation.id_toy is not None:
        return "Created Order"
    else:
        return "Failed to create order"


def get_orders():
    orders = ToyOrder.select()
    orders_array = []
    for orders in orders:
        order = {
            'id': orders.id,
            'id_toy': orders.id_toy,
            'quantity': orders.quantity
        }
        orders_array.append(order)
    return orders_array


def get_order_by_id(id_req):
    orders = ToyOrder.select().where(ToyOrder.id == id_req)
    orders_array = []
    for orders in orders:
        order = {
            'id': orders.id,
            'id_toy': orders.id_toy,
            'quantity': orders.quantity
        }
        orders_array.append(order)
    return orders_array


def delete_order(id_req):
    query_delete = ToyOrder.delete().where(ToyOrder.id == id_req)
    rows_delete = query_delete.execute()
    if rows_delete != 0:
        return "Deleted order"
    else:
        return "No order was deleted"


def update_order(id_req, id_toy_req, quantity_req):
    query_update = (ToyOrder.update({
        'id_toy': id_toy_req,
        'quantity': quantity_req
    }).where(ToyOrder.id == id_req))

    rows_updated = query_update.execute()
    if rows_updated != 0:
        # syncer.send_to_sqs(query_update.id,
        #                    query_update.type_stop,
        #                    query_update.id_stop,
        #                    'Update', query_update.timestamp)
        return "Order Updated"
    else:
        return "No order was updated"
