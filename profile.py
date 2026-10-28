
import geni.portal as portal
import geni.rspec.pg as rspec

pc = portal.Context()
request = pc.makeRequestRSpec()

# Request two bare-metal d7525 nodes running Ubuntu 24.04.
node0 = request.RawPC("node0")
node0.hardware_type = "d7525"
node0.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU24-64-STD"

node1 = request.RawPC("node1")
node1.hardware_type = "d7525"
node1.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU24-64-STD"

# Allocate storage for Docker's data directory on each node.
bs0 = node0.Blockstore("bs0", "/mydata")
bs0.size = "100GB"

bs1 = node1.Blockstore("bs1", "/mydata")
bs1.size = "100GB"

# Connect both nodes to the same LAN with static IPv4 addresses.
lan = request.LAN("lan")

iface0 = node0.addInterface("if0")
iface0.addAddress(
    rspec.IPv4Address("10.10.1.1", "255.255.255.0")
)
lan.addInterface(iface0)

iface1 = node1.addInterface("if1")
iface1.addAddress(
    rspec.IPv4Address("10.10.1.2", "255.255.255.0")
)
lan.addInterface(iface1)

pc.printRequestRSpec()
