import streamlit as st
import pandas as pd
from vega_datasets import local_data as ld

st.set_page_config(layout="wide")


@st.cache_data
def get_data(id: int):
    return ld.airports().head(10)


def highlight_changes(val):
    color = f"color: black;" if val else "color:lightgray;"
    background = f"background-color:lightgray;" if val else ""
    return f"{color} {background}"

st.subheader("Edit your data ⬇️")
data = get_data(1)
editor_df = st.data_editor(
    data, key="airport_edit", num_rows="dynamic", use_container_width=True
)


def show_diff(
    source_df: pd.DataFrame, modified_df: pd.DataFrame, editor_key: dict
) -> None:
    target = pd.DataFrame(editor_key.get("edited_rows")).transpose().reset_index()
    modified_columns = [i for i in target.notna().columns if i != "index"]
    source = source_df.iloc[target.index].reset_index()
    target = target[modified_columns].reset_index()

    changes = pd.merge(
        source[modified_columns].reset_index(),
        target,
        how="outer",
        on="index",
        suffixes=["_BEFORE", "_AFTER"],
    )
    after_columns = [i for i in changes.columns if "_AFTER" in i]
    for cl in changes:
        if cl in after_columns:
            new_col = cl.replace("_AFTER", "_BEFORE")
            changes[cl] = changes[cl].fillna(changes[new_col])

    st.subheader("Modified")
    st.caption("Showing only modified columns")

    change_markers = changes.copy()
    for cl in change_markers:
        if cl in after_columns:
            new_col = cl.replace("_AFTER", "_BEFORE")
            change_markers[cl] = change_markers[cl] != change_markers[new_col]
            change_markers[new_col] = change_markers[cl]
    st.dataframe(
        changes.style.apply(
            lambda _: change_markers.applymap(highlight_changes), axis=None
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Inserted Rows")
    inserted = pd.DataFrame(editor_key.get("added_rows"))
    st.dataframe(inserted, use_container_width=True)
    st.subheader("Deleted Rows")
    st.dataframe(data.iloc[editor_key.get("deleted_rows")], use_container_width=True)


show_diff(
    source_df=data, modified_df=editor_df, editor_key=st.session_state["airport_edit"]
)
