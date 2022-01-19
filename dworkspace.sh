#!/usr/bin/env bash

emacs &
disown emacs &
sleep 1.5
xdotool key super+Left &
sleep 0.5
firefox github.com &
sleep 1.7
xdotool key super+Right &
