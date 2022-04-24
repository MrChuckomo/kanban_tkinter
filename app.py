"""
File         : app.py
Description  :
Creation Date: 24-Apr-2022
"""

import dearpygui.dearpygui as dpg

from math import sin
from tinydb import TinyDB

dpg.create_context()

db = TinyDB('board_data.json')

print(db.table('todo').all())
print(db.table('in_progress').all())
print(db.table('done').all())


# ---------------------------------------------------------------------------------------------------------------------

def open_debug(sender, data):
    dpg.show_debug()

def open_fonts(sender, data):
    dpg.show_font_manager()

def open_style_editor(sender, data):
    dpg.show_style_editor()

def open_metrics(sender, data):
    dpg.show_metrics()

def add_item(sender, data):
    print(sender)
    print(data)
    dpg.add_button(label='New Button', parent='primary_window', tag='new_btn')

def create_new_task(sender, data):
    if sender == 'todo_input':
        dpg.add_selectable(label=data, parent='todo_win')
        db.table('todo').insert({'value': data})
    elif sender == 'progress_input':
        dpg.add_selectable(label=data, parent='progress_win')
        db.table('in_progress').insert({'value': data})
    elif sender == 'done_input':
        dpg.add_selectable(label=data, parent='done_win')
        db.table('done').insert({'value': data})

    dpg.configure_item(sender, default_value='')


sindatax = []
sindatay = []
for i in range(0, 500):
    sindatax.append(i / 1000)
    sindatay.append(0.5 + 0.5 * sin(50 * i / 1000))


# ---------------------------------------------------------------------------------------------------------------------

with dpg.window(tag='primary_window'):

    with dpg.menu_bar():
        with dpg.menu(label='File'):
            dpg.add_menu_item(label='Save')
            dpg.add_menu_item(label='Close')
        with dpg.menu(label='Board'):
            dpg.add_menu_item(label='New...')
        with dpg.menu(label='Help'):
            dpg.add_menu_item(label='Debug', callback=open_debug)
            dpg.add_menu_item(label='Fonts Manager', callback=open_fonts)
            dpg.add_menu_item(label='Style Editor', callback=open_style_editor)
            dpg.add_menu_item(label='Metrics', callback=open_metrics)

    with dpg.tab_bar(tag='primary_tabbar'):
        with dpg.tab(label='Board'):
            dpg.add_text(default_value='Project: Default Board', tag='board_title')

            with dpg.tooltip('board_title'):
                dpg.add_text('The name of your current board')

            with dpg.table(header_row=True, borders_outerH=False, borders_innerV=True, resizable=True):

                # use add_table_column to add columns to the table,
                # table columns use child slot 0
                dpg.add_table_column(label='Todo')
                dpg.add_table_column(label='In Progress')
                dpg.add_table_column(label='Done')

                with dpg.table_row():
                    dpg.add_input_text(tag='todo_input', on_enter=True, width=-1, callback=create_new_task, hint='New TODO task...')
                    dpg.add_input_text(tag='progress_input', on_enter=True, width=-1, callback=create_new_task, hint='New IN PROGRESS task...')
                    dpg.add_input_text(tag='done_input', on_enter=True, width=-1, callback=create_new_task, hint='New DONE task...')

                with dpg.table_row():
                    with dpg.child_window(tag='todo_win', autosize_x=False, horizontal_scrollbar=True, border=False):
                        for task in db.table('todo').all():
                            dpg.add_selectable(label=task['value'])
                    with dpg.child_window(tag='progress_win', autosize_x=False, horizontal_scrollbar=True, border=False):
                        for task in db.table('in_progress').all():
                            dpg.add_selectable(label=task['value'])
                    with dpg.child_window(tag='done_win', autosize_x=False, horizontal_scrollbar=True, border=False):
                        for task in db.table('done').all():
                            dpg.add_selectable(label=task['value'])


        with dpg.tab(label='Stats'):
            with dpg.plot(label='Line Series'):
                # optionally create legend
                dpg.add_plot_legend()

                # REQUIRED: create x and y axes
                dpg.add_plot_axis(dpg.mvXAxis, label='x')
                dpg.add_plot_axis(dpg.mvYAxis, label='y', tag='y_axis')

                # series belong to a y axis
                dpg.add_line_series(sindatax, sindatay, label='0.5 + 0.5 * sin(x)', parent='y_axis')

        with dpg.tab(label='Settings'):
            dpg.add_button(label='Add Item', tag='add_item', callback=add_item)

            with dpg.group(horizontal=True):
                with dpg.child_window(tag='tab_settings-window', width=600, autosize_x=False):
                    dpg.add_button(label='Add Item', callback=add_item)
                with dpg.child_window(tag='tab_settings-window2'):
                    dpg.add_button(label='Add Item', callback=add_item)

# ---------------------------------------------------------------------------------------------------------------------
# Theme

with dpg.theme() as input_theme:
    with dpg.theme_component(dpg.mvAll):
        # dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (42, 40, 46), category=dpg.mvThemeCat_Core)
        # dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (42, 40, 46), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, x=10, y=10, category=dpg.mvThemeCat_Core)

dpg.bind_item_theme('todo_input', input_theme)
dpg.bind_item_theme('progress_input', input_theme)
dpg.bind_item_theme('done_input', input_theme)
# dpg.bind_item_theme('todo_win', input_theme)
# dpg.bind_item_theme('progress_win', input_theme)
# dpg.bind_item_theme('done_win', input_theme)


# ---------------------------------------------------------------------------------------------------------------------

dpg.create_viewport(title='Kanban Board', width=1200, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('primary_window', True)
dpg.start_dearpygui()
dpg.destroy_context()
