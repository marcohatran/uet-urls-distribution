from controller.host_controller import find_hosts


def update_host_piority():
    hosts_obj = find_hosts()
    print(hosts_obj)


update_host_piority()
