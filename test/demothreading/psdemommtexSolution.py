from test.objoriented.psoopsssh import CustomSSHClient
import xml.etree.ElementTree as et
import threading


def get_host_info(xml_file):
    try:
        xml_doc = et.parse(xml_file)

        for host_info_tag in xml_doc.getiterator('host-info'):
            host_configuration = list()

            host_configuration.append(host_info_tag.get('address'))
            host_configuration.append(int(host_info_tag.get('port')))

            for host_info_child_tag in host_info_tag:
                host_configuration.append((host_info_child_tag.text))

            yield host_configuration

    except Exception as err:
        print(err)


class SSHClientHandler(CustomSSHClient):
    def __init__(self, host, port, user, pwd, job, target_file):
        super().__init__(host, port, user, pwd)
        self.job = job
        self.target_file = target_file
        self.t_name = threading.current_thread().name
        self.__ssh_handler()

    def __ssh_handler(self):
        payload = self.check_output(self.job)
        caption = '{} ran {} @ {}'.format(self.t_name, self.job, self.host)

        with open(self.target_file, 'a') as fw:
            fw.write(caption.center(80, '-') + '\n')
            fw.write(payload)
            fw.write('-' * 80 + '\n')


class ThreadedSSHClient:
    def __init__(self, host_file):
        self.host_file = host_file
        self.__thread_handler()

    def __thread_handler(self):
        for host_info in get_host_info(self.host_file):
            host_info.append('a.out')  # target file
            t = threading.Thread(target=SSHClientHandler, args=host_info)
            t.start()

        for child in threading.enumerate():
            if child is not threading.current_thread():
                child.join()


if __name__ == '__main__':
    ThreadedSSHClient('hosts.xml')