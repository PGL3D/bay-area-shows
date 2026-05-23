import json
import os

current_dir = os.path.dirname(__file__)
json_dump_path = os.path.join(current_dir, 'tixr_dump.json')
data_ts_path = os.path.join(current_dir, 'data.ts')

def update_website_data():
    if not os.path.exists(json_dump_path):
        print("Error: tixr_dump.json not found.")
        return

    with open(json_dump_path, 'r') as f:
        data = json.load(f)
    
    normalized_events = []
    
    for event in data:
        price = "TBD"
        ticket_type = "Check Website"
        
        # Based on image_f6a0e9.png, we look into 'sales' first
        sales = event.get('sales', [])
        if sales and len(sales) > 0:
            # Look for 'tiers' inside the first sales object
            tiers = sales[0].get('tiers', [])
            if tiers and len(tiers) > 0:
                t = tiers[0]
                ticket_type = t.get('name', 'General Admission')
                
                # Get the price from the tier
                raw_price = t.get('price') or t.get('minPrice')
                if raw_price:
                    try:
                        price = "{:.2f}".format(float(raw_price))
                    except:
                        price = "TBD"

        normalized_events.append({
            "artist": event.get('name'),
            "venue": "The Guild Theatre",
            "date": event.get('formattedStartDate'),
            "ticketUrl": "https://www.tixr.com" + str(event.get('url', '')),
            "ticketType": ticket_type,
            "price": price
        })
    
    file_content = "export const events = " + json.dumps(normalized_events, indent=2) + ";"
    with open(data_ts_path, 'w') as f:
        f.write(file_content)
    
    print("Successfully updated data.ts with prices from sales tiers!")

if __name__ == "__main__":
    update_website_data()