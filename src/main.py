import pandas as pd

file_from = pd.read_excel("../resources/stock-update-template.xlsx")
file_from.drop(labels=["Название склада",
                  "Имя (необязательно)",
                  "Заполнение обязательных ячеек  "], axis=1, inplace=True)
result = {"Артикул": [], "Количество": []}
for artic, amount in zip(file_from["Артикул"], file_from["Количество"]):
    try:
        artic = int(artic)
        amount = int(amount)
        if amount < 2:
            result["Артикул"].append(artic)
            result["Количество"].append(0)
        else:
            result["Артикул"].append(artic)
            result["Количество"].append(amount // 2)
    except ValueError:
        result["Артикул"].append(artic)
        result["Количество"].append(0)
output = pd.ExcelWriter("../resources/result.xlsx")
pd.DataFrame(result).to_excel(output)
output.save()