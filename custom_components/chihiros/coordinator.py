"""Integration to integrate Keymitt BLE devices with Home Assistant."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

try:
    from homeassistant.components import bluetooth
    from homeassistant.components.bluetooth.passive_update_coordinator import (
        PassiveBluetoothDataUpdateCoordinator,
    )
    from homeassistant.core import HomeAssistant, callback
except ModuleNotFoundError:
    # FIXME make fake class and decorator
    PassiveBluetoothDataUpdateCoordinator = object  # type :ignore
    callback = property  # type: ignore


from .chihiros_led_control.device.base_device import BaseDevice

if TYPE_CHECKING:
    from bleak.backends.device import BLEDevice

_LOGGER: logging.Logger = logging.getLogger(__package__)


class ChihirosDataUpdateCoordinator(PassiveBluetoothDataUpdateCoordinator):
    """Class to manage fetching data from the Chihiros.

    TODO: See if the _async_handle_bluetooth_event is called.
    If not, that means this class is useless, so we can delete it
    """

    def __init__(
        self,
        hass: HomeAssistant,
        client: BaseDevice,
        ble_device: BLEDevice,
    ) -> None:
        """Initialize."""
        self.api: BaseDevice = client
        self.data: dict[str, Any] = {}
        self.ble_device = ble_device
        super().__init__(
            hass,
            _LOGGER,
            ble_device.address,
            bluetooth.BluetoothScanningMode.ACTIVE,
        )

    @callback
    def _async_handle_bluetooth_event(
        self,
        service_info: bluetooth.BluetoothServiceInfoBleak,
        change: bluetooth.BluetoothChange,
    ) -> None:
        """Handle a Bluetooth event."""
        _LOGGER.critical("%s: CHIHIROS data: %s", self.ble_device.address, self.data)
        super()._async_handle_bluetooth_event(service_info, change)
