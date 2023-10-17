import csv
import tkinter as tk


PLAQUE_CODE = '999999' # codigo da plaqueta
locations = {}

with open('itens.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) >= 2:
            location, item = row
            location = location.lower()
            if location not in locations:
                locations[location] = []
            locations[location].append(item)

location_item_counts = {}
last_counted_location = None
last_counted_item = None

def on_show_items_button_click():
    global last_counted_location
    location = location_entry.get().lower()
    last_counted_location = location
    if location in locations:
        items_text.delete('1.0', tk.END)
        items_text.insert(tk.END, f'Items in {location}:\n')
        for item in locations[location]:
            items_text.insert(tk.END, f'- {item}\n')
    else:
        items_text.delete('1.0', tk.END)
        items_text.insert(tk.END, f'Location not found: {location}\n')

def on_count_item_button_click():
    global last_counted_location, last_counted_item
    item = item_entry.get()
    if last_counted_location is not None:
        if last_counted_location in locations and item in locations[last_counted_location]:
            if last_counted_location not in location_item_counts:
                location_item_counts[last_counted_location] = {}
            if item not in location_item_counts[last_counted_location]:
                location_item_counts[last_counted_location][item] = 0
            location_item_counts[last_counted_location][item] += 1
            last_counted_item = item
            count_text.delete('1.0', tk.END)
            count_text.insert(
                tk.END, f'Current count for item {item} in location {last_counted_location}: {location_item_counts[last_counted_location][item]}\n')
            total_count = sum(
                location_item_counts[last_counted_location].values())
            count_text.insert(
                tk.END, f'Total item count in location {last_counted_location}: {total_count}\n')
        else:
            count_text.delete('1.0', tk.END)
            count_text.insert(
                tk.END, f'Item not found in location {last_counted_location}: {item}\n')
    else:
        count_text.delete('1.0', tk.END)
        count_text.insert(tk.END, f'No last counted location to count item\n')

def on_save_inventory_button_click():
    with open('inventory.txt', 'w') as file:
        for location, items in location_item_counts.items():
            for item, count in items.items():
                file.write(f'{location},{item},{count}\n')
    save_text.delete('1.0', tk.END)
    save_text.insert(tk.END, f'Inventory saved to file "inventory.txt"\n')

root = tk.Tk()
root.title('Iventario')

location_label = tk.Label(root, text='Location code:')
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

def on_location_entry_key(event):
    if len(location_entry.get()) == 11:
        on_show_items_button_click()
        item_entry.focus_set()

location_entry.bind('<KeyRelease>', on_location_entry_key)

show_items_button = tk.Button(
    root, text='Show Items', command=on_show_items_button_click)
show_items_button.pack()

items_text = tk.Text(root)
items_text.pack()

item_label = tk.Label(root, text='Item code:')
item_label.pack()
item_entry = tk.Entry(root)
item_entry.pack()

item_entry_text = ''

def on_item_entry_key(event):
    global item_entry_text
    item_entry_text = item_entry.get()
    # verifica se o codigo inserido é igual ao codigo da plaqueta
    if item_entry_text == PLAQUE_CODE:
        item_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)
        location_entry.focus_set()
    elif len(item_entry_text) == 6:
        on_count_item_button_click()
        item_entry_text = ''
        item_entry.delete(0, tk.END)

item_entry.bind('<KeyRelease>', on_item_entry_key)

count_item_button = tk.Button(
    root, text='Count Item', command=on_count_item_button_click)
count_item_button.pack()

save_inventory_button = tk.Button(
  root, text='Save Inventory', command=on_save_inventory_button_click)
save_inventory_button.pack()

count_text = tk.Text(root)
count_text.pack()

save_text = tk.Text(root)
save_text.pack()

root.mainloop()