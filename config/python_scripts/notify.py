# Get time and settings
time                = hass.states.get('sensor.time').state
sending             = hass.states.get('input_boolean.notify_pushover').state
default_priority    = hass.states.get('input_slider.pushover_priority').state

# Get script variables
target      = data.get('target') or 'xxx'
title       = (data.get('title') or 'HA automation') + ' @ ' + time
message     = data.get('message')
priority    = data.get('priority') or default_priority

# Call service
if sending == 'on' :
    data = { "target" : target, "title" : title, "message" : message , "data" : { "priority" : int(float(priority)) } }
    hass.services.call('notify', 'pushover', data)
