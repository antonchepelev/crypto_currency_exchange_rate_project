from crypto import get_coin_by_symbol,  attribute_mapping


def html_generator(selected_crypto_symbols: list,selected_attr:list) -> str: 

    def select_crypto_objects_func(selected_crypto_symbols: list) -> list:
        selected_crypto_objects = []
        for symbol in selected_crypto_symbols:
            coin = get_coin_by_symbol(symbol)
            selected_crypto_objects.append(coin)
        return selected_crypto_objects


    html = "<style> th, td {border: 2px solid black;padding: 5px;} </style><html><body><table><tr>"
    for attr in selected_attr:
        if not attr == "name" and not attr == "image":
            for attribute_name, display_name in attribute_mapping.items():
                if attribute_name == attr:
                    html += f"<th>{display_name}</th>"
        if attr == "name":
            html += f"<th>Cryptocurrency</th>"
        if attr == "image":
            html += f"<th>               </th>"
    html += "</tr>"


    for coin in select_crypto_objects_func(selected_crypto_symbols):
        html += "<tr>"
        for attr in selected_attr :
            if not attr == "image":
                value = getattr(coin, attr)
                html += f"<td>{value}</td>"
            if attr == "image":
                value = getattr(coin, attr)
                html += f'<td><img src="{value}" width = 50px height = 50px ></td>'
        html += "</tr>"

    html += "</table></body></html>"

    
    return html
 


