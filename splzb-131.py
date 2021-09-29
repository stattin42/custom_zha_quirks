"""Develco SPLZB-131 device."""
from zigpy.profiles import zha
from zigpy.quirks import CustomDevice, CustomCluster
from zigpy.zcl.clusters.general import (
        Basic,
        DeviceTemperature,
        Identify,
        Groups,
        Scenes,
        OnOff,
        Alarms,
        Time,
        Ota,
)
from zigpy.zcl.clusters.measurement import OccupancySensing
from zigpy.zcl.clusters.smartenergy import Metering
from zigpy.zcl.clusters.homeautomation import ElectricalMeasurement
from zhaquirks.const import (
        DEVICE_TYPE,
        ENDPOINTS,
        INPUT_CLUSTERS,
        MODELS_INFO,
        OUTPUT_CLUSTERS,
        PROFILE_ID,
)


class MeteringCluster(CustomCluster, Metering):
        """Develco SPLZB-131 Metering cluster"""

        _CONSTANT_ATTRIBUTES = {
                0x0300: 0x00,      # unit_of_measure = 0 (kWh)
                0x0301: 0x000001,  # multiplier = 1
                0x0302: 0x0003E8,  # divisor = 1000
                0x0303: 0xAA,      # summa_formatting =
                                   #   0b1....... (suppress leading zeroes) |
                                   #   0b.0101... (5 digits left of d p) |
                                   #   0b.....010 (2 digits right of d p)
        }


class SPLZB_131(CustomDevice):
        """Develco SPLZB-131 device."""

        signature = {
                MODELS_INFO: [("Develco Products A/S", "SPLZB-131")],
                ENDPOINTS: {
                        # <SimpleDescriptor
                        #   endpoint=1 profile=49353 device_type=0x0001
                        #   input_clusters=[5, 6]
                        #   output_clusters=[]>
                        1: {
                                PROFILE_ID: 49353,
                                DEVICE_TYPE: 0x0001,
                                INPUT_CLUSTERS: [
                                        0x0005,  # Scenes cluster?
                                        0x0006,  # OnOff cluster?
                                ],
                                OUTPUT_CLUSTERS: [],
                        },
                        # <SimpleDescriptor
                        #   endpoint=2 profile=260 device_type=0x0051
                        #   input_clusters=[0, 2, 3, 4, 5, 6, 9, 1794, 2820]
                        #   output_clusters=[3, 10, 25, 1030]>
                        2: {
                                PROFILE_ID: zha.PROFILE_ID,
                                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                                INPUT_CLUSTERS: [
                                        Basic.cluster_id,
                                        DeviceTemperature.cluster_id,
                                        Identify.cluster_id,
                                        Groups.cluster_id,
                                        Scenes.cluster_id,
                                        OnOff.cluster_id,
                                        Alarms.cluster_id,
                                        Metering.cluster_id,
                                        ElectricalMeasurement.cluster_id,
                                ],
                                OUTPUT_CLUSTERS: [
                                        Identify.cluster_id,
                                        Time.cluster_id,
                                        Ota.cluster_id,
                                        OccupancySensing.cluster_id,
                                ],
                        },
                },
        }

        replacement = {
                ENDPOINTS: {
                        1: {
                                PROFILE_ID: 49353,
                                DEVICE_TYPE: 0x0001,
                                INPUT_CLUSTERS: [
                                        0x0005,  # Scenes cluster?
                                        0x0006,  # OnOff cluster?
                                ],
                                OUTPUT_CLUSTERS: [],
                        },
                        2: {
                                PROFILE_ID: zha.PROFILE_ID,
                                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                                INPUT_CLUSTERS: [
                                        Basic.cluster_id,
                                        DeviceTemperature.cluster_id,
                                        Identify.cluster_id,
                                        Groups.cluster_id,
                                        Scenes.cluster_id,
                                        OnOff.cluster_id,
                                        Alarms.cluster_id,
                                        MeteringCluster,
                                        ElectricalMeasurement.cluster_id,
                                ],
                                OUTPUT_CLUSTERS: [
                                        Identify.cluster_id,
                                        Time.cluster_id,
                                        Ota.cluster_id,
                                        OccupancySensing.cluster_id,
                                ],
                        },
                },
        }
