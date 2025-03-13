from returns.maybe import Maybe

def calculate_price(event=None, discount=None):
    return(
        Maybe.from_optional(event)
        .bind_optional(lambda event: event.get_ticket())
        .bind_optional(lambda ticket: ticket.get_price())
        .bind_optional(lambda price: discount.get_discount(price))
    )
