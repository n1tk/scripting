import csv
#UCS Connection Handle
from ucsmsdk.ucshandle import UcsHandle

''' 
#Create Organization
from ucsmsdk.mometa.org.OrgOrg import OrgOrg
#UUID Pool
from ucsmsdk.mometa.uuidpool.UuidpoolPool import UuidpoolPool
from ucsmsdk.mometa.uuidpool.UuidpoolBlock import UuidpoolBlock
#VLAN
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan
#Sever Pool
from ucsmsdk.mometa.compute.ComputePool import ComputePool
from ucsmsdk.mometa.compute.ComputePooledSlot import ComputePooledSlot
#Maintenance Policy
from ucsmsdk.mometa.lsmaint.LsmaintMaintPolicy import LsmaintMaintPolicy
#Power Policy
from ucsmsdk.mometa.power.PowerPolicy import PowerPolicy
#Create IP Pool
from ucsmsdk.mometa.ippool.IppoolPool import IppoolPool
from ucsmsdk.mometa.ippool.IppoolBlock import IppoolBlock
#Create MAC Pool
from ucsmsdk.mometa.macpool.MacpoolPool import MacpoolPool
from ucsmsdk.mometa.macpool.MacpoolBlock import MacpoolBlock
#Create Network Control Policy
from ucsmsdk.mometa.nwctrl.NwctrlDefinition import NwctrlDefinition
from ucsmsdk.mometa.dpsec.DpsecMac import DpsecMac
#FC WWNN and WWPN Pools
from ucsmsdk.mometa.fcpool.FcpoolInitiators import FcpoolInitiators
from ucsmsdk.mometa.fcpool.FcpoolBlock import FcpoolBlock
#Create vNIC Templates
from ucsmsdk.mometa.vnic.VnicLanConnTempl import VnicLanConnTempl
from ucsmsdk.mometa.vnic.VnicEtherIf import VnicEtherIf
#Create Local Disk Conf Policy
from ucsmsdk.mometa.storage.StorageLocalDiskConfigPolicy import StorageLocalDiskConfigPolicy
#Create Boot Policy
from ucsmsdk.mometa.lsboot.LsbootPolicy import LsbootPolicy
from ucsmsdk.mometa.lsboot.LsbootVirtualMedia import LsbootVirtualMedia
from ucsmsdk.mometa.lsboot.LsbootStorage import LsbootStorage
from ucsmsdk.mometa.lsboot.LsbootLocalStorage import LsbootLocalStorage
from ucsmsdk.mometa.lsboot.LsbootUsbFlashStorageImage import LsbootUsbFlashStorageImage
#Create HBA Template
from ucsmsdk.mometa.vnic.VnicSanConnTempl import VnicSanConnTempl
from ucsmsdk.mometa.vnic.VnicFcIf import VnicFcIf
#Configuring Uplink ports
from ucsmsdk.mometa.fabric.FabricEthLanEp import FabricEthLanEp
#Configure Port Channels
from ucsmsdk.mometa.fabric.FabricEthLanPc import FabricEthLanPc
from ucsmsdk.mometa.fabric.FabricEthLanPcEp import FabricEthLanPcEp
#Create Service Profile Template
from ucsmsdk.mometa.ls.LsServer import LsServer
from ucsmsdk.mometa.ls.LsVConAssign import LsVConAssign
from ucsmsdk.mometa.vnic.VnicEther import VnicEther
from ucsmsdk.mometa.vnic.VnicFc import VnicFc
from ucsmsdk.mometa.vnic.VnicFcIf import VnicFcIf
from ucsmsdk.mometa.vnic.VnicFcNode import VnicFcNode
from ucsmsdk.mometa.ls.LsRequirement import LsRequirement
from ucsmsdk.mometa.ls.LsPower import LsPower
from ucsmsdk.mometa.fabric.FabricVCon import FabricVCon

'''

# login into the ucsm, create handle.
handle = UcsHandle("192.168.193.138","ucspe","ucspe",secure=False)
handle.logout()

vars(handle)


handle.query_classid('computeBlade')
blades = handle.query_classid("computeBlade")
print(blades)

# get the info for the blades, each at the time itterating
for blade in blades:
    print(blade)

# get the specified info from each blade object, in this case we just have the dn(location of blade), CPu and the memory
for blade in blades:
    print(blade.dn, blade.num_of_cpus, blade.available_memory)

# query the rack resources
compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

# LEDs for locating the physical component in the data center
for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(
            in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        print('Server Location:' compute_resource.dn, 'is the LED ON?:'leds[0].oper_state)
