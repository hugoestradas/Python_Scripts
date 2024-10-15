import streamlit as st
import pandas as pd
import uuid


if "rows" not in st.session_state:
    st.session_state["rows"] = []

rows_collection = []

def add_row():
    element_id = uuid.uuid4()
    st.session_state["rows"].append(str(element_id))

def remove_row(row_id):
    st.session_state["rows"].remove(str(row_id))

def generate_row(row_id):
    row_container = st.empty()
    row_columns = row_container.columns((3, 2, 1))
    row_name = row_columns[0].text_input("Item Name", key=f"txt_{row_id}")
    row_qty = row_columns[1].number_input("Item Quantity", step=1, key=f"nbr_{row_id}")
    row_columns[2].button("🗑️", key=f"del_{row_id}", on_click=remove_row, args=[row_id])
    return {"name": row_name, "qty": row_qty}

st.title("Item Inventory")

for row in st.session_state["rows"]:
    row_data = generate_row(row)
    rows_collection.append(row_data)

menu = st.columns(2)

with menu[0]:
    st.button("Add Item", on_click=add_row)
if len(rows_collection) > 0:
    st.subheader("Collected Data")
    display = st.columns(2)
    data = pd.DataFrame(rows_collection)
    data.rename(columns={"name": "Item Name", "qty": "Quantity"}, inplace=True)
    display[0].dataframe(data=data, use_container_width=True)
    display[1].bar_chart(data=data, x="Item Name", y="Quantity")