# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from pydbus import SystemBus


class ModemManagerHelper(object):

    def __init__(self, interface, path=None):
        self._interface = interface
        if path is None:
            self._path = '/org/freedesktop/ModemManager1'
            self._dbus = SystemBus().get('.ModemManager1')
        else:
            self._path = path
            self._dbus = SystemBus().get('.ModemManager1', self._path)

    def __str__(self):
        return str(self._path)

    def Get(self, property_name, interface_name=None):
        if interface_name is None:
            interface_name = self._interface
        return self._dbus.Get(interface_name, property_name)

    def GetAll(self, interface_name=None):
        if interface_name is None:
            interface_name = self._interface
        return self._dbus.GetAll(interface_name)

    def Set(self, value, property_name, interface_name=None):
        if interface_name is None:
            interface_name = self._interface
        self._dbus.Set(interface_name, property_name, value)

    def Introspect(self):
        return self._dbus.Introspect()

    def GetMachineId(self):
        return self._dbus.GetMachineId()

    def Ping(self):
        self._dbus.Ping()

    def Help(self):
        help(self._dbus)