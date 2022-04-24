"""
File         : app.py
Description  :
Creation Date: 24-Apr-2022
"""

import dearpygui.dearpygui as dpg

from tinydb import TinyDB

dpg.create_context()

db = TinyDB('board_data.json')

print(db.table('todo').all())
print(db.table('in_progress').all())
print(db.table('done').all())


# ---------------------------------------------------------------------------------------------------------------------

def close_app(sender, data):
    quit()

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

# callback runs when user attempts to connect attributes
def link_callback(sender, app_data):
    # app_data -> (link_id1, link_id2)
    dpg.add_node_link(app_data[0], app_data[1], parent=sender)

# callback runs when user attempts to disconnect attributes
def delink_callback(sender, app_data):
    # app_data -> link_id
    dpg.delete_item(app_data)


# ---------------------------------------------------------------------------------------------------------------------

with dpg.window(tag='primary_window'):

    with dpg.menu_bar():
        with dpg.menu(label='File'):
            dpg.add_menu_item(label='Preferences')
            dpg.add_separator()
            dpg.add_menu_item(label='Close', callback=close_app)
        with dpg.menu(label='Board'):
            dpg.add_menu_item(label='New...')
            dpg.add_menu_item(label='Rename...')
            dpg.add_menu_item(label='Delete...')
            dpg.add_separator()
            with dpg.menu(label='Open Recent'):
                dpg.add_menu_item(label='Default Board')
            dpg.add_separator()
            dpg.add_menu_item(label='Archive completed tasks')
            with dpg.menu(label='Database'):
                dpg.add_menu_item(label='Open')
                dpg.add_menu_item(label='Copy path')
        with dpg.menu(label='Help'):
            with dpg.menu(label='Development'):
                dpg.add_menu_item(label='Debug', callback=open_debug)
                dpg.add_menu_item(label='Fonts Manager', callback=open_fonts)
                dpg.add_menu_item(label='Style Editor', callback=open_style_editor)
                dpg.add_menu_item(label='Metrics', callback=open_metrics)
            dpg.add_menu_item(label='About')

    with dpg.tab_bar(tag='primary_tabbar'):
        with dpg.tab(tag='board_tab', label='Board'):
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
                    with dpg.child_window(tag='todo_win', autosize_x=False, horizontal_scrollbar=True, border=False):
                        dpg.add_input_text(tag='todo_input', on_enter=True, width=-1, callback=create_new_task, hint='New TODO task...')
                        for task in db.table('todo').all():
                            dpg.add_selectable(label=task['value'])
                    with dpg.child_window(tag='progress_win', autosize_x=False, horizontal_scrollbar=True, border=False):
                        dpg.add_input_text(tag='progress_input', on_enter=True, width=-1, callback=create_new_task, hint='New IN PROGRESS task...')
                        for task in db.table('in_progress').all():
                            dpg.add_selectable(label=task['value'])
                    with dpg.child_window(tag='done_win', autosize_x=False, horizontal_scrollbar=True, border=False):
                        dpg.add_input_text(tag='done_input', on_enter=True, width=-1, callback=create_new_task, hint='New DONE task...')
                        for task in db.table('done').all():
                            dpg.add_selectable(label=task['value'])

        with dpg.tab(tag='stats_tab', label='Stats'):
            with dpg.plot(no_title=True, no_mouse_pos=True, width=250, height=250):
                # create legend
                dpg.add_plot_legend()

                # create x axis
                dpg.add_plot_axis(dpg.mvXAxis, label='', no_gridlines=True, no_tick_marks=True, no_tick_labels=True)
                dpg.set_axis_limits(dpg.last_item(), 0, 1)

                # create y axis
                with dpg.plot_axis(dpg.mvYAxis, label='', no_gridlines=True, no_tick_marks=True, no_tick_labels=True):
                    data = [len(db.table(table).all()) for table in db.tables()]
                    dpg.set_axis_limits(dpg.last_item(), 0, 1)
                    dpg.add_pie_series(0.5, 0.5, 0.5, values=data, labels=list(db.tables()))

        with dpg.tab(tag='settings_tab', label='Settings'):
            board = TinyDB('./res/boards/default_board.json').get(doc_id=1)
            dpg.add_button(label='Add column/node', tag='add_item', callback=add_item)

            with dpg.group(horizontal=True):
                with dpg.child_window(tag='tab_settings-window', width=300, autosize_x=False):
                    dpg.add_button(label='Save Board Settings', callback=add_item)
                    dpg.add_input_text(label='Board Name', default_value=board['name'], enabled=False)

                with dpg.node_editor(callback=link_callback, delink_callback=delink_callback):
                    for id in board['columns']:
                        with dpg.node(label=f'Node {id}', pos=((int(id)-1) * 250, (int(id)-1) * 25)):
                            with dpg.node_attribute(label='Node A1', attribute_type=dpg.mvNode_Attr_Static):
                                dpg.add_input_text(label='Column Name', width=100, default_value=board['columns'][id]['title'])
                                dpg.add_checkbox(label='Column visible', default_value=board['columns'][id]['show'])

                            with dpg.node_attribute(label='Node A2'):
                                dpg.add_input_text(label='Predecessor', width=100)

                            with dpg.node_attribute(label='Node A3', shape=dpg.mvNode_PinShape_TriangleFilled, attribute_type=dpg.mvNode_Attr_Output):
                                dpg.add_input_text(label='Successor', width=100)


# ---------------------------------------------------------------------------------------------------------------------
# Theme

with dpg.theme() as input_theme:
    with dpg.theme_component(dpg.mvAll):
        # dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (42, 40, 46), category=dpg.mvThemeCat_Core)
        # dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (42, 40, 46), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, x=10, y=10, category=dpg.mvThemeCat_Core)

with dpg.theme() as tab_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, x=10, y=10, category=dpg.mvThemeCat_Core)

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, x=10, y=10, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, x=10, y=10, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)
dpg.bind_item_theme('todo_input', input_theme)
dpg.bind_item_theme('progress_input', input_theme)
dpg.bind_item_theme('done_input', input_theme)
# dpg.bind_item_theme('todo_win', input_theme)
# dpg.bind_item_theme('progress_win', input_theme)
# dpg.bind_item_theme('done_win', input_theme)
# dpg.bind_item_theme('board_tab', tab_theme)
# dpg.bind_item_theme('stats_tab', tab_theme)
# dpg.bind_item_theme('settings_tab', tab_theme)


# ---------------------------------------------------------------------------------------------------------------------

dpg.create_viewport(title='Kanban Board', width=1200, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('primary_window', True)
dpg.start_dearpygui()
dpg.destroy_context()
