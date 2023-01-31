import streamlit as st
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Display the DataFrame as an editable table using handsontable
st.markdown(
    """
    <script src="https://cdn.jsdelivr.net/npm/handsontable@7.4.0/dist/handsontable.full.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/handsontable@7.4.0/dist/handsontable.full.min.css" rel="stylesheet" media="screen">
    <div id="table"></div>
    <script>
    var data = {};
    """
    + df.to_json(orient='split')
    + """
    var hot = new Handsontable(document.getElementById('table'), {
        data: data.data,
        rowHeaders: true,
        colHeaders: """
    + str(df.columns.tolist())
    + """,
        minSpareRows: 1,
        columns: """
    + str([{'readOnly': False} for _ in range(len(df.columns))])
    + """,
        stretchH: 'all',
        autoWrapRow: true,
        height: 400,
        manualRowResize: true,
        manualColumnResize: true
    });
    </script>
    """
)

