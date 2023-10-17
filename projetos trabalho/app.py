import csv
import tkinter as tk

# Crie um dicionário vazio para armazenar as localizações e os itens
locations = {}

# Abra o arquivo de texto no modo de leitura
with open('itens.txt', 'r') as file:
    # Crie um objeto reader para ler o arquivo
    reader = csv.reader(file)

    # Percorra cada linha do arquivo
    for row in reader:
        # Verifique se a linha contém pelo menos dois valores
        if len(row) >= 2:
            # Obtenha a localização e o item da linha atual
            location, item = row

            # Verifique se a localização existe no dicionário e crie-a se não existir
            if location not in locations:
                locations[location] = []

            # Adicione o item à localização
            locations[location].append(item)

# Crie um dicionário vazio para armazenar a contagem dos itens por localização
location_item_counts = {}

# Crie uma variável para armazenar a última localização e o último item contados
last_counted_location = None
last_counted_item = None

# Crie uma função para lidar com o evento de clique do botão "Show Items"


def on_show_items_button_click():
    global last_counted_location

    # Obtenha o código da localização digitado pelo usuário
    location = location_entry.get()

    # Armazene a última localização contada
    last_counted_location = location

    # Verifique se a localização existe no dicionário de localizações
    if location in locations:
        # Exiba os itens cadastrados na localização
        items_text.delete('1.0', tk.END)
        items_text.insert(tk.END, f'Itens no local {location}:\n')
        for item in locations[location]:
            items_text.insert(tk.END, f'- {item}\n')
    else:
        # Se a localização não existir, exiba uma mensagem de erro
        items_text.delete('1.0', tk.END)
        items_text.insert(tk.END, f'Local não encontrado: {location}\n')

# Crie uma função para lidar com o evento de clique do botão "Count Item"


def on_count_item_button_click():
    global last_counted_location, last_counted_item

    # Obtenha o código do item digitado pelo usuário
    item = item_entry.get()

    # Verifique se há uma última localização contada
    if last_counted_location is not None:
        # Verifique se o item existe na última localização contada
        if last_counted_location in locations and item in locations[last_counted_location]:
            # Incremente a contagem do item em 1 na última localização contada
            if last_counted_location not in location_item_counts:
                location_item_counts[last_counted_location] = {}
            if item not in location_item_counts[last_counted_location]:
                location_item_counts[last_counted_location][item] = 0
            location_item_counts[last_counted_location][item] += 1

            # Armazene o último item contado
            last_counted_item = item

            # Exiba a contagem atual do item na última localização contada
            count_text.delete('1.0', tk.END)
            count_text.insert(
                tk.END, f'Total atual do item {item} no local {last_counted_location}: {location_item_counts[last_counted_location][item]}\n')

            # Exiba a soma total dos itens na última localização contada
            total_count = sum(
                location_item_counts[last_counted_location].values())
            count_text.insert(
                tk.END, f'Total de itens contados no local {last_counted_location}: {total_count}\n')
        else:
            # Se o item não existir na última localização contada, exiba uma mensagem de erro
            count_text.delete('1.0', tk.END)
            count_text.insert(
                tk.END, f'Não existe no local {last_counted_location} o item: {item}\n')
    else:
        # Se não houver uma última localização contada, exiba uma mensagem de erro
        count_text.delete('1.0', tk.END)
        count_text.insert(tk.END, f'Não há um local inserido\n')

# Crie uma função para lidar com o evento de clique do botão "Save Inventory"


def on_save_inventory_button_click():
    # Abra o arquivo de texto no modo de escrita
    with open('inventario.txt', 'w') as file:
        # Percorra cada localização e cada item no dicionário de contagem de itens por localização
        for location, items in location_item_counts.items():
            for item, count in items.items():
                # Escreva a localização, o item e a contagem no arquivo
                file.write(f'{location},{item},{count}\n')

    # Exiba uma mensagem de confirmação
    save_text.delete('1.0', tk.END)
    save_text.insert(tk.END, f'Inventario salvo como "inventario.txt"\n')


# Crie a janela principal
root = tk.Tk()
root.title('Inventário')

# Crie um rótulo e um campo de entrada para o código da localização
location_label = tk.Label(root, text='Local:')
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

# Crie um botão para exibir os itens cadastrados na localização
show_items_button = tk.Button(
    root, text='Mostrar itens', command=on_show_items_button_click)
show_items_button.pack()

# Crie uma área de texto para exibir os itens cadastrados na localização
items_text = tk.Text(root)
items_text.pack()

# Crie um rótulo e um campo de entrada para o código do item
item_label = tk.Label(root, text='Código do item')
item_label.pack()
item_entry = tk.Entry(root)
item_entry.pack()

# Crie um botão para incrementar a contagem do item
count_item_button = tk.Button(
    root, text='Contar', command=on_count_item_button_click)
count_item_button.pack()

# Crie um botão para salvar o inventário em um arquivo de texto
save_inventory_button = tk.Button(
    root, text='Salvar inventário', command=on_save_inventory_button_click)
save_inventory_button.pack()

# Crie uma área de texto para exibir a contagem dos itens por localização
count_text = tk.Text(root)
count_text.pack()

# Crie uma área de texto para exibir mensagens de confirmação ao salvar o inventário
save_text = tk.Text(root)
save_text.pack()

# Inicie o loop principal da janela
root.mainloop()

