"""
File         : app.py
Description  :
Creation Date: 24-Apr-2022
"""
from re import L
from subprocess import call
import dearpygui.dearpygui as dpg


# ---------------------------------------------------------------------------------------------------------------------

def open_debug(sender, data):
    dpg.show_debug()

def open_metrics(sender, data):
    dpg.show_metrics()


# ---------------------------------------------------------------------------------------------------------------------

dpg.create_context()

with dpg.window(tag='Primary Window'):

    with dpg.menu_bar():
        with dpg.menu(label='File'):
            dpg.add_menu_item(label='Save')
            dpg.add_menu_item(label='Close')
        with dpg.menu(label='Board'):
            dpg.add_menu_item(label='New...')
        with dpg.menu(label='Help'):
            dpg.add_menu_item(label='Debug', callback=open_debug)
            dpg.add_menu_item(label='Metrics', callback=open_metrics)

    dpg.add_text('Project: Test 123')

    with dpg.table(header_row=False):
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()

        with dpg.table_row():
            dpg.add_input_text()
            dpg.add_input_text()
            dpg.add_input_text()

    with dpg.table(header_row=True, borders_outerH=False, borders_innerV=True, resizable=True, policy=dpg.mvTable_SizingStretchProp):

        # use add_table_column to add columns to the table,
        # table columns use child slot 0
        dpg.add_table_column(label='Todo')
        dpg.add_table_column(label='In Progress')
        dpg.add_table_column(label='Done')

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
        for i in range(0, 14):
            with dpg.table_row():
                for j in range(0, 3):
                    dpg.add_text(f'Row{i} Column{j}')





# ---------------------------------------------------------------------------------------------------------------------

dpg.create_viewport(title='Kanban Board', width=1200, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('Primary Window', True)
dpg.start_dearpygui()
dpg.destroy_context()
