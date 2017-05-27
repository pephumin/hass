import time, math, requests
import voluptuous as vol

from xml.etree import ElementTree

from homeassistant.components.media_player import (PLATFORM_SCHEMA, MediaPlayerDevice)
from homeassistant.const import (CONF_HOST, CONF_PORT)
import homeassistant.helpers.config_validation as cv

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_HOST): cv.string,
    vol.Required(CONF_PORT): cv.string,
})

def setup_platform(hass, config, add_devices, discovery_info=None):

    denonxml = DenonSensor(config.get(CONF_HOST), config.get(CONF_PORT))
    add_devices([denonxml])

class DenonSensor(MediaPlayerDevice):

    def __init__(self, host, port):
        self._state = "off"
        self._host  = host
        self._port  = port
        self._name  = "Denon " + port

    @property
    def name(self):
        return "Denon Zone" + self._port

    @property
    def state(self):
        return self._state

    @property
    def source(self):
        return self._mediasource

    @property
    def volume_level(self):
        return self._volume

    def getZon(self):
        if self._port == "2":
            return "Z2"
        else:
            return "ZM"

    def turn_off(self):
        url = "http://" + self._host + "/goform/formiPhoneAppDirect.xml?" + self.getZon() + "OFF"
        requests.get(url)
        time.sleep(4)

    def turn_on(self):
        url = "http://" + self._host + "/goform/formiPhoneAppDirect.xml?" + self.getZon() + "ON"
        requests.get(url)
        time.sleep(4)

    def update(self):

        url = "http://" + self._host + "/goform/formMainZone_MainZoneXml.xml?ZoneName=zone" + self._port
        response = requests.get(url)
        root = ElementTree.fromstring(response.content)

        on_off = root.find('ZonePower').find('value').text
        src    = root.find('InputFuncSelect').find('value').text
        volume = root.find('MasterVolume').find('value').text

        self._state = on_off.lower()
        self._mediasource = src
        self._volume = math.ceil(float(volume)) + 80
