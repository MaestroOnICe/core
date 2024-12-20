"""Base class for IOmeter entities."""

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import IOMeterCoordinator


class IOmeterEntity(CoordinatorEntity[IOMeterCoordinator]):
    """Defines a base AirGradient entity."""

    _attr_has_entity_name = True

    def __init__(self, coordinator: IOMeterCoordinator) -> None:
        """Initialize airgradient entity."""
        super().__init__(coordinator)
        status = coordinator.data.status
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, status.device.id)},
            manufacturer="IOmeter GmbH",
            model="IOmeter",
            serial_number=coordinator.identifier,
            sw_version=f"{ status.device.core.version}/{status.device.bridge.version}",
        )
