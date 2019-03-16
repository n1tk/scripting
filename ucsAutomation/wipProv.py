import csv
#UCS Connection Handle
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan
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

'''Query Compute and Led Objects
from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.110", "admin", "password")

compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        print(compute_resource.dn, leds[0].oper_state)

'''
# query the rack resources
compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

# LEDs for locating the physical component in the data center
for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(
            in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        print('Server Location: ' + compute_resource.dn + 'is the LED ON?:  ' + leds[0].oper_state)

'''
Modify Led Object state


    Retrieve the equipmentLocatorLed operational status of each compute object, change the oper_state to the opposite of the current state using the set_mo and commit methods. The equipmentLocatorLed state is shown via the oper_state however, the state is managed through the admin_state. Use these python statements.

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.113", "admin", "password")

compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        previous_oper_state = leds[0].oper_state

        if leds[0].oper_state == "on":
            leds[0].admin_state = "off"
        else:
            leds[0].admin_state = "on"

        handle.set_mo(leds[0])
        handle.commit()

        print( "dn:",compute_resource.dn,
               "led previous",previous_oper_state,
               "led current",leds[0].admin_state)
'''

for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(
            in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        previous_oper_state = leds[0].oper_state

        if leds[0].oper_state == "on":
            leds[0].admin_state = "off"
        else:
            leds[0].admin_state = "on"

        handle.set_mo(leds[0])
        handle.commit()

        print("dn:", compute_resource.dn,
              "led previous", previous_oper_state,
              "led current", leds[0].admin_state)


'''
Modifying UCS Manager object with the Python SDK is pretty easy, just follow these steps.

* Retrieve the objects with a query
* Modify the object
* Set the object in the handle with the method set_mo()
* Commit the object with the handle method commit()
'''

import csv

def createVlan(parameter_list):
    pass

########## Create VLANs objects ################

'''
How works: 
UCS Manager VLANs are a simple object to create and understanding how to create a VLAN allows you to understand how to create any UCS Manager object.

The process to creating a new UCS Manager object starts with knowing the dn of the parent object or retrieving the parent object, of the object you are creating. The UCS Manager objects are arranged in a hierarchical model, when a new object is created it needs to be placed in the object model under its' parent.

VLAN objects typically reside under the Lan Cloud. You could specify the dn for the Lan Cloud but best practice would be to use a query to retrieve the Lan Cloud object.

In addition to importing the UcsHandle module you will also need to import the FabricVlan module. Think of the module as a recipe for creating a VLAN.

    Create vlan100. Use these python statements.

There is no output indicating successful completion of the operation, no error is an indication of a successful operation. However, if you wanted to ensure that the object was created just query for it.

In this operation the add_mo() handle method was used with two arguments. The first argument, like set_mo() is the object, the second argument could have been written as modify_present=True. Since the modify_present is the second argument in the add_mo method definition Python lets up just provide the value without having to provide the argument name.

modify_present allows the add_mo() method to act like a set_mo() and update the object if it already exists. By default modify_present is False meaning that if add_mo() was being used to create an object that already exists then the add operation would fail.
'''

handle = UcsHandle("192.168.193.138", "ucspe", "ucspe", secure=False)

lan_cloud = handle.query_classid("FabricLanCloud")
vlan_mo = FabricVlan(parent_mo_or_dn=lan_cloud[0], name="vlan_1001", id="1001")
handle.add_mo(vlan_mo, modify_present=True)

handle.commit()


################ Create UCS Manager VLANs in a Transaction ##############

''' 
UCS Manager Python SDK commit() can commit more than one object at a time, in fact the objects can be of different classes. Objects can be continually added to the handle and a single call to commit() will commit them all. This is called a Transaction, a few caveats apply.

    If one object fails to be created everything up to that point is rolled back and nothing is created.
    Objects in the Transaction cannot have dependencies on each other.
    Objects only become visible to others users of UCS Manager when the Transaction is complete.

UCS Manager is Transaction oriented by default adding objects to the handle and committing them is the standard process. Using Transactions for processes that create many objects is far more efficient than processing each object one at a time.

    Create vlan200, vlan201, vlan202 in a Transaction. Use these python statements.

'''

lan_cloud = handle.query_classid("FabricLanCloud")

vlans = ["200", "201", "202"]

for vlan in vlans:
    vlan_mo = FabricVlan(parent_mo_or_dn=lan_cloud[0], name="vlan"+vlan, id=vlan)
    print('Check what object/parameters are inside:', vlan_mo)
    handle.add_mo(vlan_mo, modify_present=True)
handle.commit()

############## Delete UCS Manager VLANs in a Transaction ####################

'''
It is that simple. In the example you iterated over the values in the vlans list, 
created the vlan_mo object, and added the object to the handle with add_mo(). 
After all the vlan objects were added to the handle, the commit() method was used to create the objects in UCS Manager.

To Delete or remove UCS Manager objects, query for the object and add the removal of the object to the handle with the remove_mo() method.

Remove the VLANs created in this lab, be sure not to remove VLAN 1, the default VLAN. Use these python statements.

'''

vlans = handle.query_classid("FabricVlan")

for vlan_mo in vlans:
    if vlan_mo.id != "1":
        handle.remove_mo(vlan_mo)


handle.commit()


############# Disconnect from UCS Manager. Use this python statement. ##############
handle.logout()
