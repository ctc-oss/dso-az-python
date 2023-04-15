import time
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from dso_az_python.utils.env import SUBSCRIPTION_ID, RESOURCE_GROUP

compute_client = ComputeManagementClient(
    credential=DefaultAzureCredential(),
    subscription_id=SUBSCRIPTION_ID,
    api_version="2021-04-01",
)


def stop(vm_name):
    power_off = compute_client.virtual_machines.begin_power_off(RESOURCE_GROUP, vm_name)

    while not power_off.done():
        print("Powering off...")
        time.sleep(5)

    power_off.wait()


def deallocate(vm_name):
    power_off = compute_client.virtual_machines.begin_deallocate(
        RESOURCE_GROUP, vm_name
    )

    while not power_off.done():
        print("Deallocating...")
        time.sleep(5)

    power_off.wait()


def start(vm_name):
    start = compute_client.virtual_machines.begin_start(RESOURCE_GROUP, vm_name)

    while not start.done():
        print("Powering on...")
        time.sleep(5)
