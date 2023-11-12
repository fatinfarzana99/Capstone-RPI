#!/usr/bin/env python
import PySimpleGUI as sg
from time import sleep

# Simple example of TabGroup element and the options available to it
sg.theme('LightGreen3')     # Please always add color to your window
# The tab 1, 2, 3 layouts - what goes inside the tab
tab1_layout = [[sg.Button('Start Harvest'), sg.Button('Stop Harvest'), sg.Button('Reset System'), sg.Button('Reboot System')],
               [sg.Radio('Harvesting Tray 1', 1)],
               [sg.Radio('Harvesting Tray 2', 2)],              
               [sg.Text('Harvesting Tray In Progress')],
               [sg.ProgressBar(1, orientation='h', size=(20, 20), key='progress')],
               [sg.Cancel()]]


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


def HarvestingTrayProgressBar():
    progress_bar = window['progress']
    # loop that would normally do something useful
    for i in range(10000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=0)
        if event == 'Cancel' or event == None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.update_bar(i+1, 10000)
    # done with loop... need to destroy the window as it's still open


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
    HarvestingTrayProgressBar()


window.close()