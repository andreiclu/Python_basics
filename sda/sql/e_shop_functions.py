import pymysql


def cart_detail_command(cart_id):
    read_cart = f"select carts.id, carts.user_id, carts.status, cart_items.quantity, cart_items.product_id from carts join cart_items where carts.id = {cart_id}"
    return read_cart


def product_price_command(product_id):
    prod_price = f"select price from products where id = {product_id} "
    return prod_price


def manipulate_cart_data(cursor, cart_data):
    total = 0
    for cart_details in cart_data:
        id_, user_id, status, quantity, product_id = cart_details
        cursor.execute(product_price_command(product_id))
        price_tuple = cursor.fetchall()
        price = price_tuple[0][0]
        total = total + (price * quantity)
    print(f"total = {total} Lei")
    return total


def cart_total(connection, cart_id):
    with connection.cursor() as cursor:
        cursor.execute(open_database)
        cursor.execute(cart_detail_command(cart_id))
        print([d[0] for d in cursor.description])
        print(cursor.description)

        cart_data = cursor.fetchall()
        total = manipulate_cart_data(cursor, cart_data)
        return total
if __name__ == '__main__':

    with pymysql.connect(host="127.0.0.1", user="root", password=password.password) as connection:
        print("connected!")

        open_database = "use e_shop"
        total = cart_total(connection, 1)