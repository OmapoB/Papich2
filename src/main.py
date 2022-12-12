import pandas as pd
from libbs.data_loader import DataFrameLoader
from libbs.GUI.gui import *


def main():
    amount_file = DataFrameLoader(cols=['Номенклатура',
                                        'Описание',
                                        'Ед.изм.',
                                        'Базовая',
                                        'Цена со скидкой 0%',
                                        'Всего в наличии',
                                        'Заказать',
                                        'Региональный склад',
                                        'Витрина ОК Галерея Кухни'],
                                  skip=2)

    amount_file.set_path(main_window.get_amount_input())
    amount_file = amount_file.load_df()
    amount_file = amount_file.astype({'Код для поиска': 'int32'})
    amount_file.set_index('Код для поиска', inplace=True)

    article_file = DataFrameLoader(cols=['Название склада',
                                         'Имя (необязательно)',
                                         'Заполнение обязательных ячеек  '])
    article_file.set_path(main_window.get_article_input())
    article_file = article_file.load_df()
    article_file.set_index('Артикул', inplace=True)

    result = {"Артикул": [], "Количество": []}
    for i in article_file.index:
        if i in amount_file.index:
            result["Артикул"].append(i)
            new_amount = amount_file["Основной склад"].get(i)
            if new_amount is not None:
                if new_amount > 2:
                    result["Количество"].append(int(new_amount) // 2)
                else:
                    result["Количество"].append(0)
            else:
                result["Количество"].append(0)

    saver = pd.ExcelWriter(main_window.get_save_input() + "/result.xlsx")
    result = pd.DataFrame(result)
    result.set_index("Артикул", inplace=True)
    result.to_excel(saver)
    saver.save()


if __name__ == '__main__':
    root = Tk()
    main_window = MainWindow(root)
    main_window.submit.config(command=main)
    root.mainloop()
