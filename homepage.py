#!/usr/bin/env python

"""
    Demo - Simple Tabs

    How to use the Tab Element and the TabGroup Element

    Copyright 2021 PySimpleGUI
"""

import PySimpleGUI as sg
# Simple example of TabGroup element and the options available to it
sg.theme('Dark Red')     # Please always add color to your window
# The tab 1, 2, 3 layouts - what goes inside the tab

tab1_layout = [[sg.Button('Start Harvest'), sg.Button('Stop Harvest'), sg.Button('Reset System'), sg.Button('Reboot System')],
               [sg.Text('Put your layout in here')],
               [sg.Text('Input something'), sg.Input(size=(12,1), key='-IN-TAB1-')]]

tab2_layout = [[sg.Text('Diagnostic')]]
tab3_layout = [[sg.Text('Output')]]

# The TabgGroup layout - it must contain only Tabs
tab_group_layout = [[sg.Tab('Main', tab1_layout, key='-TAB1-'),
                     sg.Tab('Diagnostic', tab2_layout, visible=True, key='-TAB2-'),
                     sg.Tab('Output', tab3_layout, key='-TAB3-')]]


# The window layout - defines the entire window
layout = [[sg.TabGroup(tab_group_layout,
                       enable_events=True,
                       key='-TABGROUP-')]]
          #[sg.Button('Start Harvest'), sg.Button('Stop Harvest'), sg.Button('Reboot System')]

window = sg.Window('Automated Harvesting Tray Retrieval', layout, no_titlebar=False)

tab_keys = ('-TAB1-','-TAB2-','-TAB3-')         # map from an input value to a key
while True:
    event, values = window.read()       
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    # handle button clicks
    if event == 'Start Harvest':
        window[tab_keys[int(values['-IN-'])-1]].update(visible=False)
    if event == 'Stop Harvest':
        window[tab_keys[int(values['-IN-'])-1]].update(visible=True)
    if event == 'Reset System':
        window[tab_keys[int(values['-IN-'])-1]].select()      
    if event == 'Reboot System':
        window[tab_keys[int(values['-IN-'])-1]].select()
window.close()