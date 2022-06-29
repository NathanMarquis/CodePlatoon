from curses import pair_content
from msilib.schema import ComboBox


def picker(prices):
    loop through prices
        loop through again to get every combo 
            if first_value < next_value
                if diff greater than comparitor, make it comparitor and add ind pair as answer
                remove first value from prices array to keep buy-sell order