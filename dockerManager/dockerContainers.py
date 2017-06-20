from docker import APIClient

class Container:
    def __init__(self):
        self.cli = APIClient(base_url='unix://var/run/docker.sock')

    def start(self, image, cmd, service_port=[]):
        port_bindings = {}
        for i in service_port:
            port_bindings[i] = port_bindings.get(None)
        self.container = self.cli.create_container(image, cmd, ports=service_port,
            host_config = self.cli.create_host_config(port_bindings=port_bindings)
        )
        resp = self.cli.start(container = self.container.get('Id'))
        return resp



if __name__ == '__main__':
    container =  Container()
    container_info = container.start('ubuntu', 'tail -f /etc/hosts', [8080])
    print container_info
