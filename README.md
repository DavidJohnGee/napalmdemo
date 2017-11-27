## NAPALM Demo Pack

__Introduction__

This pack offers some 'wrapping' of NAPALM to demonstrate what could be possible for your project.

The story is there are some routers with BGP configured between them. We want to automate receiving additional prefixes and testing for reachability of a node within the new prefix.

1.	Create a virtual Cisco CSR and a virtual Juniper SRX
2.	Configure BGP between those devices (could be between each other, or something else)
3.	Create a configuration that uses a prefix-list called INBOUND
4.	Configure the INBOUND prefix-list to accept a prefix from a remote BGP peer
5.	Install StackStorm/EWC and NAPALM. Configure NAPALM and the hosts file (see the Installation section)
6.	Link StackStorm/EWC to Slack or some other collaboration platform

Once you're at this stage, it's possible to exercise the workflows.

1.	Run the `add_device` action to add a device to the kv store. You can validate with `st2 key list` once you've ran this action.
2.	Run the `wf_add_prefix` workflow to add a prefix to each of the routers INBOUND prefix-lists, clear down the BGP session (softly) and attempt to ping the test nodes. Ensure you input an IP address for the `test` field. 
3.	Enjoy and sit smugly watching your tests automate.

This could be used as a part of a CI/CD pipeline to validate reachability after configuration push.

Note, also in the `deviceconfigs` directory resides the base configuration for CSR01 and SRX01. Feel free to use these for speed if you need it!

__Installation__

You will need to install NAPALM and provide configuration for your reachable nodes.

You will also need to add entries in to the `/etc/hosts` file to ensure reachability by FQDN of the devices.
It's recommended to call the device in the `/etc/hosts` file the same as the device name in the NAPALM configuration file.

You will need to create the `/snippets` directory in the root file system. This directory is used by some of the actions to store temporary configuration files for NAPALM.

__Usage__

Go here for a Youtube video on basic usage.

https://www.youtube.com/watch?v=MD3P3_MR8J0

__Support__

No support is provided with this pack. If you want to see new features, please create them and create a pull request to add them!

This pack is not designed to satisfy production requirements. This is a demo pack and if you want to use it in production, do so at your own risk!
