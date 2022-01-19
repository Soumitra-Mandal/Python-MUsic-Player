#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sat Jun 27 11:38:44 2020

@author: Soumitra
"""

import os
from pygame import mixer
import PySimpleGUI as sg

# File Uploader section

file_list_column = [[sg.Text('Songs Folder'), sg.In(size=(25, 1),
                    enable_events=True, key='FOLDER'),
                    sg.FolderBrowse()], [sg.Listbox(values=[],
                    enable_events=True, size=(40, 20), key='FILE LIST'
                    )]]

# Music Player Section

player = [
    [sg.Text('MUSIC PLAYER')],
    [sg.Button('PLAY')],
    [sg.Button('PAUSE')],
    [sg.Button('UNPAUSE')],
    [sg.Button('STOP')],
    [sg.Text('VOLUME')],
    [sg.Slider(
        (1, 100),
        default_value=30,
        key='VOL',
        orientation='h',
        enable_events=True,
        disable_number_display=True,
        )],
    ]

# Final Layout

layout = [[sg.Column(file_list_column), sg.VSeperator(),
          sg.Column(player)]]

window = sg.Window('Soumi Music Player', layout)  # Sending the layout to the window

# Starting the mixer

mixer.init()

# Create an event loop

while True:
    (event, values) = window.read()

    # End program if user closes window

    if event == sg.WIN_CLOSED:
        break
    elif event == 'FOLDER':
        folder = values['FOLDER']
        try:

            # Get list of files in folder

            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [f for f in file_list
                  if os.path.isfile(os.path.join(folder, f))
                  and f.lower().endswith('.mp3')]
        window['FILE LIST'].update(fnames)
    elif event == 'FILE LIST':

                                # A file was chosen from the listbox

        try:
            filename = os.path.join(values['FOLDER'], values['FILE LIST'
                                    ][0])
            mixer.music.load(filename)  # loading the song
        except:
            pass
    elif event == 'PLAY':

    # Basic Controls

        mixer.music.play()
    elif event == 'PAUSE':

        mixer.music.pause()
    elif event == 'UNPAUSE':

        mixer.music.unpause()
    elif event == 'STOP':
        mixer.music.stop()

    mixer.music.set_volume(values['VOL'] / 100)  #  Volume Controls

window.close()
