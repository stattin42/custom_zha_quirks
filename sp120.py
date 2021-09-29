"""Innr SP 120 device."""
from zigpy.profiles import zll
from zigpy.quirks import CustomDevice, CustomCluster
from zigpy.zcl.clusters.general import (
        Basic,
        Identify,
        Groups,
        Scenes,
        OnOff,
        LevelControl,
        Time,
        Ota,
)
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
        """Innr SP 120 Metering cluster"""

        _CONSTANT_ATTRIBUTES = {
                0x0300: 0x00,  # unit_of_measure = 0 (kWh)
                0x0301: 0x01,  # multiplier = 1
                0x0302: 0x64,  # divisor = 100
                0x0303: 0xAA,  # summa_formatting =
                               #   0b1....... (suppress leading zeroes) |
                               #   0b.0101... (5 digits left of d p) |
                               #   0b.....010 (2 digits right of d p)
        }


class SP120_1(CustomDevice):
        """Innr SP 120 device."""

        signature = {
                MODELS_INFO: [("innr", "SP 120")],
                ENDPOINTS: {
                        # <SimpleDescriptor
                        #   endpoint=1 profile=49246 device_type=0x0010
                        #   input_clusters=[0, 3, 4, 5, 6, 8, 10, 1794, 2820]
                        #   output_clusters=[]>
                        1: {
                                PROFILE_ID: zll.PROFILE_ID,
                                DEVICE_TYPE: zll.DeviceType.ON_OFF_PLUGIN_UNIT,
                                INPUT_CLUSTERS: [
                                        Basic.cluster_id,
                                        Identify.cluster_id,
                                        Groups.cluster_id,
                                        Scenes.cluster_id,
                                        OnOff.cluster_id,
                                        LevelControl.cluster_id,
                                        Time.cluster_id,
                                        Metering.cluster_id,
                                        ElectricalMeasurement.cluster_id,
                                ],
                                OUTPUT_CLUSTERS: [],
                        },
                        # <SimpleDescriptor
                        #   endpoint=2 profile=49246 device_type=0x1000
                        #   input_clusters=[]
                        #   output_clusters=[]>
                        2: {
                                PROFILE_ID: zll.PROFILE_ID,
                                DEVICE_TYPE: 0x1000,
                                INPUT_CLUSTERS: [],
                                OUTPUT_CLUSTERS: [],
                        },
                },
        }

        replacement = {
                ENDPOINTS: {
                        1: {
                                PROFILE_ID: zll.PROFILE_ID,
                                DEVICE_TYPE: zll.DeviceType.ON_OFF_PLUGIN_UNIT,
                                INPUT_CLUSTERS: [
                                        Basic.cluster_id,
                                        Identify.cluster_id,
                                        Groups.cluster_id,
                                        Scenes.cluster_id,
                                        OnOff.cluster_id,
                                        LevelControl.cluster_id,
                                        Time.cluster_id,
                                        MeteringCluster,
                                        ElectricalMeasurement.cluster_id,
                                ],
                                OUTPUT_CLUSTERS: [],
                        },
                        2: {
                                PROFILE_ID: zll.PROFILE_ID,
                                DEVICE_TYPE: 0x1000,
                                INPUT_CLUSTERS: [],
                                OUTPUT_CLUSTERS: [],
                        },
                },
        }


class SP120_2(CustomDevice):
        """Innr SP 120 device."""

        signature = {
                # <SimpleDescriptor
                #   endpoint=1 profile=49246 device_type=0x0010
                #   input_clusters=[0, 3, 4, 5, 6, 8, 10, 1794, 2820]
                #   output_clusters=[]>
                MODELS_INFO: [("innr", "SP 120")],
                ENDPOINTS: {
                        1: {
                                PROFILE_ID: zll.PROFILE_ID,
                                DEVICE_TYPE: zll.DeviceType.ON_OFF_PLUGIN_UNIT,
                                INPUT_CLUSTERS: [
                                        Basic.cluster_id,
                                        Identify.cluster_id,
                                        Groups.cluster_id,
                                        Scenes.cluster_id,
                                        OnOff.cluster_id,
                                        LevelControl.cluster_id,
                                        Time.cluster_id,
                                        Metering.cluster_id,
                                        ElectricalMeasurement.cluster_id,
                                ],
                                OUTPUT_CLUSTERS: [
                                        Identify.cluster_id,
                                        Time.cluster_id,
                                        Ota.cluster_id
                                ],
                        },
                        # <SimpleDescriptor
                        #   endpoint=2 profile=49246 device_type=0x1000
                        #   input_clusters=[]
                        #   output_clusters=[]>
                        2: {
                                PROFILE_ID: zll.PROFILE_ID,
                                DEVICE_TYPE: 0x1000,
                                INPUT_CLUSTERS: [
                                        0x1000,
                                ],
                                OUTPUT_CLUSTERS: [],
                        },
                },
        }

        replacement = {
                ENDPOINTS: {
                        1: {
                                PROFILE_ID: zll.PROFILE_ID,
                                DEVICE_TYPE: zll.DeviceType.ON_OFF_PLUGIN_UNIT,
                                INPUT_CLUSTERS: [
                                        Basic.cluster_id,
                                        Identify.cluster_id,
                                        Groups.cluster_id,
                                        Scenes.cluster_id,
                                        OnOff.cluster_id,
                                        LevelControl.cluster_id,
                                        Time.cluster_id,
                                        MeteringCluster,
                                        ElectricalMeasurement.cluster_id,
                                ],
                                OUTPUT_CLUSTERS: [
                                        Identify.cluster_id,
                                        Time.cluster_id,
                                        Ota.cluster_id
                                ],
                        },
                        2: {
                                PROFILE_ID: zll.PROFILE_ID,
                                DEVICE_TYPE: 0x1000,
                                INPUT_CLUSTERS: [
                                        0x1000,
                                ],
                                OUTPUT_CLUSTERS: [],
                        },
                },
        }
