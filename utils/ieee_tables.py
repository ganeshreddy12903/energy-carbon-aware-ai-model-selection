def generate_ieee_table(df):
    table = "\\begin{table}[h]\n\\centering\n"
    table += "\\begin{tabular}{|l|c|c|c|}\n\\hline\n"
    table += "Model & Accuracy & Energy (J) & Carbon (gCO$_2$) \\\\\n\\hline\n"

    for _, row in df.iterrows():
        table += f"{row['Model']} & {row['Accuracy']} & {row['Energy (J)']} & {row['Carbon (gCO₂)']} \\\\\n"

    table += "\\hline\n\\end{tabular}\n"
    table += "\\caption{Sustainability-Aware Model Comparison}\n"
    table += "\\end{table}"

    return table
