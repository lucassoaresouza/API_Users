from typing import List

from customers.models import Customer, Paginator


class CustomerPagination():
    """
    Class that paginate a customer list
    """
    def __init__(
        self,
        customers: List[Customer],
        page_number: int,
        page_size: int = 10
    ):
        """
        Class constructor.
        :param customers: A list of Customer instances.
        :param page_number: The actual page.
        :param page_size: The amount of customers on a page.
        """
        self.customers: List[Customer] = customers
        self.page_number: int = page_number
        self.page_size: int = page_size

    def paginate(self) -> Paginator:
        """
        Get a interval of the customers list to make a Paginator instance.
        :returns: A Paginator instance.
        """
        initial_value = self.page_number * self.page_size
        final_value = initial_value + self.page_size
        page = self.customers[initial_value:final_value]
        return Paginator(
            pageNumber=self.page_number,
            pageSize=self.page_size,
            totalCount=len(self.customers),
            users=page
        )
