from iris_sdk.models.accounts import Account
from iris_sdk.client import Client

class GetOrdersExample():

    def __init__(self, url=None, account_id=None, username=None,
            password=None, filename=None):

        self._client = Client(
            url=url,
            account_id=account_id,
            username=username,
            password=password
        )

        acc = Account(self._client)

        print("\n--- Orders ---\n")

        # Note: different result sets for different page/size params, e.g.
        # the test server responds with the same order for page=i/size=1, and
        # while the xml states that the total number of orders for a search is
        # X, an XML returned for page=1/size=X*2 is different than for size=X
        # and actually includes X*2 orders.

        orders = acc.orders.list({"page": 1, "size": 200})

        i = 1
        total_displayed = len(orders)
        total = int(acc.orders.search_count)

        print("total for search: " + acc.orders.search_count)

        while (total_displayed <= total):

            if (i > 1):
                orders = acc.orders.list({"page": i, "size": 200})

            for order in orders:

                print(order.order_id)
                print("    status: " + order.order_status)

                print("    states:")
                for state in order.telephone_number_details.states.items:
                    print("        state: " + (state.name or ""))
                    print("            phone numbers: " + (state.count or ""))

                print("    rate centers:")
                for rate_center in order.telephone_number_details.\
                        rate_centers.items:
                    print("        rate center: " + (rate_center.name or ""))
                    print("            phone numbers: " +\
                        (rate_center.count or ""))

                print("    cities:")
                for city in order.telephone_number_details.cities.items:
                    print("        city: " + (city.name or ""))
                    print("            phone numbers: " + (city.count or ""))

                print("    tiers:")
                for tier in order.telephone_number_details.tiers.items:
                    print("        tier: " + (tier.name or ""))
                    print("            phone numbers: " + (tier.count or ""))

                print("    vendors:")
                for vendor in order.telephone_number_details.vendors.items:
                    print("        vendor id: " + (vendor.id or ""))
                    print("            vendor name: " + (vendor.name or ""))
                    print("            phone numbers: " +(vendor.count or ""))

            i += 1
            total_displayed += len(orders)